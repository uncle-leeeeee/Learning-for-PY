import pandas as pd
import numpy as np
import cx_Oracle
import os
os.environ['path'] = r'D:\software\instantclient_11_2'  # 设置instantclient环境变量位置
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
print("cx_Oracle.version:", cx_Oracle.version)
connection = cx_Oracle.connect(
    'hgxt', 'hgxt_gx#11', cx_Oracle.makedsn('10.0.109.9', '1521', 'sjzx9'))

cursor = cx_Oracle.Cursor(connection)
print('连接成功')
s1 = 'select * from qzj_tar.V_D_O_DLYS_KEHUOYUNYEHU'
yzk = pd.read_sql(s1, connection)
yzk.to_csv('yzk.csv')
print('输出成功')
