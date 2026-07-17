from faker import Faker
import pandas as pd

fake = Faker()

customers = []

for i in range(1,101):

    customer = {
        "CustomerID": i,
        "Name": fake.name(),
        "Email": fake.email(),
        "Phone": fake.msisdn()[:10],
        "City": fake.city()
    }

    customers.append(customer)

df = pd.DataFrame(customers)

df.to_csv("customers.csv", index=False)
print("Customer data generated successfully!")