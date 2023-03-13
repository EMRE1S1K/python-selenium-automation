from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ITEM_LOCATOR = (By.CSS_SELECTOR, "div._bGlmZ_badgeItemImage_2uh-g")
FIRST_MOVE = (By.CSS_SELECTOR, "i.a-icon.a-accordion-radio.a-icon-radio-inactive")
SECOND_MOVE = (By.CSS_SELECTOR, "#add-to-cart-button")
VERIFY_ITEM = (By.CSS_SELECTOR, ".a-section.a-padding-medium.sw-atc-message-section")


@when('Search for {any_item}')
def product_search(context, any_item):
    context.app.header.input_search_text(any_item)


@then('search button')
def click_search(context):
    context.app.header.click_search()


@when('Select an item')
def choosing_item(context):
    context.app.header.item_selection()


@then('Move item into cart')
def mov_to_cart(context):
    context.app.header.moving_item_first()
    sleep(1)


@then('click again')
def mov_to_cart2(context):
    context.app.header.moving_tem_second()
    sleep(1)


@then('Check if {expected_text} text shown')
def visible_item(context,expected_text):
    context.app.search_results_page.item_in_cart(expected_text)
