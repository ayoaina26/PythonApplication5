from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

PATH = 'C:\Python27\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://www.youtube.com/')

driver.maximize_window()

time.sleep(10) 

item = driver.find_element_by_css_selector("ytd-masthead div#buttons ytd-button-renderer a")
item.click()

driver.find_element_by_id("identifierId").send_keys("ayoaina26@gmail.com")
driver.find_element_by_id("identifierNext").click()

search = driver.find_element_by_id('search')
search.send_keys('6783089405')
search.send_keys(Keys.RETURN)

time.sleep(300)

driver.quit()
