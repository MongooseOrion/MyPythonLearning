import os

def search_files(folder_path, keyword):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                if keyword in content:
                    print(f"Found keyword '{keyword}' in file: {file_path}")

folder_path = 'C:\\Users\\smn90\\Desktop\\PDS2022.2-lite_wujian100\\race_info\\MES50HP\\MES50HP_v2\\01_demo_document_alinx\\demo\\video_ethernet\\video_ethernet\\source\\'
keyword = '1024'
search_files(folder_path, keyword)