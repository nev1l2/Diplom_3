import allure

from data import Urls
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.URL = Urls.ACCOUNT_URL

    @allure.step('Дожидаемся полной загрузки страницы')
    def wait_loading_page(self):
        self.wait_visibility(AccountPageLocators.ORDERS_HISTORY_MENU)

    @allure.step('Нажимаем на ссылку "История заказов"')
    def click_link_order_history(self):
        self.click_element(AccountPageLocators.ORDERS_HISTORY_MENU)

    @allure.step("Нажимаем на кнопку 'Выход'")
    def click_button_exit(self):
        self.click_element(AccountPageLocators.EXIT_BUTTON)