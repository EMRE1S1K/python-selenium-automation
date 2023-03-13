from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
SIGNIN_BUTTON = (By.CSS_SELECTOR,  "#nav-signin-tooltip span.nav-action-inner")


@when('Click on Amazon orders')
def orders_returns(context):
    # context.driver.wait.until(EC.element_to_be_clickable(SIGNIN_BUTTON)).click()
    context.app.header.amazon_orders()


@then('Verify {expected_text} text shown')
def sign_in_shown(context, expected_text):
    context.app.search_results_page.verify_signin_shown(expected_text)
    # expected_result = 'Sign in'
    # actual_result = context.driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small").text
    # assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
