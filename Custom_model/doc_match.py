import os
import json
import re
import win32com.client

# 设置文档目录和输出JSON文件路径
doc_directory = 'C:\\Users\\smn90\\Desktop\\100份判决\\'
output_json_path = os.path.join(doc_directory, 'output.json')

# 初始化存储结果的字典
results = []

# 创建Word应用程序对象
word_app = win32com.client.Dispatch("Word.Application")

# 正则表达式模式
#title_pattern = r"案件名称：(.*?)(?=\n|$)"
date_pattern = r"裁判日期：(\d{4}\.\d{2}\.\d{2})"
law_pattern = r"依照(.*?)规定"
plaintiff_pattern = r"原告：(.*?)[，。]"
defendant_pattern = r"被告：(.*?)[，。]"
claim_pattern = r"诉讼请求[：\r](.*?元)"
result_pattern = r"裁判结果[:\r](.*?元)"


# 遍历文档目录中的所有文档文件
for filename in os.listdir(doc_directory):
    if filename.endswith('.doc') and not filename.startswith('~$'):
        file_path = os.path.join(doc_directory, filename)
        
        # 打开Word文档
        doc = word_app.Documents.Open(file_path)
        
        # 初始化当前文件的结果字典
        file_result = {'文件名': filename}
        
        # 获取整个文档的内容
        doc_content = doc.Range().Text
        
        # 使用文件名作为标题
        lines = filename.split(sep='.')
        if lines:
            file_result['案件名称'] = lines[0]
        
        # 匹配判决时间
        date_match = re.findall(date_pattern, doc_content)
        if date_match:
            file_result['判决时间'] = date_match
        
        # 匹配依照法条
        law_matches = re.findall(law_pattern, doc_content)
        if law_matches:
            file_result['依照法条'] = law_matches

        # 匹配原告
        plaintiff_match = re.findall(plaintiff_pattern, doc_content)
        if plaintiff_match:
            file_result['原告'] = plaintiff_match

        # 匹配被告
        defendant_match = re.findall(defendant_pattern, doc_content)
        if plaintiff_match:
            file_result['被告'] = defendant_match

        # 匹配诉讼请求和裁判结果
        claim_match = re.findall(claim_pattern, doc_content)
        if claim_match:
            claim_amounts = re.findall(r"赔偿(.*?元)", ' '.join(claim_match))
            if claim_amounts:
                file_result['诉讼请求'] = [amount.strip() for amount in claim_amounts]
        result_match = re.findall(result_pattern, doc_content)
        if result_match:
            result_amounts = re.findall(r"赔偿(.*?元)", ' '.join(result_match))
            if result_amounts:
                file_result['裁判结果'] = [amount.strip() for amount in result_amounts]
        
        # 关闭文档
        doc.Close()
        
        # 将当前文件的结果添加到列表中
        results.append(file_result)

# 关闭Word应用程序
word_app.Quit()

# 将结果写入JSON文件
with open(output_json_path, 'w', encoding='utf-8') as json_file:
    json.dump(results, json_file, ensure_ascii=False, indent=4)

print("匹配结果已写入JSON文件。")
