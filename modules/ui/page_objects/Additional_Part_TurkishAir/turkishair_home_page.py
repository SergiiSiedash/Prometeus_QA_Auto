from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


# Init subclass TurkishAir
class TurkishAir(BasePage):
    URL = "https://www.turkishairlines.com/"

    def __init__(self) -> None:
        super().__init__()

    # Method to open Turkish Airlines main page
    def go_to(self):
        self.driver.get(TurkishAir.URL)

    # Method to find flight
    def try_to_search_flight(self, arrival, destenation):
        # Find insert field and insert airport of departure
        arrival_elem = self.driver.find_element(By, ID = "#fromPort")
        arrival_elem.send_keys(arrival)

        # Find insert field and insert airport of arrival
        destenation_elem = self.driver.find_element(By.CSS_SELECTOR, "#toPort")
        destenation_elem.send_keys(destenation)

        # Find "search" button
        btn_elem = self.driver.find_element(
            By.XPATH,
            "/html/body/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/button/svg/path",
        )

        # Push "search" button
        btn_elem.click()

    # Method to find alert box
    def check_alert_box(self):
        # Getting alert-box element
        alert_elem = self.driver.find_element(
            By.CSS_SELECTOR,
            "body > div.hm__style_thy-modal-background__GgsUv.hm__style_error-modal__bF3yH > div > div > div.hm__style_error-modal-header__uklc1.hm__grid_row__uBL8m > div.hm__style_title__MRCSZ.hm__grid_col-lg-11__jxHOm",
        )
        alert_text = alert_elem.text
        return alert_text
