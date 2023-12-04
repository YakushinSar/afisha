from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class BasePage():
    TIMEOUT = 10

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def is_visible(self, locator: tuple, timeout: int = TIMEOUT) -> WebElement:
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def is_clickable(self, locator: tuple, timeout: int = TIMEOUT) -> WebElement:
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
