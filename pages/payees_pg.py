import string
from typing import List

from playwright.sync_api import Locator

from pages.add_new_payee_pg import AddNewPayee
from pages.base_pg import BasePage


class PayeePage(BasePage):

    @property
    def payee_header_text(self) -> Locator:
        return self.page.locator('//h1/span')

    def add_button(self) -> Locator:
        return self.page.locator("button[aria-label='Add payee'] span:nth-child(1)")

    def locator_payee_names(self) -> Locator:
        return self.page.locator('.js-payee-name')

    def list_payee_names(self) -> List[str]:
        return self.locator_payee_names().all_inner_texts()

    def click_add_button(self) -> AddNewPayee:
        self.add_button().click()
        return AddNewPayee(self.page)

    # ------------------------------------------------------------
    # After Added New Payee
    # ------------------------------------------------------------
    def alert_message(self) -> string:
        return self.page.wait_for_selector("span[role='alert']", timeout=1000).inner_text()
