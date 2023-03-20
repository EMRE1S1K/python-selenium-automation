from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    SIGNIN_BUTTON = (By.CSS_SELECTOR, "#nav-signin-tooltip span.nav-action-inner")
    AMAZON_ORDERS = (By.CSS_SELECTOR, "#nav-orders")
    CART_BUTTON = (By.CSS_SELECTOR, "#nav-cart-count-container")
    ITEM_LOCATOR = (By.CSS_SELECTOR, "div._bGlmZ_badgeItemImage_2uh-g")
    FIRST_MOVE = (By.CSS_SELECTOR, "i.a-icon.a-accordion-radio.a-icon-radio-inactive")
    SECOND_MOVE = (By.CSS_SELECTOR, "#add-to-cart-button")
    LANGUAGE_OPTIONS =(By.ID, 'icp-nav-flyout')
    LANGUAGE = (By.CSS_SELECTOR, "a[href='#switch-lang=es_US']")
    DEPARTMENT_DROPDOWN = (By.ID, 'searchDropdownBox')
    NEW_ARRIVALS = (By.CSS_SELECTOR, "a[aria-label='New Arrivals'] span.nav-a-content")
    NEW_DEALS = (By.CSS_SELECTOR, ".mm-merch-panel h3")

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

    def hover_language_options(self):
        language_options = self.find_element(*self.LANGUAGE_OPTIONS)
        actions = ActionChains(self.driver)
        actions.move_to_element(language_options)
        actions.perform()

    def verify_language_shown(self):
        self.wait_for_element_appear(*self.LANGUAGE)

    def hover_new_arrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def new_arrivals_shown(self):
        self.wait_for_element_appear(*self.NEW_DEALS)

    def select_department(self, alias):
        department_dropdown = self.find_element(*self.DEPARTMENT_DROPDOWN)
        select = Select(department_dropdown)
        select.select_by_value(f'search-alias={alias}')
