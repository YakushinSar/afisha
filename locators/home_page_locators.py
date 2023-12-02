from selenium.webdriver.common.by import By

class HomePageLocators:
#header
    AFISHA_PEREDELANO_HEDER= (By.XPATH,'//*[@class="header__logo"]')
    ABOUT_US_TEXT = (By.XPATH,"//*[@class='header__nav-link'][contains(text(),'Об Афише')]")
    SUPPORT_TEXT = (By.XPATH,"//*[@class='header__nav-link'][contains(text(),'Поддержка')]")
    HELP_AFISHA_TEXT = (By.XPATH,"//*[@class='header__nav-link'][contains(text(),'Помочь Afisha')]")
    LANGUAGE_SELECTOR = (By.XPATH,"//*[@aria-label='Выберите язык']")
    CONTENT_BUTTON = (By.XPATH,"//*[@class ='button__content'][contains(text(),'Пользователь')]")