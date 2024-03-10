from web_driver import WebDriver
from selenium import webdriver


class SaraminWebDriver(WebDriver):
    def __init__(self):
        super(SaraminWebDriver, self).__init__()
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'

        self.chrome_options.add_argument(f'user-agent={user_agent}')
        self.driver = webdriver.Chrome(options=self.chrome_options)

