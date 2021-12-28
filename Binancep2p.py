from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.utils import ChromeType



driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install()) # Here I am using chrome
# Lets maximize 
driver.maximize_window()
# Lets open the application ,we want to scrap
driver.get("https://p2p.binance.com/en/trade/buy/USDT?fiat=NGN&payment=ALL")
# Wait for the particular time 
driver.implicitly_wait(10)

print("*****************")

driver.find_element(By.XPATH,"//h2[contains(@class,'css-4enzhw')]").click()
# advertisers,prices,available,limit,payment store the list of web elements:
advertisers = driver.find_elements(By.XPATH,"//a[contains(@id,'C2Cofferlistsell_link_merchant')]")
prices = driver.find_elements(By.XPATH,"//div[contains(@class,'css-1kj0ifu')]")
available = driver.find_elements(By.XPATH,"//div[contains(@class,'css-3v2ep2')]/div[2]")
limit = driver.find_elements(By.XPATH,"//div[contains(@class,'css-16w8hmr')]/div[2]")
payment = driver.find_elements(By.XPATH,"//div[contains(@class,'css-1n3cl9k')]")


myadv = []
myprice = []
myava = []
mylm = []
mypay = []

for adv in advertisers:
    print(adv.text)
    myadv.append(adv.text)

print('******************')

for price in prices:
    print(price.text)
    myprice.append(price.text)

print('******************')

for ava in available:
    print(ava.text)
    myava.append(ava.text)


for lm in limit:
    print(lm.text)
    mylm.append(lm.text)

print('******************')

for pay in payment:
    print(pay.text)
    mypay.append(pay.text)

print('******************')
print('*****list**********')
finallist = zip(myadv,myprice,myava,mylm,mypay)
#print(list(finallist))

for data in list(finallist):
    print(data)

driver.implicitly_wait(10)
driver.quit()





