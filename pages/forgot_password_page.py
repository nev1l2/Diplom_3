import allure

from data import Urls
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.URL = Urls.PASSWORD_FORGOT_URL

    @allure.step('Открываем страницу восстановления пароля')
    def open_forgot_password_page(self):
        self.open_url(MainPageLocators.LOADING_ANIMATION,self.URL)

    @allure.step('Вводим E-mail {email}')
    def fill_email_field(self, email):
        self.fill_field(ForgotPasswordPageLocators.EMAIL, email)

    @allure.step('Нажимаем кнопку "Восстановить"')
    def click_button_recovery(self):
        self.click_element(MainPageLocators.LOADING_ANIMATION,ForgotPasswordPageLocators.BUTTON_RECOVERY)
