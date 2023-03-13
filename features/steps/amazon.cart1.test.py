from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_BUTTON = (By.CSS_SELECTOR, "#nav-cart-count-container")
CART_VERIFICATION= (By.CSS_SELECTOR, ".a-row.sc-your-amazon-cart-is-empty")


@when('Click on cart button')
def cart_click(context):
    # context.driver.find_element(*CART_BUTTON).click()
    context.app.header.cart_icon()


@then('Empty {expected_text} text shown')
def product_check(context, expected_text):
    context.app.search_results_page.empty_cart(expected_text)
    # expected_result = 'Your Amazon Cart is empty'
    # actual_result = context.driver.find_element(*CART_VERIFICATION).text
    # assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
