from faker import Faker
import json
fake_ru =Faker('ru_RU')
#print(fake_ru.name())
# print(fake_ru.isbn10())
#print(fake_ru.phone_number())
#print(fake_ru.job())
#print(fake_ru.address())

# a, b, c, d =fake_ru.name(), fake_ru.phone_number(), fake_ru.job(), fake_ru.address()
#for i in range(1:5):

dict_={}
for i in range(1,250):
    name = fake_ru.name()
    tn = fake_ru.phone_number()
    j = fake_ru.job()
    ad = fake_ru.address()
    dict_[i]={name:[ad, j, tn]}
    with open ("DS.txt",'w',encoding='utf-8') as f:
        json.dump(dict_, f, indent = 4, ensure_ascii = False)

#121