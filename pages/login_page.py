import allure

from data import Urls
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.URL = Urls.LOGIN_URL

    @allure.step('Открываем страницу авторизации')
    def open_login_page(self):
        self.open_url(MainPageLocators.LOADING_ANIMATION, Urls.LOGIN_URL)

    @allure.step('Дожидаемся полной загрузки страницы')
    def wait_loading_page(self):
        self.wait_visibility(LoginPageLocators.BUTTON_LOGIN)

    @property
    def get_password_field(self):
        return self.get_visible_element(ResetPasswordPageLocators.INACTIVE_PASSWORD_FIELD)

    @allure.step('Клик на иконку показа пароля')
    def click_icon_in_field_password(self):
        self.click_element(MainPageLocators.LOADING_ANIMATION,LoginPageLocators.EYE_INPUT_ICON)

    @allure.step('Нажимаем на ссылку "Восстановить пароль"')
    def click_link_recovery_password(self):
        self.click_element(MainPageLocators.LOADING_ANIMATION, LoginPageLocators.PASS_RECOVERY_LINK)

    @allure.step('Заполняем поле E-mail {email}')
    def fill_email_field(self, email):
        self.fill_field(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step('Заполняем поле Password {password}')
    def fill_password_field(self, password):
        self.fill_field(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_button_enter(self):
        self.click_element(MainPageLocators.LOADING_ANIMATION, LoginPageLocators.BUTTON_LOGIN)

    @allure.step('Логинимся')
    def logining_user(self, login_details):
        self.fill_email_field(login_details['email'])
        self.fill_password_field(login_details['password'])
        self.click_button_enter()

