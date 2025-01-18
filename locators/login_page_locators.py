from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_INPUT = By.NAME, "name"
    PASSWORD_INPUT = By.NAME, "Пароль"
    BUTTON_LOGIN = By.XPATH, "//*[text()='Войти']"

    PASS_RECOVERY_LINK = By.LINK_TEXT, 'Восстановить пароль'

    EYE_INPUT_ICON = By.XPATH, "//*[contains(@class, 'input__icon')]"