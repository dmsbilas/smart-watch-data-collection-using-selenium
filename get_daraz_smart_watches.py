import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

page=1
max_page=5

driver.get("https://www.daraz.com.bd/catalog/?q=smart%20watch")

daraz_url = "https://www.daraz.com.bd/catalog/?q=smart%20watch"+"&page=" + str(page)

time.sleep(5)

# write method

def GetProductUrlsAndWriteToFile():
    while page <= max_page:
        divs = GetProductUrlsFromPage()
        GoToNextPage()
        page += 1

    divs = driver.find_elements(By.XPATH, '//div[@data-qa-locator="product-item"]')
    for div in divs:
        anchor_element = div.find_element(By.TAG_NAME, 'a')
        product_url = anchor_element.get_attribute('href')
        # write to file
        with open('daraz_smart_watches_urls.txt', 'a') as f:
            f.write(product_url + '\n')
    return divs

def GoToNextPage():
    driver.find_element(By.XPATH, '//a[@data-qa-locator="pagination-next"]').click()
    time.sleep(5)


# Get all page count


# Go go next page 
driver.find_element(By.XPATH, '//a[@data-qa-locator="pagination-next"]').click()
driver.find_element(By.XPATH,) '//a[@data-qa-locator="pagination-next"]').click()

time.sleep(5)
driver.quit()