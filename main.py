import pandas as pd
import numpy as np
import cx_Oracle
import os
os.environ['path'] = r'D:\software\instantclient_12_1'  # 设置instantclient环境变量位置
connection = cx_Oracle.connect(
    'hgxt', 'hgxt_gx#11', '10.0.109.9:1521/ORCL')  # 需要以SYSDBA身份进行登录，否则会报错

# 遍历六月份的gps数据，根据起始点经纬度，计算每个物流园区的到发量（由距离公式，如果到圆心距离小于3km，则属于从该点出发或到达该点）
s1 = 'select startpx,startpy,endpx,endpy from GPS_OUTPUT_RAW_202106_T1 group by startpx,startpy,endpx,endpy'
car_SE = pd.read_sql(s1, connection)
car_SE = car_SE[['STARTPX', 'STARTPY', 'ENDPX', 'ENDPY']].values
