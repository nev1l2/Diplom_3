from selenium.webdriver.common.by import By


class AccountPageLocators:
    ORDERS_HISTORY_MENU = By.LINK_TEXT, "История заказов"
    EXIT_BUTTON = By.XPATH, "//*[text()='Выход']"
