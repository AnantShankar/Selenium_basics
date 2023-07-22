# 1st test Case
# 1. open web browser
# 2. open the URL
# 3. enter th username
# 4. enter the password
# 5. click on login
# 6. capture the title of the web page
# 7. verify the title
# 8. close the browse

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#1. first step
serv_obj=Service("C:\drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

#2. secomd step
driver.get("https://bmsitm.gnums.in/Login.aspx")

#3. third step
driver.find_element(By.NAME,"txtUsername").send_keys("anantshankar822@gmail.com")

#4. forth step
driver.find_element(By.NAME,"txtPassword").send_keys("2F2J5!")


#5. Click on login
driver.find_element(By.NAME,"btnLogin").click()


#6. capture the title of the web page,#7. verify the title
act_title=driver.title
exp_title="BMS Institute of Technology & Management"

if act_title==exp_title:
    print("test passed")
else:
    print("test failed")

#8. close the browser
time.sleep(5)