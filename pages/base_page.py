from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop

from data import SET_TIMEOUT, LOADING_ANIMATION


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def current_url(self):
        return self.driver.current_url

    def wait_loading(self, timeout=SET_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(expected_conditions.invisibility_of_element(LOADING_ANIMATION))

    def open_url(self, url):
        self.driver.get(url)
        self.wait_loading()

    def click_element(self, locator, timeout=SET_TIMEOUT):
        self.wait_loading()
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator)).click()

    def fill_field(self, locator, text, timeout=SET_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator)).send_keys(text)

    def wait_visibility(self, locator, timeout=SET_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def get_attribute(self, locator, attribute, timeout=SET_TIMEOUT):
        return (WebDriverWait(self.driver, timeout).
                until(expected_conditions.visibility_of_element_located(locator)).get_attribute(attribute))

    def is_element_exist(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        finally:
            return False

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def get_visible_element(self, locator, timeout=SET_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until((expected_conditions.visibility_of_element_located(locator)))

    def get_visible_elements(self, locator, timeout=SET_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until((expected_conditions.visibility_of_all_elements_located(locator)))

    def drag_and_drop(self, source_drag, target_drop):
        drag_and_drop(self.driver, source_drag, target_drop)