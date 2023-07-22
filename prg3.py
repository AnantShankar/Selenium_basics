import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.amazon.in/")
driver.maximize_window()

#1. absolute xpath
driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input").send_keys("t-shirts")
driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input").click()

#2
driver.find_element(By.XPATH,"//*[@id='twotabsearchtextbox']").send_keys("t-shirt")
driver.find_element(By.XPATH,"//*[@id='nav-search-submit-button']").click()

#3. or & and
driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox' or @name='field-keywords']").send_keys("t-shirts")
driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox' and @class='nav-input nav-progressive-attribute']").send_keys("t-shirts")
driver.find_element(By.XPATH,"//*[@id='nav-search-submit-button']").click()

#contains() amd starts-with()
driver.find_element(By.XPATH,"//input[contains(@id,'twotab')]").send_keys("t-shirt")


#rediff
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

txt_msg=driver.find_element(By.XPATH,"//a[contains(text(),'NTPC')]").text
print(txt_msg)

#self
txt_msg=driver.find_element(By.XPATH,"//a[contains(text(),'NTPC')]/self::a").text
print(txt_msg)

#parent
txt_msg=driver.find_element(By.XPATH,"//a[contains(text(),'NTPC')]/parent::td").text
print(txt_msg)

#child
child=driver.find_elements(By.XPATH,"//a[contains(text(),'NTPC')]/ancestor::tr/child::td")
print(len(child))

#ancestor
ans=driver.find_element(By.XPATH,"//a[contains(text(),'NTPC')]/ancestor::tr").text
print(ans)

#desendents
des=driver.find_elements(By.XPATH,"//a[contains(text(),'NTPC')]/ancestor::tr/descendant::*")
print("no of descendant are:",len(des))

#following
des=driver.find_elements(By.XPATH,"//a[contains(text(),'NTPC')]/ancestor::tr/following::*")
print("no of followings are:",len(des))

#following-sibling
fol=driver.find_elements(By.XPATH,"//a[contains(text(),'NTPC')]/ancestor::tr/following-sibling::*")
print("no od followings are:",len(fol))

#preceding
pes=driver.find_elements(By.XPATH,"//a[contains(text(),'NTPC')]/ancestor::tr/preceding::*")
print("no od followings are:",len(pes))

#preceding-siblings
pes_s=driver.find_elements(By.XPATH,"//a[contains(text(),'NTPC')]/ancestor::tr/preceding-sibling::*")
print("no od followings are:",len(pes_s))


time.sleep(3)