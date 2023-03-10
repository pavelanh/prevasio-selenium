from src.helper.csv_parser import parse
from src.pages.login_page import LoginPage
from src.pages.main_page import MainPage
from tests.base_test import BaseTest


class LoginTest(BaseTest):
    def initialize(self):
        self.login_page: LoginPage = LoginPage(self.driver, self.configs)
        self.main_page: MainPage = MainPage(self.driver, self.configs)
        self.test_data = parse('tests/test_data/login.csv')

    def test_correct_username_and_correct_password(self):
        data = [row for row in self.test_data if row['Test Case ID'] == 'TC-1']
        for d in data:
            self.login_page.go_to().enter_username(d['User Name']).enter_password(d['Password']).click_login()
            self.assertEqual(self.main_page.get_username(), 'test.username')

    def test_incorrect_username_and_correct_password(self):
        data = [row for row in self.test_data if row['Test Case ID'] == 'TC-2']
        for d in data:
            self.login_page.go_to().enter_username(d['User Name']).enter_password(d['Password']).click_login()
            self.assertEqual(self.login_page.get_error_message(), d['Error Message'])

    def test_correct_username_and_incorrect_password(self):
        data = [row for row in self.test_data if row['Test Case ID'] == 'TC-3']
        for d in data:
            self.login_page.go_to().enter_username(d['User Name']).enter_password(d['Password']).click_login()
            self.assertEqual(self.login_page.get_error_message(), d['Error Message'])

    def test_incorrect_username_and_incorrect_password(self):
        data = [row for row in self.test_data if row['Test Case ID'] == 'TC-4']
        for d in data:
            self.login_page.go_to().enter_username(d['User Name']).enter_password(d['Password']).click_login()
            self.assertEqual(self.login_page.get_error_message(), d['Error Message'])

    def test_blank_username(self):
        data = [row for row in self.test_data if row['Test Case ID'] == 'TC-5']
        for d in data:
            self.login_page.go_to().enter_username(d['User Name']).enter_password(d['Password']).click_login()
            self.assertEqual(self.login_page.get_error_message(), d['Error Message'])

    def test_blank_password(self):
        data = [row for row in self.test_data if row['Test Case ID'] == 'TC-6']
        for d in data:
            self.login_page.go_to().enter_username(d['User Name']).enter_password(d['Password']).click_login()
            self.assertEqual(self.login_page.get_error_message(), d['Error Message'])
