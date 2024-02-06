from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver


class WebDriver:
    """
    페이지만 크롤링함
    파싱은 하지 않음
    """

    def __init__(self, headless: bool = True, no_sandbox: bool = True):
        self.page_source = None
        chrome_options = Options()
        if headless:
            chrome_options.add_argument('--headless')
        if no_sandbox:
            chrome_options.add_argument('--no-sandbox')
        chrome_options.add_experimental_option('detach', True)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

        self.driver = webdriver.Chrome(options=chrome_options)
        handles = self.driver.window_handles
        for handle in handles:
            if handle != handles[0]:
                self.driver.switch_to.window(handle)
                self.driver.close()
        self.driver.switch_to.window(handles[0])

    def open_url(self, url: str):
        self.driver.get(url)
        self.page_source = self.driver.page_source

    def get_page_source(self):
        return self.page_source

    def save_page_source(self, path: str):
        with open(path, 'w') as file:
            for line in self.page_source:
                file.write(line)
        print('page source saved')

    def close_url(self):
        self.driver.quit()

    def get_elements_by_xpath(self, xpath: str):
        return self.driver.find_elements(By.XPATH, xpath)

    def get_elements_by_class(self, _class: str):
        return self.driver.find_elements(By.CLASS_NAME, _class)

    def get_element_by_class(self, _class: str):
        return self.driver.find_element(By.CLASS_NAME, _class)

    def get_elements_by_name(self, _class: str):
        return self.driver.find_elements(By.NAME, _class)

    def get_element_by_name(self, _class: str):
        return self.driver.find_element(By.NAME, _class)
