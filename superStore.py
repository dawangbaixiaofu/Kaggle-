import pandas as pd
import numpy as np

data = pd.read_csv(r'D:\Github\kaggle\superstore_dataset2011-2015.csv', encoding='ISO-8859-1')
# str.encode('new code')把Python默认的编码转化为新的编码方式  str.decode('old code')把原有编码转换为Python3默认的编码
print('数据的大小：', data.shape)

data.rename(columns=lambda x:x.replace(' ','_').replace('-','_'), inplace=True)
# 对order_date 进行类型转换
data['Order_Date'] = pd.to_datetime(data['Order_Date'])
data['Order_Year'] = data['Order_Date'].dt.year
data['Order_Month'] = data['Order_Date'].dt.month
# 每列缺失值统计
print('每列缺失值个数统计：\n',data.isnull().sum(axis=0))

# 缺失值较多的是Postal_Code列，进行删除处理
data.drop(columns=['Postal_Code'], axis=1, inplace=True)

# 分析部分
# 销售部分分析
sales_element = ['Order_Date', 'Sales', 'Quantity', 'Profit', 'Order_Year', 'Order_Month']
sales = data.loc[:, sales_element]
# 对年月进行销售额，销售量和利润进行分组求和
sales_group = sales.groupby(['Order_Year','Order_Month']).sum()

# 计算每一年的增长率

# 找出淡季和旺季，重点销售月份

# 利润和利润率

# 客单价， 每年的消费次数 消费总金额

# 市场布局分析,不同地区每年全部销售额分布情况

# 四年来各个地区销售额占总销售额的百分比：看下各个地区排名

# 商品销售数量，金额，利润，进行排序，销售前10的商品

# 按照不同种类的商品分别按照销售额和利润进行排序统计

# 统计每种商品销售额的累积占比


# 用户情况分析
# 不同类型的客户占比，不同类型客户的每年的数量
# 不同类型客户每年的销售额


# 客户下单行为分析：用户第一次购买日期分布。用来看下最近新增用户
# 用户最近一次购买日期分布，可以看出用户是否流失严重

# RFM模型分析








