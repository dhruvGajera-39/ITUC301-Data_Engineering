import pandas as pd

# Read customer data
df = pd.read_csv("customers.csv")

print("Checking Data Quality...\n")

# Check for missing values
print("Missing Values:")
print(df.isnull().sum())

print("\nInvalid Records:")

for index, row in df.iterrows():

    # Check email
    if pd.isnull(row["Email"]) or "@" not in str(row["Email"]):
        print(f"Row {index+1}: Invalid Email")

    # Check phone number
    if len(str(row["Phone"])) != 10:
        print(f"Row {index+1}: Invalid Phone Number")