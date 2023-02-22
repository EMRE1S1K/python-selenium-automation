from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Launch amazon')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    sleep(1)


@when('Search for espresso cream drink')
def product_search(context):
    context.driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox").send_keys('Espresso cream coffee')


@then('search button')
def click_saerch(context):
    context.driver.find_element(By.CSS_SELECTOR, "#nav-search-submit-button").click()


# @when('Add item into cart')
# def choosing_item(context):
#     context.driver.find_element(By.CSS_SELECTOR, "div._bGlmZ_badgeItemImage_2uh-g").click()


@then('Check the item')
def mov_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "#newAccordionRow > div > div.a-accordion-row-a11y.a-accordion-row.a-declarative.accordion-header.mobb-header-css").click()
    sleep(1)


@then('click again')
def mov_to_cart2(context):
    context.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-button").click()
    sleep(1)


@then('Check if item visible')
def visible_item(context):
    expected_result = context.driver.find_element(By.CSS_SELECTOR, "input[data-feature-id='proceed-to-checkout-action']")
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "input[data-feature-id='proceed-to-checkout-action']")
    assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
    print('Test case succesfull')
