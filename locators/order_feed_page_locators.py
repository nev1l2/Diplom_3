from selenium.webdriver.common.by import By


class OrdersFeedPageLocators:

    ORDERS_LIST = By.XPATH, "//*[contains(@class, 'OrderHistory_listItem')]"
    ORDERS_NUMBERS_LIST = By.XPATH, "//*[contains(text(), '#')]"
    ORDERS_IN_PROGRESS_LIST = By.XPATH, "//*[contains(@class, '_orderListReady')]/li[contains(@class, 'digits')]"
    ORDER_NUMBER_IN_POPUP = By.XPATH, "//*[contains(@class, 'Modal_orderBox')]/p[1]"
    COUNTER_COMPLETED_FOR_ALL_TIME = By.XPATH, "//*[text()='Выполнено за все время:']/parent::div/p[2]"
    COUNTER_COMPLETED_FOR_TODAY = By.XPATH, "//*[text()='Выполнено за сегодня:']/parent::div/p[2]"