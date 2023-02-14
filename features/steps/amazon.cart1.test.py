from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Start amazon.com')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    sleep(1)


@when('Click on cart button')
def cart_empty(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/gp/cart/view.html?ref_=nav_cart']").click()


@then('Verify that cart is empty')
def product_check(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.XPATH, '//*[@id="sc-active-cart"]/div/div/div[2]/div[1]/h2').text
    assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
