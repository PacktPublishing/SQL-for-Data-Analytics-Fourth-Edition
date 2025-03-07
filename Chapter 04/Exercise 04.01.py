# Step 5
import psycopg2
conn = psycopg2.connect(
        host="localhost", 
        user="postgres", 
        password="<your superuser password>", 
        dbname="sqlda", 
        port=5432
) 

# Step 6
cur = conn.cursor() 
cur.execute("SELECT * FROM customers LIMIT 2") 
records = cur.fetchall()
print(records)


