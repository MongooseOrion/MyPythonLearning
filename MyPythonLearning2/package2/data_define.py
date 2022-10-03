#
# 用于进行数据定义的类
#
class Record(object):
    
    def __init__(self, data, order_id, money, province):
        self.data = data                        # 订单日期
        self.order_id = order_id                # 订单 ID
        self.money = money                      # 订单金额
        self.province = province                # 销售省份


