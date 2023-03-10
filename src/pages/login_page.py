from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class LoginPage(BasePage):
    def go_to(self):
        self.driver.get(self.configs.base_url())
        return self

    def enter_username(self, username: str):
        username_input = self.driver.find_element(By.ID, 'id_username')
        username_input.clear()
        username_input.send_keys(username)
        return self

    def enter_password(self, password: str):
        password_input = self.driver.find_element(By.ID, 'id_password')
        password_input.clear()
        password_input.send_keys(password)
        return self

    def click_login(self):
        self.driver.find_element(By.ID, 'submit-button').click()

    def get_error_message(self):
        return self.driver.find_element(By.XPATH, "//*[starts-with(@class, 'alert')]/div").text
