import allure

from data import Urls
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.URL = Urls.BASE_URL

    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        self.open_url(MainPageLocators.LOADING_ANIMATION, Urls.BASE_URL)
        self.wait_visibility(MainPageLocators.LIST_OF_INGREDIENTS)

    @allure.step('Выбираем ингредиент')
    def click_on_ingredient_(self, index):
        ingredients = self.get_visible_elements(MainPageLocators.LIST_OF_INGREDIENTS)
        ingredients[index].click()

    @allure.step('Закрываем всплывающее окно')
    def click_cross_button_in_popup_window(self):
        self.click_element(MainPageLocators.LOADING_ANIMATION, MainPageLocators.CLOSE_POPUP_WINDOW_BUTTON)

    @allure.step('Добавляем ингредиент в заказ')
    def add_ingredient_to_order(self, index):
        ingredients = self.get_visible_elements(MainPageLocators.LIST_OF_INGREDIENTS)
        basket = self.get_visible_element(MainPageLocators.BURGER_CONSTRUCTOR_BASKET)
        self.drag_and_drop(ingredients[index], basket)

    @allure.step('Кликаем на кнопку оформления заказа')
    def click_place_order_button(self):
        self.click_element(MainPageLocators.LOADING_ANIMATION, MainPageLocators.ORDER_BUTTON)

    @allure.step('Получаем название ингредиента')
    def get_ingredient_name_by_index_(self, index):
        ingredients = self.get_visible_elements(MainPageLocators.LIST_OF_INGREDIENTS)
        return ingredients[index].text.split('\n')[2]

    @allure.step('Получаем название ингредиента в окне с деталями')
    def get_ingredient_name_in_details_window(self):
        return self.get_visible_element(MainPageLocators.INGREDIENT_NAME_IN_DETAILS_WINDOW).text

    @allure.step('Получаем текст из окна подтверждения заказа')
    def get_order_status(self):
        return self.get_visible_element(MainPageLocators.ORDER_STATUS_START_TO_PREPARE).text

    @allure.step('Получаем номер заказа из окна подтверждения заказа')
    def get_order_number_from_confirm_popup(self):
        return f'0{self.find_element(MainPageLocators.ORDER_NUMBER_IN_POPUP_WINDOW).text}'

    @allure.step('Получаем всплывающее окно с деталями ингредиента')
    def get_popup_details_window(self):
        return self.get_visible_element(MainPageLocators.POPUP_WINDOW)

    @allure.step('Проверяем наличие всплывающего окна с деталями ингредиента')
    def find_popup_window(self):
        return self.is_element_exist(MainPageLocators.POPUP_WINDOW)

    @allure.step('Получаем значение счетчика ингредиента')
    def get_ingredients_counter_(self, index):
        counters = self.get_visible_elements(MainPageLocators.INGREDIENTS_COUNTERS)
        return int(counters[index].text)

    @allure.step('Создаем заказ и получаем его номер')
    def add_order(self, login_user):
        self.add_ingredient_to_order(0)
        self.add_ingredient_to_order(3)
        self.click_place_order_button()
        self.wait_loading(MainPageLocators.LOADING_ANIMATION)
        order_number = self.get_order_number_from_confirm_popup()
        self.click_cross_button_in_popup_window()

        return order_number