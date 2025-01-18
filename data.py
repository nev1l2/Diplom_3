from selenium.webdriver.common.by import By


class Browsers:
    Firefox = 'Firefox'
    Chrome = 'Chrome'

class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'
    LOGIN_URL = f'{BASE_URL}login'
    PASSWORD_FORGOT_URL = f'{BASE_URL}forgot-password'
    PASSWORD_RESET_URL = f'{BASE_URL}reset-password'
    ACCOUNT_URL = f'{BASE_URL}account/profile'
    HISTORY_ORDERS_URL = f'{BASE_URL}account/order-history'
    FEED_URL = f'{BASE_URL}feed'

    USER_create = f'{BASE_URL}api/auth/register'
    USER_authorization = f'{BASE_URL}api/auth/create_user'
    USER_delete = f'{BASE_URL}api/auth/user'

SET_TIMEOUT = 10