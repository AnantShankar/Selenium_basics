import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

#1. Select specific checkboxes
driver.find_element(By.XPATH,"//*[@id='monday']").click()

#2. select all checkboxes
check=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print("no of checkboxes are:",len(check))

#looping statement to select or unselect all checkboxes
for i in range(len(check)):
    check[i].click()

    #or

for i in check:
    i.click()

#3.select multiple checkboxes
for checkbox in check:
    weekname=checkbox.get_attribute('id')
    if weekname=='tuesday' or weekname=='thursday':
        checkbox.click()

#4. select 2 checkboxes from the last
for i in range(len(check)-2,len(check)):
    check[i].click()

#5. select 2 checkboxes from the beginning
for i in range(len(check)):
    if i<2:
        check[i].click()

#6. unselect all checkboxes
for che in check:
    if che.is_selected():
        che.click()



time.sleep(5)