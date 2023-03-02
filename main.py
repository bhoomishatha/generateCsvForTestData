from faker import Faker
import pandas as pd
import numpy as np
import random
fake = Faker()

gender = np.random.choice(["M", "F"], p=[0.5, 0.5])

def create_rows_faker(num,start):
    output = [{"id":x,
                   "name":fake.name(),
                   "address":str(fake.address()).replace("\n"," "),
                   "email":fake.email(),
                   "city":fake.city(),
                   "state":fake.state(),
                   "date_time":fake.date_time(),
                   "gender":gender,
                   "contact":fake.phone_number()} for x in range(start,start+num)]
    return output

start = 1
final =[]
for x in range(1,101):
    print(x)
    final.append(pd.DataFrame(create_rows_faker(10000,start)))
    start = start + 10000

df6 = pd.concat(final)
print("The Total")
df6.to_csv("customer.csv",index=False)