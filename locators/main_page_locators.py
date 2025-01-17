from selenium.webdriver.common.by import By


class MainPageLocators:

    ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"
    LIST_OF_INGREDIENTS = By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]"
    INGREDIENTS_COUNTERS = By.XPATH, "//*[contains(@class, 'counter_counter__num')]"
    BURGER_CONSTRUCTOR_BASKET = By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]"
    CLOSE_POPUP_WINDOW_BUTTON = By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]//button"
    POPUP_WINDOW = By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]"
    ORDER_NUMBER_IN_POPUP_WINDOW = By.XPATH, "//h2[contains(@class,'title_shadow')]"
    INGREDIENT_NAME_IN_DETAILS_WINDOW = By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]/div/div/p"
    ORDER_STATUS_START_TO_PREPARE = By.XPATH, "//*[contains(@class, 'Modal_modal__text')]/p[1]"
