#Primero se instala datetime con el siguiente comando  "pip install datetime"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

web_element = driver.find_element(By.NAME, 'q')
web_element.send_keys("Selenium Webdriver"+ Keys.ENTER)

time.sleep(30)

