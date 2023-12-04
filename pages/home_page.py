from base.seleniumbase import BasePage
from pages.home_page_locators import *


class HomePage(BasePage):
    def header(self):
        return self.is_visible(AFISHA)

    def about(self):
        return self.is_clickable(ABOUT)

    def support(self):
        return self.is_clickable(SUPPORT)

    def donate(self):
        return self.is_clickable(DONATE)

    def language(self):
        return self.is_clickable(LANGUAGE)

    def english(self):
        return self.is_clickable(ENGLISH)

    def avtorization(self):
        return self.is_visible(AVTORIZATION)

    def asisha_futer(self):
        return self.is_visible(AFISHA_FUTER)

    def about_futer(self):
        return self.is_clickable(ABOUT_FUTER)

    def support_futer(self):
        return self.is_clickable(SUPPORT_FUTER)

    def donate_futer(self):
        return self.is_clickable(DONATE_FUTER)

    def limitation(self):
        return self.is_clickable(LIMITATION)
