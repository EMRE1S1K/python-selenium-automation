from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
HAMBURGER_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, "table.navFooterMoreOnAmazon td.navFooterDescItem")
HEADER_LINKS = (By.CSS_SELECTOR, '#nav-xshop a.nav-a')
BESTSELLERS_BUTTON = (By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_bestsellers']")
BESTSELLERS_LINK = (By.CSS_SELECTOR, "div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq  div._p13n-zg-nav-tab-all_style_zg-tabs-li-div__1YdPR")

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


@then('Click on bestsellers button')
def bestsellers_button(context):
    context.driver.find_element(*BESTSELLERS_BUTTON).click()


@then('Verify hamburger menu icon present')
def hamburger_menu(context):
    #print('\n find element:')
    element = context.driver.find_element(*HAMBURGER_MENU)
    #print(element)


@then('Verify that footer has {expected_amount_of_links} links')
def verify_footer_link_count(context, expected_amount_of_links):
    expected_amount_of_links = int(expected_amount_of_links)
    footer_links = context.driver.find_elements(*FOOTER_LINKS)
    print('\n Link count :', len(footer_links))
    assert len(footer_links) == expected_amount_of_links, f'expected {expected_amount_of_links} links but got {len(footer_links)}'


@then('Verify that header has {expected_amount_of_links} links')
def verify_header_link_count(context, expected_amount_of_links):
    expected_amount_of_links = int(expected_amount_of_links)
    header_links = context.driver.find_elements(*HEADER_LINKS)
    print('\n Link count :', len(header_links))
    assert len(header_links) == expected_amount_of_links, f'expected {expected_amount_of_links} links but got {len(header_links)}'


@then('Verify that bestsellers option has {expected_amount_of_links} links')
def verify_header_link_count(context, expected_amount_of_links):
    expected_amount_of_links = int(expected_amount_of_links)
    Bestsellers_links = context.driver.find_elements(*BESTSELLERS_LINK)
    print('\n Link count :', len(Bestsellers_links))
    assert len(Bestsellers_links) == expected_amount_of_links, f'expected {expected_amount_of_links} links but got {len(Bestsellers_links)}'