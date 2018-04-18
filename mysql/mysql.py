import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "lxn", "Blue1989pawn821_", "Scraw")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 使用execute方法执行SQL语句
cursor.execute("select version()")
# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()
print("Database version : %s " % data)

# # 如果数据表已经存在使用 execute() 方法删除表。
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#
# # 创建数据表SQL语句
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""
#
# cursor.execute(sql)

# # SQL 插入语句
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# try:
#     # 执行sql语句
#     cursor.execute(sql)
#     # 提交到数据库执行
#     db.commit()
# except:
#     # Rollback in case there is any error
#     db.rollback()


# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
              (fname, lname, age, sex, income))
except:
    print("Error: unable to fecth data")

db.close()
