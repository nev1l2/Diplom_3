import allure

from data import Urls
from locators.history_orders_page_locators import HistoryOrdersPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class OrderHistoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.URL = Urls.HISTORY_ORDERS_URL

    @allure.step('Открываем страницу истории заказов пользователя {self.URL}')
    def open_order_history_page(self):
        self.open_url(MainPageLocators.LOADING_ANIMATION, self.URL)

    @allure.step('Получаем номера заказов пользователя из Истории заказов')
    def get_order_numbers(self):
        order_numbers = list(order_number.text for order_number in self.get_visible_elements(
            HistoryOrdersPageLocators.ORDER_NUMBERS))
        return order_numbers