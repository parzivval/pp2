
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="_",
)

sql = "select * from phonebooks" 

cursor = conn.cursor() 
cursor.execute(sql) 
conn.commit()

contacts = cursor.fetchall()
for contact in contacts:
    print(contact)

cursor.close() 
conn.close()