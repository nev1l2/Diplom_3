import allure
import pytest


class TestMainPage:

    @allure.title('Навигация в Конструктор')
    @allure.description('Проверка осуществления перехода по нажатию на «Конструктор»')
    def test_navigate_to_constructor(self, main_page, switch_page):
        main_page.open_main_page()
        switch_page.click_orders_feed_button()
        switch_page.click_constructor_button()

        with allure.step(f'Проверяем переход на URL {main_page.URL}'):
            assert main_page.current_url == main_page.URL

    @allure.title('Навигация в Ленту заказов')
    @allure.description('Проверка осуществления перехода по нажатию на «Лента заказов»')
    def test_navigate_to_order_feed(self, switch_page, main_page, order_feed_page):
        main_page.open_main_page()
        switch_page.click_orders_feed_button()

        with allure.step(f'Проверяем переход на URL {order_feed_page.URL}'):
            assert switch_page.current_url == order_feed_page.URL

    @allure.title('Показ деталей ингредиента')
    @allure.description('Проверка появления поп-апа с деталями при нажатии на ингредиент')
    def test_ingredient_details_popup(self, main_page):
        main_page.open_main_page()
        ingredient_name = main_page.get_ingredient_name_by_index_(0)
        main_page.click_on_ingredient_(0)

        with allure.step(f'Проверяем наличие поп-апа с деталями об ингредиенте «{ingredient_name}»'):
            assert main_page.get_ingredient_name_in_details_window() == ingredient_name

    @allure.title('Закрытие поп-апа')
    @allure.description('Проверка закрытия поп-ап окна по клику на крестик')
    def test_close_popup(self, main_page):
        main_page.open_main_page()
        main_page.click_on_ingredient_(1)
        main_page.click_cross_button_in_popup_window()

        with allure.step(f'Проверяем, что поп-ап с деталями об ингредиенте закрыт'):
            assert not main_page.find_popup_window()

    @allure.title('Увеличение счетчика ингредиентов')
    @allure.description('Проверка увеличения счетчика ингредиентов при добавлении в заказ')
    @pytest.mark.parametrize('ingredient_index, counter_increment', [(0, 2), (2, 1)],
                             ids=['Две булки', 'Один соус'])
    def test_ingredient_counter_increment(self, main_page, ingredient_index, counter_increment):
        main_page.open_main_page()
        initial_counter = main_page.get_ingredients_counter_(ingredient_index)
        main_page.add_ingredient_to_order(ingredient_index)
        updated_counter = main_page.get_ingredients_counter_(ingredient_index)

        with allure.step(f'Проверяем, что счетчик увеличился на {counter_increment}'):
            assert updated_counter == initial_counter + counter_increment

    @allure.title('Оформление заказа для авторизованного пользователя')
    @allure.description('Проверка возможности заполнения заказа авторизованным пользователем')
    def test_place_order_authorized_user(self, login_user, main_page):
        main_page.add_ingredient_to_order(1)
        main_page.add_ingredient_to_order(4)
        main_page.click_place_order_button()

        with allure.step(f'Проверяем, что заказ успешно оформлен'):
            assert main_page.get_order_status() == 'Ваш заказ начали готовить'