from typing import List

from playwright.sync_api import Locator

from pages.base_pg import BasePage


class AddNewPayee(BasePage):

    @property
    def visible_model_content(self) -> Locator:
        return self.page.locator('.js-modal-inner.Modal-content')

    def payee_name_text(self) -> Locator:
        return self.page.locator("input[name=\"apm-name\"]")

    def bank_text(self) -> Locator:
        return self.page.locator('#apm-bank')

    def branch_text(self) -> Locator:
        return self.page.locator('#apm-branch')

    def account_text(self) -> Locator:
        return self.page.locator('#apm-account')

    def suffix_text(self) -> Locator:
        return self.page.locator('#apm-suffix')

    def add_button(self) -> Locator:
        return self.page.locator("button[class='js-submit Button Button--primary Button--disabled']")

    def click_payee_name_text(self) -> None:
        return self.payee_name_text().click()

    def enter_name(self, name):
        self.payee_name_text().type(name)

    def enter_bank_number(self, bank, branch, account, suffix):
        self.bank_text().fill(bank)
        self.branch_text().fill(branch)
        self.account_text().fill(account)
        self.suffix_text().fill(suffix)

    def click_add_button(self):
        self.add_button().click()
