from pages.home_page import HomePage
from pages.home_page_url import *
from selenium.webdriver.support import expected_conditions as EC
import time


class TestHeader():
    def test_afisha_logo_visible(self, driver):
        page = HomePage(driver, url=HOME_PAGE_URL)
        page.open()
        assert page.header(), 'текст не видимый'

    def test_about_text_clickable(self, driver, wait):
        page = HomePage(driver, url=HOME_PAGE_URL)
        page.open()
        assert page.about().text == 'Об Афише', 'текст не соответствует'
        assert page.about().is_enabled(), 'не кликабельный'
        page.about().click()
        assert driver.current_url == ABOUT_URL, 'переход не на ту страницу'

    def test_support_clickable(self, driver, wait):
        page = HomePage(driver, url=HOME_PAGE_URL)
        page.open()
        assert page.support().text == 'Поддержка', 'текст не соответствует'
        assert page.support().is_enabled(), 'не кликабельный'
        page.support().click()
        time.sleep(6)

    def test_donate_text_clickable(self, driver, wait):
        page = HomePage(driver, url=HOME_PAGE_URL)
        page.open()
        assert page.donate().text == 'Помочь Afisha', 'текст не соответствует'
        assert page.donate().is_enabled(), 'не кликабельный'
        page.donate().click()
        time.sleep(1)
        assert driver.current_url == DONATE_URL, 'переход не на ту страницу'

    def test_language_icon_clickable(self, driver, wait):
        page = HomePage(driver, url=HOME_PAGE_URL)
        page.open()
        assert page.language().is_enabled(), 'не кликабельный'

    def test_language_choice(self, driver, wait):
        page = HomePage(driver, url=HOME_PAGE_URL)
        page.open()
        page.language().click()
        time.sleep(2)
        page.english()
        assert page.english().text == 'English', 'текст не соответствует'
        assert page.english().is_enabled() == True, 'нельзя взаимодействовать'

    def test_avtorization_button_clickable(self, driver, wait):
        page = HomePage(driver, HOME_PAGE_URL)
        page.open()
        assert page.avtorization().text == 'Авторизоватьс', 'текст не соответствует'
        page.avtorization().click()
        time.sleep(1)
        assert driver.current_url == AVRORIZATION_URL, 'переход не на ту страницу'
