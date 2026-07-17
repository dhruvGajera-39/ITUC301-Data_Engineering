import pandas as pd

# Read the CSV file
df = pd.read_csv("customers.csv")

# Display first 5 records
print("First 5 Records:")
print(df.head())

# Display information about the dataset
print("\nDataset Information:")
print(df.info())

# Display column names
print("\nColumn Names:")
print(df.columns)

# Display missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Display number of rows and columns
print("\nDataset Shape:")
print(df.shape)