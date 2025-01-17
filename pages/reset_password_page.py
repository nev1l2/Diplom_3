import allure

from data import Urls
from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.URL = Urls.PASSWORD_RESET_URL

    def get_password_field(self):
        return self.get_visible_element(ResetPasswordPageLocators.INACTIVE_PASSWORD_FIELD)

    @allure.step('Дожидаемся загрузки страницы')
    def wait_load_page(self):
        self.wait_visibility(ResetPasswordPageLocators.EYE_INPUT_ICON)

    @allure.step('Клик на иконку показа пароля')
    def click_icon_in_field_password(self):
        self.click_element(ResetPasswordPageLocators.EYE_INPUT_ICON)