import allure


class TestAccountPage:

    @allure.title('Переход в личный кабинет')
    @allure.description('Проверка перехода при клике на «Личный кабинет»')
    def test_navigate_to_personal_account(self, driver, login_user, switch_page, account_page):
        switch_page.click_account_button()
        account_page.wait_loading_page()
        with allure.step(f'Верификация перехода на url {driver.current_url}'):

            assert driver.current_url == account_page.URL

    @allure.title('Переход в раздел «История заказов»')
    @allure.description('Проверка перехода в раздел «История заказов»')
    def test_navigate_to_order_history(self, driver, login_user, switch_page, account_page, orders_history_page):
        switch_page.click_account_button()
        account_page.click_link_order_history()
        with allure.step(f'Верификация перехода на url {driver.current_url}'):

            assert driver.current_url == orders_history_page.URL

    @allure.title('Выход из аккаунта')
    @allure.description('Проверка процедуры выхода из аккаунта')
    def test_logout(self, driver, login_user, login_page, switch_page, account_page):
        switch_page.click_account_button()
        account_page.click_button_exit()
        login_page.wait_loading_page()
        with allure.step(f'Верификация перехода на url {driver.current_url}'):

            assert driver.current_url == login_page.URL