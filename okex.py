from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager import chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.utils import ChromeType

from selenium.webdriver.common.action_chains import ActionChains # For hover in selenium


driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install()) # Here I am using chrome

# Lets maximize it
driver.maximize_window()
# Lets open the application ,we want to scrap
driver.get("https://www.okex.com/p2p-markets/ngn/buy-usdt")
driver.implicitly_wait(10)

# driver.find_element(By.XPATH,"//li[contains(@class,'nav-item nav-buy isSub')]").click()
driver.find_element(By.XPATH,"//a[contains(@class,'item item-active')]").click()

advertiser1 = driver.find_elements(By.XPATH,"//tbody[contains(@class,'')]/tr//span[contains(@class,'merchant-name')]") # Advertiser 1
# advertiser2 = driver.find_elements(By.XPATH,"//span[contains(@class,'merchant-link-side')]") # Advertiser 2


available = driver.find_elements(By.XPATH,"//div[contains(@class,'quantity-and-limit')]/div[1]")  # Avalilable
limit = driver.find_elements(By.XPATH,"//div[contains(@class,'quantity-and-limit')]/div[2]")  # Limit
prices = driver.find_elements(By.XPATH,"//span[contains(@class,'price c-buy')]") # Price

payment = driver.find_elements(By.XPATH, "//div[contains(@class, 'okui-popup okui-tooltip okui-tooltip-neutral   c2c-common-icon-tooltip')]")
# //div[contains(@class, 'okui-popup okui-tooltip okui-tooltip-neutral   c2c-common-icon-tooltip')] :--This path contain the symbol
# in the payement section


myadv1 = []
myava = []
mylim = []
myprice = []
mypayment = []

for adv1 in advertiser1:
    a =adv1.text
    b =a.split()
    print(b[0])
    myadv1.append(b[0])


    #print(adv1.text)
print('111111111111111')


for ava in available:
    a1 =ava.text[9:]
    print(a1)
    myava.append(a1)
print('222222222222222')

for lm in limit:
    a2 = lm.text[6:]
    print(a2)
    mylim.append(a2)
print('3333333333333')

for price in prices:
    a3 = price.text
    print(a3)
    myprice.append(a3)
print('44444444444444')

# hover
for i in payment:
    hover = ActionChains(driver).move_to_element(i)
    hover.perform()
    xpath = "//div[contains(@class, 'okui-popup-layer-content')]"  # It contains 'Bank Transfer' path
    data_in_the_bubble = driver.find_element_by_xpath(xpath)
    hover_data = data_in_the_bubble.get_attribute("innerHTML")
    mypayment.append(hover_data)
print('----------------------------')
pay = mypayment[1:]
print(pay)
print('------------------')


finalrecord = zip(myadv1,myava,mylim,myprice,pay)
# for data in list(finalrecord):
#     print(data)

dicts_data = []
for a,b,c,d,e in finalrecord:
                dicts = {}
                dicts['Advertisers'] = a
                dicts['Available'] = b  
                dicts['Limit'] = c
                dicts['Price'] = d
                dicts['Payment'] = e
                
                dicts_data.append(dicts)
print(dicts_data)

driver.implicitly_wait(10)
driver.quit()
