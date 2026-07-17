import pandas as pd
import sqlite3

# Read customer data
df = pd.read_csv("customers.csv")

# Connect to SQLite database
conn = sqlite3.connect("ecommerce.db")

# Store data into a table named 'customers'
df.to_sql("customers", conn, if_exists="replace", index=False)

print("Data stored successfully in SQLite database!")

# Close the connection
conn.close()