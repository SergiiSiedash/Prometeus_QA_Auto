from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )

    def close(self):
        self.driver.close()
