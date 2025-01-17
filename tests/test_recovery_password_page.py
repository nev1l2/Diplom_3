import allure


class TestPasswordRecoveryPage:

    @allure.title('Навигация на страницу восстановления пароля')
    @allure.description('Проверка навигации на страницу восстановления пароля через кнопку «Восстановить пароль»')
    def test_navigate_to_password_recovery_page(self, driver, login_page, forgot_password_page):
        login_page.open_login_page()
        login_page.click_link_recovery_password()
        with allure.step(f'Верификация перехода на url {forgot_password_page.URL}'):

            assert driver.current_url == forgot_password_page.URL

    @allure.title('Восстановление пароля с использованием электронной почты')
    @allure.description('Проверка ввода электронной почты и нажатия кнопки «Восстановить»')
    def test_recover_password_with_email(self, driver, forgot_password_page, reset_password_page, user_create):
        forgot_password_page.open_forgot_password_page()
        forgot_password_page.fill_email_field(user_create['email'])
        forgot_password_page.click_button_recovery()
        reset_password_page.wait_load_page()
        with allure.step(f'Верификация перехода на url {reset_password_page.URL}'):

            assert driver.current_url == reset_password_page.URL

    @allure.title('Активация поля для пароля при нажатии кнопки показать/скрыть')
    @allure.description('Проверка, что нажатие кнопки показать/скрыть пароль делает поле активным')
    def test_password_field_activation(self, forgot_password_page, reset_password_page, user_create):
        forgot_password_page.open_forgot_password_page()
        forgot_password_page.fill_email_field(user_create['email'])
        forgot_password_page.click_button_recovery()
        border = reset_password_page.get_password_field()
        reset_password_page.click_icon_in_field_password()
        with allure.step(f'Проверка активности поля с паролем'):

            assert 'input_status_active' in border.get_attribute('class')