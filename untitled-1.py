import pymysql

conn = pymysql.connect(host="localhost", user="root", passwd="macbook", db="blood_donation_db")

cursor = conn.cursor()

sql = "SELECT * FROM blood_donor"

print (c.fetchall())