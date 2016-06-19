#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########### prepare ###########

#install mysql-connector-python3
#pip install mysql-connector-python-rf

import mysql.connector

#change root password to you:
conn = mysql.connector.connect(host='localhost', user='root',password='901112',database='test')

cursor = conn.cursor()
#创建user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#插入一行记录，注意Mysql的占位符是%：
cursor.execute('insert into user (id,name) values (%s,%s)',('1','Michael'))
print('rowcount =', cursor.rowcount)
#提交事务：
conn.connit()
cursor.close()

#运行查询：
cursor = conn.cursor()
cursor.execute('select * from user where id = %s',('1',))
values = cursor.fetchall()
print(values)
#关闭cursor和connection:
cursor.close()
conn.close()
