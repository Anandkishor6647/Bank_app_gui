import mysql.connector

my_db = mysql.connector.connect(host="localhost", username="Anand", password="Anand@6647", database="bank_db")
my_cursor = my_db.cursor()


def write(val):
    sql = "INSERT INTO cus_table (Id,name,email,mob,pass,balance) VALUES (%s,%s,%s,%s,%s,%s)"
    my_cursor.executemany(sql, val)
    my_db.commit()


def clear():
    sql = "truncate cus_table"
    my_cursor.execute(sql)


def show_db():
    sql = "SELECT * FROM cus_table"
    my_cursor.execute(sql)
    data_out = my_cursor.fetchall()
    return data_out


def update(amount, ac_num):
    sql = "UPDATE cus_table SET balance = %s WHERE id = %s"
    values = (amount, ac_num)
    my_cursor.execute(sql, values)
    my_db.commit()

#
# clear()
# print(show_db())
