import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\drivers\chromedriver_win32 (3)\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

#driver.get("https://demo.nopcommerce.com/")
#driver.maximize_window()

#1.search by using ID's locator
#driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

#1.search by using NAME locator
#driver.find_element(By.NAME,"q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

#3*.a.Link Text
#Register
#driver.find_element(By.LINK_TEXT,"Register").click()
#3*.b.LogIn
#driver.find_element(By.LINK_TEXT,"Log in").click()

#3.Partial Link Text
#driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()

#4.ClassName
#driver.get("https://www.amazon.in")
#driver.maximize_window()

#find all the anchor tag
#links=driver.find_elements(By.TAG_NAME, "a")
#print("The number of links are",len(links))

driver.get("https://www.facebook.com/")
driver.maximize_window()


#5.css locator
#5.a.tag(optional) and id
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("sathwikps16@gmail.com")
#driver.find_element(By.CSS_SELECTOR,"#email").send_keys("xyz123@gmail.com")

#5.b.tag(opt) and class
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc1234@gmail.com")
#driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc1234@gmail.com")

#5.c.tag(opt and attribute
#driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("abc1234@gmail.com")
driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("abc1234@gmail.com")

#5.d.tag,class and attributes
driver.find_element(By.CSS_SELECTOR,"input.inputtext[placeholder=Password]").send_keys("abcd1234")

time.sleep(4)