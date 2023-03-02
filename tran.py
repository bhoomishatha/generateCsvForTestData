from faker import Faker
import pandas as pd
import random

fake = Faker()

card = pd.read_csv('credit_cards.csv',index_col=False)
type =["DR","CR"]
l = len(card)
print(l)

def create_rows_faker(num,start):
    output = [{
        "card_number":card["card_number"][random.randint(0,l-1)],
        "amount":random.randint(1,100000),
        "type":type[random.randint(0,1)],
        "date":fake.date_time(),
        "narration":str(fake.text()).replace("\n"," ")
    } for x in range(num)]
    return output

final =[]

for x in range(0,400):
    print(x)
    final.append(pd.DataFrame(create_rows_faker(10000,10000)))




dfzz = pd.concat(final)




dfzz.to_csv("tranx.csv",index=False)