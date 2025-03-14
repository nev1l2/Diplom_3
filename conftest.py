import allure
import pytest
import requests

from faker import Faker
from selenium import webdriver
from data import Urls, Browsers
from pages.account_page import AccountPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.history_orders_page import OrderHistoryPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.reset_password_page import ResetPasswordPage
from pages.switch_page import SwitchPage


@pytest.fixture(params=[Browsers.Firefox, Browsers.Chrome])
def driver(request):
    with allure.step(f'Запускаем браузер {request.param}'):
        if request.param == Browsers.Firefox:
            driver = webdriver.Firefox()
        elif request.param == Browsers.Chrome:
            driver = webdriver.Chrome()
        driver.get(Urls.BASE_URL)

    yield driver
    driver.quit()

@pytest.fixture()
def user_create():
    fake = Faker()
    user_data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.user_name()
    }
    response = requests.post(Urls.USER_create, json=user_data)
    access_token = response.json()['accessToken']
    del user_data['name']
    yield user_data
    headers = {'Authorization': access_token}
    requests.delete(Urls.USER_delete, headers=headers)

@allure.title('Авторизация тестового пользователя')
@pytest.fixture()
def login_user(login_page, user_create):
    login_page.open_login_page()
    login_page.logining_user(user_create)

@allure.title('Формирование заказа')
@pytest.fixture()
def create_order(main_page):
    main_page.add_ingredient_to_order(1)
    main_page.add_ingredient_to_order(4)
    main_page.click_place_order_button()
    main_page.click_cross_button_in_popup_window()

@pytest.fixture()
def main_page(driver):
    return MainPage(driver)

@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture()
def forgot_password_page(driver):
    return ForgotPasswordPage(driver)

@pytest.fixture()
def reset_password_page(driver):
    return ResetPasswordPage(driver)

@pytest.fixture()
def order_feed_page(driver):
    return OrderFeedPage(driver)

@pytest.fixture()
def account_page(driver):
    return AccountPage(driver)

@pytest.fixture()
def orders_history_page(driver):
    return OrderHistoryPage(driver)

@pytest.fixture()
def switch_page(driver):
    return SwitchPage(driver)