# coding: utf-8
import pymysql

db = pymysql.connect(host='192.168.56.100', user='root', password='root', database='summo')

cursor = db.cursor()

page = 1

while page < 100:
    print("url" + (str(page)))
    page += 1
# sql = "SELECT * FROM house  WHERE title = %s" % (1000)
# cursor.execute("select * from house where title = '%s'" % ('エステートピアマツモト - (株)ミニミニ城東行徳店が提供する賃貸物件情報'))
# cursor.execute(sql)
# results = cursor.fetchall()
# print(results)
# if (len(results) > 0):
#     exit(0)