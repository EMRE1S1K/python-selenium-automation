from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

AMAZON_SEARCH_FIELD=(By.ID, 'twotabsearchtextbox')
SEARCH_ICON=(By.ID, 'nav-search-submit-button')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    sleep(2)


@when('Input text {search_word}')
def input_search_word(context, search_word):
    context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(search_word)


@when('Click on search button')
def click_search_button(context):
    context.driver.find_element(*SEARCH_ICON).click()



