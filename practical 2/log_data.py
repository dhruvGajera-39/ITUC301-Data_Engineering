import pandas as pd

# Read customer data
df = pd.read_csv("customers.csv")

# Open log file
with open("quality.log", "w") as log:

    log.write("DATA QUALITY REPORT\n")
    log.write("===================\n\n")

    for index, row in df.iterrows():

        # Check Email
        if pd.isnull(row["Email"]) or "@" not in str(row["Email"]):
            log.write(f"Row {index+1}: Invalid Email\n")

        # Check Phone
        if len(str(row["Phone"])) != 10:
            log.write(f"Row {index+1}: Invalid Phone Number\n")

print("Quality log created successfully!")