from pages.home_page import HomePage
from pages.home_page_url import *
import time


class TestFuter():
    def test_afisha_logo_visible(self, driver):
        page = HomePage(driver, url=HOME_PAGE_URL)
        page.open()
        assert page.asisha_futer(), 'текст не видимый'

    def test_about_clickable(self, driver):
        page = HomePage(driver, url=HOME_PAGE_URL)
        page.open()
        assert page.about_futer(), 'текст не кликабельный'
        page.about_futer().click()
        assert driver.current_url == ABOUT_URL, 'страница не верная'

    def test_support_futer_clickable(self, driver):
        page = HomePage(driver, url=HOME_PAGE_URL)
        page.open()
        assert page.support_futer().text == 'Поддержка', "текст не соответсвует"
        page.support_futer().click()
        assert driver.current_url == SUPPORT_URL, 'неправильный переход на страницу'

    def test_donate_futer_clickable(self, driver):
        page = HomePage(driver, url=HOME_PAGE_URL)
        page.open()
        assert page.donate_futer().text == 'Помочь Afisha', "текст не соответствует"
        page.donate_futer().click()
        assert driver.current_url == DONATE_URL, 'неправильный переход на страницу'

    def test_limitation_futer_clickable(self, driver):
        page = HomePage(driver, url=HOME_PAGE_URL)
        page.open()
        assert page.limitation().text == 'Ограничение ответственности', "текст не соответствует"
        page.limitation().click()
        assert driver.current_url == LIMITATION_URL, 'неправильный переход на страницу'

    def test_instagram_enabled(self, driver):
        page = HomePage(driver, url=HOME_PAGE_URL)
        page.open()
        assert page.instagram().is_enabled() == True, 'недоступен для взаимодействия'

    def test_twitter_enabled(self, driver):
        page = HomePage(driver, url=HOME_PAGE_URL)
        page.open()
        assert page.twitter().is_enabled() == True, 'недоступен для взаимодействия'

    def test_linkedin_enabled(self, driver):
        page = HomePage(driver, url=HOME_PAGE_URL)
        page.open()
        assert page.linkedin().is_enabled() == True, 'недоступен для взаимодействия'

    def test_telegram_enabled(self, driver):
        page = HomePage(driver, url=HOME_PAGE_URL)
        page.open()
        assert page.telegram().is_enabled() == True, 'недоступен для взаимодействия'
