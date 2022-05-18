from playwright.sync_api import Locator

from pages.base_pg import BasePage
from pages.payees_pg import PayeePage
from pages.payment_pg import PaymentPage


class MenuPage(BasePage):
    @property
    def payee_locator(self) -> Locator:
        return self.page.locator('.js-main-menu-payees a')

    def pay_or_transfer(self) -> Locator:
        return self.page.locator('text=Pay or transfer')

    def click_payees(self) -> PayeePage:
        self.payee_locator.click()
        return PayeePage(self.page)

    def click_pay_or_transfer(self) -> PaymentPage:
        self.pay_or_transfer().click()
        return PaymentPage(self.page)
