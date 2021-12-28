from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import openpyxl  # for read and write excel sheet

# Sending an email with the data
import smtplib
from email.message import EmailMessage

driver = webdriver.Chrome(ChromeDriverManager().install()) # Here I am using chrome
# Lets maximize 
driver.maximize_window()
# Lets open the application ,we want to scrap
driver.get("https://www.amazon.in/")
# Wait for the particular time 
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[contains(@id,'search')]").send_keys("Samsung phones")
driver.find_element(By.XPATH,"//input[@value='Go']").click()
driver.find_element(By.XPATH,"//span[text()='Samsung']").click() # click on samsung check-box
# phonenames store the list of web elements:
phonenames = driver.find_elements(By.XPATH,"//span[contains(@class,' a-color-base a-text-normal')]")
# prices store the list of prices:
prices = driver.find_elements(By.XPATH,"//span[contains(@class,'price-whole')]")

myphone = []
myprice = []

for phone in phonenames:
    # print(phone.text)
    myphone.append(phone.text)

print("*"*50)

for price in prices:
    # print(price.text)
    myprice.append(price.text)

finallist = zip(myphone,myprice)
# print(list(finallist))
print('********************')

# for data in list(finallist):
#     print(data)

print('part 1')
# Lets store the data in excel sheet:
wb = openpyxl.Workbook()
wb['Sheet'].title = 'Amazone Samsung data'
sheet1 = wb.active

sheet1.append(['Name','Price']) # Add column name
for x in list(finallist):
    sheet1.append(x)

wb.save("FinalRecords.xlsx")

print('part 2')

print('**************Email******************')

msg =  EmailMessage()
msg['Subject'] = 'Samsung Phone data'
msg['From'] = 'DS'
msg['To'] = 'sonidhruvil708@gmail.com'

with open('EmailTemplate.text') as myfile:
    data = myfile.read()
    msg.set_content(data)

with open("FinalRecords.xlsx","rb") as f:
        file_data = f.read()
        print("File data in binary ",file_data)
        file_name = f.name
        print("File name is ",f.name)
        msg.add_attachment(file_data,maintype ='appllication',subtype = 'xlsx',filename = file_name)


# NOTE : For sending an email you have to do these things :
#   Log in to your Google account, and use these links:
#   Step 1 [Link of Disabling 2-step verification]:
#         https://myaccount.google.com/security?utm_source=OGB&utm_medium=act#signin
#   Step 2: [Link for Allowing less secure apps]:
#         https://myaccount.google.com/u/1/lesssecureapps?pli=1&pageId=none


with smtplib.SMTP_SSL('smtp.gmail.com',465) as server :
    #server.login("EmailId","Password")
    server.login("   ","   ")
    server.send_message(msg)

print("Email Sent!!!")

#driver.quit()