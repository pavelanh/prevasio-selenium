from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class MainPage(BasePage):
    def get_username(self) -> str:
        return self.driver.find_element(By.XPATH, "//*[@class='nav-link dropdown-toggle']/*[contains(@class,'icon-user')]/..").text
