import os

# 指定路径和文件类型
path = 'C:/Users/smn90/repo/FPGA-Image-Recognition/RTL/'
output_file = 'C:/Users/smn90/repo/FPGA-Image-Recognition/RTL/main.filelist'
extension = '.v'

file_list = []
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(extension):
            file_list.append(file)

with open(output_file, 'a') as f:
        for item in file_list:
            f.write(item + '\n')