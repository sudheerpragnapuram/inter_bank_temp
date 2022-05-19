import playwright
import pytest
import logging
from playwright.sync_api import Playwright, sync_playwright, expect, Page

from pages.add_new_payee_pg import AddNewPayee
from pages.base_pg import BasePage
from pages.home_pg import HomePage
from pages.landing_pg import LandingPage
from pages.menu_pg import MenuPage
from pages.payees_pg import PayeePage
from pages.payment_pg import PaymentPage

logger = logging.getLogger(__name__)


# @pytest.mark.integration
# @pytest.mark.smoke
@pytest.mark.sanity(reason="Just for now")
class TestPayees:
    def test_navigate_to_payees_page(self, page: Page,
                                     landing_pg: LandingPage,
                                     home_pg: HomePage,
                                     menu_pg: MenuPage,
                                     payee_pg: PayeePage,
                                     add_new_payee_pg: AddNewPayee,
                                     payment_pg: PaymentPage
                                     ) -> None:
        landing_pg.load()
        landing_pg.click_check_btn()
        """
        Description: Verify you can navigate to Payees page using the navigation menu 
        """
        expect(home_pg.menu_btn).to_be_visible()
        home_pg.click_menu_btn()
        menu_pg.click_payees()
        print("Temp Menu closed")
        """
        TC2 Description: Verify you can add new payee in the Payees page
        """

        home_header = payee_pg.payee_header_text.inner_text()
        print(f'Header name is {home_header}')
        expect(payee_pg.payee_header_text).to_have_text("Payees")
        payee_pg.click_add_button()
        # page.locator("button[aria-label='Add payee'] span:nth-child(1)").click()
        expect(add_new_payee_pg.visible_model_content).to_be_visible()
        add_new_payee_pg.click_payee_name_text()

        bank_details = True
        while bank_details:
            if not page.is_visible("[placeholder=\"Bank\"]"):
                add_new_payee_pg.enter_name("Sudh")
                page.locator("a[role=\"option\"]:has-text(\"Someone new: \")").click()
            else:
                bank_details = False
                # print("Bank field is NOt FOUND..!")

        add_new_payee_pg.enter_bank_number("12", "3525", "8363557", "45")
        add_new_payee_pg.click_add_button()

        page.screenshot(path="NewClientError.png")
        # page.is_visible("span[role='alert']")

        if page.is_visible("span[role='alert']"):
            payee_Added_Message = payee_pg.alert_message()
            print(f'Success Message - {payee_Added_Message}')

        else:
            print("ERROR....New Payee is Not Added")

        # page.locator('#combobox-3901_-99').click()
        #
        # client_name = page.locator('ComboboxInput-apm-name').inner_text()
        #
        # print("New client name is", client_name)
        # print(f'New client name is {client_name}')
        #
        # # Default timeout
        # page.set_default_timeout(5000)
        # # Click a[role="option"]:has-text("Someone new: sudh")
        # page.locator("a[role=\"option\"]:has-text(\"Someone new: sudh\")").click()

        """
        TC3 Description: Verify payee name is a required field 
        """

        """
        TC4 Description: Verify list is sorted in ascending order by default
        """

        expected_sorted_list = ['Auckland Council', 'Babysitter', 'Cleaners', 'MERIDIAN ENERGY', 'Sudh',
                                'VODAFONE NZ LTD (MOBILE)']
        expected_reverse_list = ['VODAFONE NZ LTD (MOBILE)', 'Sudh', 'MERIDIAN ENERGY', 'Cleaners', 'Babysitter',
                                 'Auckland Council']
        # name = page.locator('text=Auckland').inner_text()
        #
        # print(f'Payee single name is {name}')

        actual_sorted_list = payee_pg.list_payee_names()  # names.sort(reverse=False)
        print(f'Expected sorted list names is {expected_sorted_list}')
        print(f'Actual sorted list names is {actual_sorted_list}')
        expect(payee_pg.locator_payee_names()).to_have_text(expected_sorted_list)

        """
        Description: Verify list is sorted in descending order
        """

        # After click
        page.locator('text=name').click()
        actual_reverse_list = payee_pg.list_payee_names()
        print(f'Expected Reverse list names is {expected_reverse_list}')
        print(f'Actual Reverse list names is {actual_reverse_list}')
        expect(payee_pg.locator_payee_names()).to_have_text(expected_reverse_list)

        """
                TC5 Description:  Navigate to Payments page
                """
        page.locator("div[class='Button']").click()
        home_pg.click_menu_btn()
        menu_pg.click_pay_or_transfer()
        payment_pg.account_selection_transfer("500", "check", "2345", "done", "chaki", "5335", "yes")

        if not page.is_visible("//div[@class='inner js-notification']"):
            payment_Message = page.locator("//div[@class='inner js-notification']").inner_text()
            print(f'Success Message - {payment_Message}')

        else:
            print("ERROR....Payment is not done...!")

        # account_names = page.locator('.name-1-1-65').all_inner_texts()
        # account_namess = page.locator('.name-1-1-65').all_text_contents()
        # print(f'Account names are {account_names}')
        # print(f'Account names are {account_namess}')


@pytest.mark.skip(reason="Not Ready")
# @pytest.mark.xfail(reason="Give any reaon, to test the fail")
# @pytest.mark.regression
def test_navigate_to_payees_page2(page):
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # context = browser.new_context()
    # page = context.new_page()

    # in the test
    base_page = BasePage(page)
    base_page.navigate()
    # page = context.new_page()
    landing_page = LandingPage(page)

    # landing_page = LandingPage()
    landing_page.click_check_it()

    # Assert Home page
    expect(page.locator("span[class='js-main-menu-button-text'] span span:nth-child(1)")).to_be_visible()
    landing_page.menu_click()
    # new Line


    # page.locator("span[class='js-main-menu-button-text'] span span:nth-child(1)").click()

    # Assert Payees Locator
    payee_page = PayeePage(page)
    expect(page.locator("//span[normalize-space()='Payees']")).to_be_visible()
    payee_page.payee_click()

    home_header = page.locator('//h1/span').inner_text()
    print(home_header)
    expect(page.locator('//h1/span')).to_have_text("Payees")
