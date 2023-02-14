from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Get amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    sleep(1)


@when('Check the orders&returns')
def orders_returns(context):
    context.driver.find_element(By.CSS_SELECTOR, "#nav-orders").click()


@then('Verify Sign in text shown')
def sign_in_shown(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small").text
    assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
