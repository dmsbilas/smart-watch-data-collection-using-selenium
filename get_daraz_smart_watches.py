import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.daraz.com.bd/catalog/?q=smart%20watch")

time.sleep(5)

divs = driver.find_elements(By.XPATH, '//div[@data-qa-locator="product-item"]')

i = 0 
for div in divs:
    anchor_element = div.find_element(By.TAG_NAME, 'a')
    product_url = anchor_element.get_attribute('href')
    

time.sleep(5)
driver.quit()