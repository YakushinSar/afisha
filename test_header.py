from home_page_url import *
from seleniumbase import BasePage
from home_page_locators import *
from selenium.webdriver.support import expected_conditions as EC


def test_afisha_header(driver):
    page = BasePage(driver, HOME_PAGE_URL)
    page.open()
    assert page.is_visible(AFISHA_PEREDELANO_HEDER), 'текст не видимый'


def test_about_clickable(driver, wait):
    page = BasePage(driver, HOME_PAGE_URL)
    page.open()
    about = wait.until(EC.visibility_of_element_located(ABOUT_US_TEXT))
    assert about.text == 'Об Афише', 'текст не соответствует'
    assert page.is_clickable(ABOUT_US_TEXT), 'не кликабельный'
    about.click()
    assert driver.current_url == ABOUT_URL, 'переход не на ту страницу'


def test_support_clickable(driver, wait):
    page = BasePage(driver, HOME_PAGE_URL)
    page.open()
    support = wait.until(EC.visibility_of_element_located(SUPPORT_TEXT))
    assert support.text == 'Поддержка', 'текст не соответствует'
    assert page.is_clickable(SUPPORT_TEXT), 'не кликабельный'
    # support.click()
    # assert driver.current_url == SUPPORT_URL, 'переход не на ту страницу'


def test_help_clickable(driver, wait):
    page = BasePage(driver, HOME_PAGE_URL)
    page.open()
    help = wait.until(EC.visibility_of_element_located(HELP_AFISHA_TEXT))
    assert help.text == 'Помочь Afisha', 'текст не соответствует'
    assert page.is_clickable(HELP_AFISHA_TEXT), 'не кликабельный'
    help.click()
    assert driver.current_url == DONATE_URL, 'переход не на ту страницу'


def test_language_clickable(driver):
    page = BasePage(driver, HOME_PAGE_URL)
    page.open()
    assert page.is_clickable(LANGUAGE_SELECTOR), 'не кликабельный'


def test_avtorization_clickable(driver, wait):
    page = BasePage(driver, HOME_PAGE_URL)
    page.open()
    content = wait.until(EC.visibility_of_element_located(CONTENT_BUTTON))
    assert content.text == 'Авторизоваться', 'текст не соответствует'
    assert page.is_clickable(CONTENT_BUTTON)
    content.click()
    assert driver.current_url == AVRORIZATION_URL, 'переход не на ту страницу'
