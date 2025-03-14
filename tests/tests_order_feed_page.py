import allure

from pages.main_page import MainPage

class TestOrderFeedPage:

    @allure.title('Просмотр информации о заказе')
    @allure.description('Проверка функционала открытия попапа с информацией при нажатии на заказ')
    def test_order_details_popup(self, order_feed_page):
        order_index = 0
        order_feed_page.open_order_feed_page()
        order_number = order_feed_page.get_order_number_by_index(order_index)
        order_feed_page.click_orders_by_index_(order_index)
        with allure.step('Проверяем открытие попапа заказа'):
            assert order_feed_page.get_order_number_in_popup_window() == order_number

    @allure.title('Показ заказов клиента')
    @allure.description(
        'Проверка наличия заказов клиента из раздела «История заказов» на странице «Лента заказов»')
    def test_user_orders_display(self, login_user, create_order, switch_page,
                                 account_page, order_feed_page, orders_history_page):
        switch_page.click_account_button()
        account_page.click_link_order_history()
        client_orders = orders_history_page.get_order_numbers()
        order_feed_page.open_order_feed_page()
        with allure.step('Проверяем наличие заказов в «Лента заказов»'):
            assert order_feed_page.are_all_orders_present(client_orders)

    @allure.title('Увеличение счетчика «Завершено за все время»')
    @allure.description('Проверка увеличения счетчика «Завершено за все время» при создании нового заказа')
    def test_total_orders_counter_increment(self, switch_page, order_feed_page, main_page, login_user):
        switch_page.click_orders_feed_button()
        initial_counter = order_feed_page.get_count_completed_orders_for_all_time()
        switch_page.click_constructor_button()
        MainPage.add_order(main_page, login_user)
        switch_page.click_orders_feed_button()
        with allure.step('Проверяем увеличение счетчика «Завершено за все время»'):
            assert order_feed_page.get_count_completed_orders_for_all_time() > initial_counter

    @allure.title('Увеличение счетчика «Завершено за сегодня»')
    @allure.description('Проверка увеличения счетчика «Завершено за сегодня» при создании нового заказа')
    def test_today_orders_counter_increment(self, switch_page, main_page, order_feed_page, login_user):
        switch_page.click_orders_feed_button()
        initial_counter = order_feed_page.get_count_completed_orders_for_today()
        switch_page.click_constructor_button()
        MainPage.add_order(main_page, login_user)
        switch_page.click_orders_feed_button()
        with allure.step('Проверяем увеличение счетчика «Завершено за сегодня»'):
            assert order_feed_page.get_count_completed_orders_for_today() > initial_counter

    @allure.title('Появление номера заказа в «В процессе»')
    @allure.description('Проверка отображения номера заказа в «В процессе» после оформления заказа')
    def test_order_number_in_progress(self, login_user, switch_page, main_page, order_feed_page):
        new_order_number = MainPage.add_order(main_page, login_user)
        switch_page.click_orders_feed_button()
        order_feed_page.wait_load_page()
        orders_in_progress = order_feed_page.get_orders_number_in_progress()

        with allure.step(f'Проверяем наличие номер нового заказа - {new_order_number} в «В процессе»'):
            assert new_order_number in orders_in_progress