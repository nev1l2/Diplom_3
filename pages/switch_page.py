import allure

from locators.switch_page_locators import SwitchPageLocators
from pages.base_page import BasePage


class SwitchPage(BasePage):

    @allure.step('Кликаем на кнопку «Конструктор»')
    def click_constructor_button(self):
        self.click_element(SwitchPageLocators.CONSTRUCTOR_PAGE_BUTTON)

    @allure.step('Кликаем на кнопку «Лента Заказов»')
    def click_orders_feed_button(self):
        self.click_element(SwitchPageLocators.ORDERS_FEED_PAGE_BUTTON)

    @allure.step('Кликаем на ссылку «Личный кабинет»')
    def click_account_button(self):
        self.click_element(SwitchPageLocators.ACCOUNT_PAGE_BUTTON)