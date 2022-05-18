from pages.base_pg import BasePage
from playwright.sync_api._generated import Locator

from pages.home_pg import HomePage


class LandingPage(BasePage):
    # def __init__(self, page):
    #     self.page = page
    @property
    def check_btn(self) -> Locator:
        return self.page.locator('.button')
        # self.page.click('.button')

    def load(self) -> None:
        """Load the home page."""
        self.page.goto(f"{self.base_url}")

    def click_check_btn(self) -> HomePage:
        """Click the menu button"""
        self.check_btn.click()
        return HomePage(self.page)

        # return Menu(self.page)

    # def menu_click(self):
    #     self.page.click("span[class='js-main-menu-button-text'] span span:nth-child(1)")


# @property
# def menu_button(self) -> Locator:
#     return self.page.locator(".MenuButton")
#
#
# def load(self) -> None:
#     """Load the home page."""
#     self.page.goto(f"{self.base_url}")
#
#
# def clickMenu(self) -> Menu:
#     """Click the menu button"""
#     self.menu_button.click();
#     return Menu(self.page)
