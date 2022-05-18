import pytest
import pytest
from playwright.sync_api import Page

from pages.add_new_payee_pg import AddNewPayee
from pages.home_pg import HomePage
from pages.landing_pg import LandingPage

# from pages.payees import PayeesPage
# from pages.menu import Menu


# @pytest.fixture
# def set_up(page):
#     page.goto("https://www.demo.bnz.co.nz")
from pages.menu_pg import MenuPage
from pages.payees_pg import PayeePage
from pages.payment_pg import PaymentPage


@pytest.fixture
def landing_pg(page: Page) -> LandingPage:
    return LandingPage(page)


@pytest.fixture
def home_pg(page: Page) -> HomePage:
    return HomePage(page)


@pytest.fixture
def menu_pg(page: Page) -> MenuPage:
    return MenuPage(page)


@pytest.fixture
def payee_pg(page: Page) -> PayeePage:
    return PayeePage(page)


@pytest.fixture
def add_new_payee_pg(page: Page) -> AddNewPayee:
    return AddNewPayee(page)


@pytest.fixture
def payment_pg(page: Page) -> PaymentPage:
    return PaymentPage(page)
