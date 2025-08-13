from Connection import get_connection

def select_query():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Employee")

    for row in cursor.fetchall():
        print(row)

    conn.close()

select_query()



