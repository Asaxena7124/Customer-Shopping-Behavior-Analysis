import pyodbc

conn = pyodbc.connect(
    'Driver={ODBC Driver 18 for SQL Server};'
    'Server=ANUBHAV_PC;'
    'Database=customer_behaviour;'
    'Trusted_Connection=yes;'
    'Encrypt=no;'
)

cursor = conn.cursor()
print("Connection successful!")


