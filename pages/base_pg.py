# models/search.py
from playwright.sync_api import Page


class BasePage(object):
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://www.demo.bnz.co.nz"


