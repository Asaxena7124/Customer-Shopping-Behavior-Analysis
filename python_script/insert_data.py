import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("customer_shopping_behavior.csv")

# Rename CSV columns to match SQL table
df.columns = [
    "customer_id",
    "age",
    "gender",
    "item_purchased",
    "category",
    "purchase_amount",
    "location",
    "size",
    "color",
    "season",
    "review_rating",
    "subscription_status",
    "shipping_type",
    "discount_applied",
    "promo_code_used",
    "previous_purchases",
    "payment_method",
    "frequency_of_purchases"
]

engine = create_engine(
    "mssql+pyodbc://ANUBHAV_PC/customer_behaviour?driver=ODBC+Driver+18+for+SQL+Server&Encrypt=no&Trusted_Connection=yes"
)

df.to_sql("customer_data", engine, if_exists="append", index=False)

print("Data inserted successfully!")
