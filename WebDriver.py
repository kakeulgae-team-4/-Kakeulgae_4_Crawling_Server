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

    def wait_button_and_click(self, xpath: str):
        button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        button.click()

    def job_get_sub_title(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        for i in range(2, 20):
            try:
                # 버튼 요소 선택
                button_xpath = f'/html/body/div[5]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/dl[1]/dd[2]/div[2]/dl[2]/dd/div[1]/ul[2]/li[{i}]/label/span'
                button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, button_xpath)))
                # 버튼 클릭
                button.click()

            except Exception as e:
                print(f"버튼 클릭에 실패했습니다: {e}")

        search_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'dev-btn-search')))
        search_button.click()
        self.body = self.driver.find_element(By.TAG_NAME, 'body')


    def init_order_select(self):
        self.body.send_keys(Keys.END)
        time.sleep(2)
        # 특정 엘리먼트가 나타날 때까지 스크롤 다운
        try:
            xpath = '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[2]/div[5]/div[2]/div[1]/select'
            optional_xpath = '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[2]/div[5]/div[2]/div[1]/select/option[2]'
            self.wait_button_and_click(xpath)
            self.wait_button_and_click(optional_xpath)
            self.page_source = self.driver.page_source
        except Exception as e:
            print("특정 엘리먼트가 발견되지 않았습니다. 스크롤을 내리면서 기다리겠습니다.")


    def get_page_nums(self):
        pass

    def page_num_exists(self):
        pass
