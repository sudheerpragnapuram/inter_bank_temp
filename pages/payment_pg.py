import string
from typing import List

from playwright.sync_api import Locator

from pages.add_new_payee_pg import AddNewPayee
from pages.base_pg import BasePage


class PaymentPage(BasePage):

    @property
    def from_options(self) -> Locator:
        return self.page.locator("[data-testid=\"from-account-chooser\"]")

    def everyday_account(self) -> Locator:
        return self.page.locator("//p[normalize-space()='Everyday']")

    def to_options(self) -> Locator:
        return self.page.locator("[data-testid=\"to-account-chooser\"]")

    def sel_account_option(self) -> Locator:
        return self.page.locator("[data-testid=\"to-account-accounts-tab\"]")

    def bills_account(self) -> Locator:
        return self.page.locator("//p[normalize-space()='Bills']")

    def amount_text(self) -> Locator:
        return self.page.locator("[placeholder=\"\\30 \\.00\"]")

    def stat_particular(self) -> Locator:
        return self.page.locator("[aria-label=\"Statement details\\, for payer\\, particulars\"]")

    def stat_code(self) -> Locator:
        return self.page.locator("[aria-label=\"Statement details\\, for payer\\, code\"]")

    def stat_reference(self) -> Locator:
        return self.page.locator("[aria-label=\"Statement details\\, for payer\\, reference\"]")

    def pay_particular(self) -> Locator:
        return self.page.locator("[aria-label=\"Statement details\\, for payee\\, particulars\"]")

    def pay_code(self) -> Locator:
        return self.page.locator("[aria-label=\"Statement details\\, for payee\\, code\"]")

    def pay_reference(self) -> Locator:
        return self.page.locator("[aria-label=\"Statement details\\, for payee\\, reference\"]")

    # Click text=Copy details
    def copy_details(self) -> Locator:
        return self.page.locator("text=Copy details")

    def transfer_button(self) -> Locator:
        return self.page.locator("button[class='Button-component-88 Button-component-106 Button-normalSize-96 "
                                 "Button-midblueColor-92 Button-solidVariant-89 Button-solidVariant-107'] span["
                                 "class='Button-wrapper-98']")

    def account_selection_transfer(self, amount, statement_particular, statement_code, statement_reference,
                                   payee_particular, payee_code, payee_reference):
        self.from_options.click()
        self.everyday_account().click()
        self.to_options().click()
        self.sel_account_option().click()
        self.bills_account().click()
        self.amount_text().fill(amount)
        self.stat_particular().fill(statement_particular)
        self.stat_code().fill(statement_code)
        self.stat_reference().fill(statement_reference)
        self.pay_particular().fill(payee_particular)
        self.pay_code().fill(payee_code)
        self.pay_reference().fill(payee_reference)
        self.copy_details().click()
        self.transfer_button().click()

    # ------------------------------------------------------------
    # After Added New Payee
    # ------------------------------------------------------------
