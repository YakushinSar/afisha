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
