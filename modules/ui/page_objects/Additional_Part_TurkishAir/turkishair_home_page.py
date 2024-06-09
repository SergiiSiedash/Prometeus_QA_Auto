from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class TurkishAir(BasePage):
    URL = "https://www.turkishairlines.com/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(TurkishAir.URL)

    def try_to_search_flight(self,arrival, destenation):
        insert_arrival = self.driver.find_element(By.ID, "#fromPort")

        arrival_elem.send_keys(arrival)

        # Знаходимо поле, в яке будемо вводити неправильний пароль
        isert_destenation = self.driver.find_element(By.ID, "#toPort")

        # вводимо неправильний пароль
        destenation_elem.send_keys(destenation)
        
        # Знаходимо кнопку sign in
        btn_elem = self.driver.find_element(By.NAME, "hm__style_thy-button__qr6mU hm__RoundAndOneWayTab_searchButton__vpLcA")

        # емулюємо клік лівою кнопкою миші
        btn_elem.click()

    # def check_title(self, expected_title):
    #     return self.driver.title == expected_title
