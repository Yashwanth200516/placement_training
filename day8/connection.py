from dbconnect import connect_db

try:
    conn=connect_db()
    if conn.is_connected():
        print("connection success")
    conn.close()
except Exception as e:
    print(f"error:{e}")