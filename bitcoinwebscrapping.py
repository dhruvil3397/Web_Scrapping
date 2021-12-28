from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager import chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.utils import ChromeType

import sqlite3
from sqlite3 import Error
from datetime import datetime
from django.utils.text import slugify




driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install()) # Here I am using chrome

# Lets maximize it
driver.maximize_window()
# Lets open the application ,we want to scrap
driver.get("https://localbitcoins.com/instant-bitcoins/?action=buy&amount=500000&currency=NGN&country_code=NG&online_provider=ALL_ONLINE&find-offers=Search")
driver.implicitly_wait(10)

trader = driver.find_elements(By.XPATH,"//tr[contains(@class,'clickable')]")

payment = driver.find_elements(By.XPATH,"//tr[contains(@class,'clickable')]/td[2]")

price = driver.find_elements(By.XPATH,"//tr[contains(@class,'clickable')]/td[3]")

limits = driver.find_elements(By.XPATH,"//tr[contains(@class,'clickable')]/td[4]")

mytrader = []
for trade in trader:
    a =trade.text
    b = a.split()
    # print(b[0])
    mytrader.append(b[0])

mypayment =[]
for pay in payment:
    a1 = pay.text
    # print(a1)
    mypayment.append(a1)

myprice =[]
for prc in price:
    a2 = prc.text
    # print(a2)
    myprice.append(a2)

mylimits =[]
for lim in limits:
    a3 = lim.text
    # print(a3)
    mylimits.append(a3)

finalrecord = zip(mytrader,mypayment,myprice,mylimits)

# for data in list(finalrecord):
#     print(data)

dicts_data = []
for a,b,c,d in finalrecord:
                dicts = {}
                dicts['Trader'] = a
                dicts['Payment method'] = b
                dicts['Price/BTC'] = c
                dicts['limits'] = d

                dicts_data.append(dicts)
# print(dicts_data)


driver.implicitly_wait(10)
driver.quit()



print('**********************')
trader1 = dicts_data[0]
z0 =[]
z1 =[]
z2 =[]
z3 =[]
z4 =[]
z5 =[]
time = str(datetime.now())

for i in range(len(dicts_data)):
    z0.append(time)
    z1.append(dicts_data[i]['Trader'])
    z2.append(dicts_data[i]['Payment method'])
    z3.append(dicts_data[i]['Price/BTC'])
    z4.append(dicts_data[i]['limits'])
    z5.append(slugify(dicts_data[i]['Trader']))



# print(z0)
# print(z1)
# print(z2)
# print(z3)
# print(z4)
# print(z5)

time = str(datetime.now())

print('.................')
final = zip(z0,z1,z2,z3,z4,z5)
final1 = zip(z0,z1,z2,z3,z4,z5)

def sql_connector():
    try:
        con = sqlite3.connect('bitcoin.db')
        print('Created')
        return con
    except Error:
        print('Error')


con = sql_connector()


def table_create():
    table_data = con.cursor()
    table_data.execute(
        'create table if not exists Data1(Time TEXT ,Trader TEXT,Payment_method TEXT,Price TEXT,Limits TEXT,Slugify TEXT type UNIQUE)')

        


def record_insert(final,final1):
    table_data = con.cursor()
    data = table_data.execute('select Slugify from Data1')
    db = []
    for i in data:
        for j in i:
            db.append(j)
    print(db)  

    new = []
    for i in final:
        new.append(i)
    # print(new)
    w = []
    if len(db) == 0:
             print('none')
             table_data.executemany(
                            'insert into Data1(Time,Trader,Payment_method,Price,Limits,Slugify) values(?,?,?,?,?,?)', final1)
             print('inserted')
    else:
        for i in new:
            
            if i[5] not in db :
                w.append(i)
                table_data.executemany(
                                'insert into Data1(Time,Trader,Payment_method,Price,Limits,Slugify) values(?,?,?,?,?,?)', w)
                print('done')
            else:
                
                table_data.executemany(
                    'update  Data1 set  Time = ?,Trader =?,Payment_method = ?,Price = ?,Limits= ? where Slugify = ? ' ,final1)
                print('update')
   

table_create()
record_insert(final,final1)

con.commit()
con.close()
