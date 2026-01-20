class DarazSmartWatchFinder:
    import time
    import validators
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    
    driver = None
    _url = None
    current_page = 1
    total_pages = 1

    def __init__(self, url):
        #check if url is valid structure
        if not self.validators.url(url):
            raise ValueError("Invalid URL structure")
        self.driver = self.initialize_driver(url)
        self._url = url
        self.current_page = 1
        if self.GetSearchResultPageCount() > 0:
            self.total_pages = self.GetSearchResultPageCount()

    def GetPageCount(self):
        return self.total_pages


    def get_product_divs(self):
        product_item_divs = self.driver.find_elements(self.By.XPATH, '//div[@data-qa-locator="product-item"]')
        return product_item_divs

    def write_product_urls_to_file(self, product_item_divs):
        for div in product_item_divs:
            anchor_element = div.find_element(self.By.TAG_NAME, 'a')
            product_url = anchor_element.get_attribute('href')
            # write to file
            with open('daraz_smart_watches_urls.txt', 'a') as f:
                f.write(product_url + '\n')

        self.driver.quit()

    def initialize_driver(self, url):
        self.driver = self.webdriver.Chrome(service=self.Service(self.ChromeDriverManager().install()))
        self.driver.get(url)
        self.time.sleep(5)
        return self.driver

    def GetSearchResultPageCount(self):
        elements = self.driver.find_elements(
            self.By.CSS_SELECTOR,
            "li.ant-pagination-item a"
        )
        pages = [
            int(el.text)
            for el in elements
            if el.text.isdigit()
        ]
        max_page = max(pages)
        return max_page
