from playwright.sync_api import Locator

from pages.base_pg import BasePage
from pages.menu_pg import MenuPage


class HomePage(BasePage):
    @property
    def menu_btn(self) -> Locator:
        return self.page.locator('.MenuButton')

    def click_menu_btn(self) -> MenuPage:
        self.menu_btn.click()
        return MenuPage(self.page)
