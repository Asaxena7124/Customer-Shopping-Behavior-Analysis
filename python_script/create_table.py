import pyodbc

conn = pyodbc.connect(
    'Driver={ODBC Driver 18 for SQL Server};'
    'Server=ANUBHAV_PC;'
    'Database=customer_behaviour;'
    'Trusted_Connection=yes;'
    'Encrypt=no;'
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE customer_data (
    customer_id VARCHAR(50),
    age INT,
    gender VARCHAR(20),
    item_purchased VARCHAR(100),
    category VARCHAR(100),
    purchase_amount FLOAT,
    location VARCHAR(100),
    size VARCHAR(50),
    color VARCHAR(50),
    season VARCHAR(50),
    review_rating FLOAT,
    subscription_status VARCHAR(50),
    shipping_type VARCHAR(50),
    discount_applied VARCHAR(10),
    promo_code_used VARCHAR(10),
    previous_purchases INT,
    payment_method VARCHAR(50),
    frequency_of_purchases VARCHAR(50)
)
""")

conn.commit()
print("Table created successfully!")
