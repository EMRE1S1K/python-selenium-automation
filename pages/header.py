from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    SIGNIN_BUTTON = (By.CSS_SELECTOR, "#nav-signin-tooltip span.nav-action-inner")
    AMAZON_ORDERS = (By.CSS_SELECTOR, "#nav-orders")
    CART_BUTTON = (By.CSS_SELECTOR, "#nav-cart-count-container")
    ITEM_LOCATOR = (By.CSS_SELECTOR, "div._bGlmZ_badgeItemImage_2uh-g")
    FIRST_MOVE = (By.CSS_SELECTOR, "i.a-icon.a-accordion-radio.a-icon-radio-inactive")
    SECOND_MOVE = (By.CSS_SELECTOR, "#add-to-cart-button")


    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def signin_clickable(self):
        e = self.wait.until(EC.element_to_be_clickable(*self.SIGNIN_BUTTON), message=f'Element not clickable by {self.SIGNIN_BUTTON}')
        e.click()

    def amazon_orders(self):
        self.click(*self.AMAZON_ORDERS)

    def cart_icon(self):
        self.click(*self.CART_BUTTON)

    def item_selection(self):
        self.click(*self.ITEM_LOCATOR)

    def moving_item_first(self):
        self.click(*self.FIRST_MOVE)

    def moving_tem_second(self):
        self.click(*self.SECOND_MOVE)