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
# futher
AFISHA_FUTER = (By.XPATH, '//*[@aria-current="page"]')
ABOUT_FUTER = (By.XPATH, ' //*[@class="navigation__link"][contains(text(),"Об Афише")]')
SUPPORT_FUTER = (By.XPATH, '//*[@class="navigation__link"][contains(text(),"Поддержка")]')
DONATE_FUTER = (By.XPATH, '//*[@class="navigation__link"][contains(text(),"Помочь Afisha")]')
LIMITATION = (By.XPATH, '//*[@class="navigation__link"][contains(text(),"Ограничение ответственности")]')

INSTAGRAM = (By.XPATH, "//a[@href='https://www.instagram.com/afisha_peredelano/']")
TWITTER = (By.XPATH, "//a[@href='https://twitter.com/afisha_prdln']")
LINKEDIN = (By.XPATH, "//a[@href='https://www.linkedin.com/company/afisha-peredelano']")
TELEGRAM = (By.XPATH, "//a[@href='https://t.me/afisha_peredelano']")
