#
# uart 上位机功能
#

import serial

# 串口配置
ser = serial.Serial(
    port='COM10',           # 串口端口
    baudrate=115200,        # 波特率
    timeout=1               # 超时时间，单位秒
)

# 打开串口
#ser.open()

try:
    while True:
        # 读取串口数据
        data = ser.readline().decode('HEX').strip()
        
        if data:
            print(f"Received: {data}")
        
except KeyboardInterrupt:
    pass

# 关闭串口
ser.close()
