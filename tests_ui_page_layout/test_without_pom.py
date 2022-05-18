import playwright
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


# @pytest.mark.smoke
@pytest.mark.skip(reason="Not Ready")
def test_without_pom(set_up) -> None:
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # context = browser.new_context()
    # page = context.new_page()
    page = set_up
    page.locator('.button').click()
    # Assert Home page
    expect(page.locator("span[class='js-main-menu-button-text'] span span:nth-child(1)")).to_be_visible()
    page.locator("span[class='js-main-menu-button-text'] span span:nth-child(1)").click()

    # # Assert Payees Locator
    expect(page.locator("//span[normalize-space()='Payees']")).to_be_visible()
    page.locator("//span[normalize-space()='Payees']").click()

    home_header = page.locator('//h1/span').inner_text()
    print(home_header)
    expect(page.locator('//h1/span')).to_have_text("Payees")

    # context.close()
    # browser.close()

# with sync_playwright() as playwright:
#     test_navigate_to_payees_page(playwright)
