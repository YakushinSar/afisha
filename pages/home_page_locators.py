from selenium.webdriver.common.by import By

# header
AFISHA = (By.XPATH, '//*[@class="header__logo"]')
ABOUT = (By.XPATH, "//*[@class='header__nav-link'][contains(text(),'Об Афише')]")
SUPPORT = (By.XPATH, "//*[@class='header__nav-link'][contains(text(),'Поддержка')]")
DONATE = (By.XPATH, "//*[@class='header__nav-link'][contains(text(),'Помочь Afisha')]")
LANGUAGE = (By.XPATH, "//*[@aria-label='Выберите язык']")
AVTORIZATION = (By.XPATH, "//*[@class ='button__content'][contains(text(),'Авторизоваться')]")
ENGLISH = (By.XPATH, '//*[@href="/en"]')

# body
