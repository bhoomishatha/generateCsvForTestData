from faker import Faker
import pandas as pd
import random
fake = Faker()

card_type=['maestro', 'mastercard', 'visa16', 'visa13', 'visa19', 'amex', 'discover', 'diners', 'jcb15', 'jcb16']

id =0

def generate_card(n):
    global id
    id =n
    return fake.credit_card_number(card_type=card_type[n])

def create_rows_faker(num,kk):
    output = [{"customer_id":random.randint(1,2000000),
                   "card_number":generate_card(random.randint(0,9)),
                   "limit":random.randint(10000,1000000),
                   "card_type":card_type[id]} for x in range(num)]
    return output

final = []
for x in range(0,200):
    print(x)
    final.append(pd.DataFrame(create_rows_faker(10000,10000)))


data = pd.concat(final)
data.to_csv("credit_cards.csv",index=False)
