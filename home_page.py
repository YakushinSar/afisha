from base.seleniumbase import BasePage
from base.home_page_locators import HomePageLocators


class HomePage(BasePage):
    def header(self):
        return self.is_visible(HomePageLocators.AFISHA_PEREDELANO_HEDER)

    def about(self):
        return self.is_clickable(HomePageLocators.ABOUT_US_TEXT)

    def support(self):
        return self.is_visible(HomePageLocators.SUPPORT_TEXT)

    def help(self):
        return self.is_visible(HomePageLocators.HELP_AFISHA_TEXT)

    def language(self):
        return self.is_visible(HomePageLocators.LANGUAGE_SELECTOR)

    def contest(self):
        return self.is_clickable(HomePageLocators.CONTENT_BUTTON)
