from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = 'C:\Python27\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('http://president.md/')

driver.maximize_window()

search = driver.find_element_by_name('keywords')
search.send_keys('Dodon')
search.send_keys(Keys.RETURN)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

click = driver.find_element_by_link_text('PRESA')
click.click()

time.sleep(300)

driver.quit()
