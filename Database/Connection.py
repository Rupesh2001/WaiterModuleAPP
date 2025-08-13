import pyodbc

server = r'DESKTOP-1G19QOT'
database = 'Test'

def get_connection():
    try:
        conn = pyodbc.connect(
            f'DRIVER={{SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'Trusted_Connection=yes;'
        )
        return conn
    except Exception as e:
        print("Connection failed:", e)
        return None

# Use the function and test if connection is successful
conn = get_connection()
if conn is not None:
    print("Connection successful")
    conn.close()
else:
    print("Connection could not be established")
