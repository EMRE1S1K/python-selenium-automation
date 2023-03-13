from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    SIGNIN_SHOWN = (By.CSS_SELECTOR, "h1.a-spacing-small")
    CART_VERIFICATION = (By.CSS_SELECTOR, ".a-row.sc-your-amazon-cart-is-empty")
    VERIFY_ITEM = (By.CSS_SELECTOR, ".a-size-medium-plus.a-color-base.sw-atc-text.a-text-bold")

    def verify_search_result(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)

    def verify_signin_shown(self, expected_text):
        self.verify_text(expected_text, *self.SIGNIN_SHOWN)
        # actual_result = self.driver.find_element(*self.SIGNIN_SHOWN)
        # assert expected_text == actual_result, f'Error! Expected {expected_text}, but got {actual_result}'

    def empty_cart(self, expected_text):
        self.verify_text(expected_text, *self.CART_VERIFICATION)

    def item_in_cart(self,expected_text):
        self.verify_text(expected_text, *self.VERIFY_ITEM)
