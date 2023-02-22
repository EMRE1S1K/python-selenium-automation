from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open amazon customer service')
def amazon_customer_service(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')
    sleep(2)


@then('Verify welcome to amazon customer service is present')
def welcome_to_a_customer_service(context):
    expected_result = 'Welcome to Amazon Customer Service'
    actual_result = context.driver.find_element(By.XPATH, "//h1[contains(text(), 'Welcome to Amazon Customer Service')]").text
    assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'


@then('Verify that there is {shortcut_links} shortcut links')
def welcome_to_a_customer_service(context, shortcut_links):
    shortcut_links = int(shortcut_links)
    wrapper_links = context.driver.find_elements(By.CSS_SELECTOR, ".issue-card-container .issue-card-wrapper")
    print('\n Link count :', len(wrapper_links))
    assert len(wrapper_links) == shortcut_links, f'expected {shortcut_links} links but got {len(wrapper_links)}'
    print('Verified')


@then('Verify that Search our help library is shown')
def search_library_shown(context):
    expected_result = 'Search our help library'
    actual_result = context.driver.find_element(By.XPATH, "//h2[contains(text(),'Search our help library')]").text
    assert expected_result == actual_result, f'Error! Expected {expected_result} but got {actual_result}'
    print('Verified')


@then('Verify search box is present')
def welcome_to_a_customer_service(context):
    context.driver.find_element(By.CSS_SELECTOR, "#hubHelpSearchInput")
    print('\n Help Search box is present')
    print('Verified')


@when('Verify All help topics is shown')
def welcome_to_a_customer_service(context):
    expected_result='All help topics'
    actual_result = context.driver.find_element(By.XPATH, "//h2[contains(text(),'All help topics')]").text
    assert expected_result == actual_result, f'Error! Expected {expected_result} but got {actual_result}'
    print('Verified')


@then('Verify that customer service has {help_links} links')
def verify_help_links(context,help_links):
    help_links = int(help_links)
    helper_links = context.driver.find_elements(By.CSS_SELECTOR, ".help-topics")
    print('\n Link count:', len(helper_links))
    assert len(helper_links) == help_links, f'expected {help_links} but got {len(helper_links)}'
    print('Verified')


# @then('Verify that header has {expected_amount_of_links} links')
# def verify_header_link_count(context, expected_amount_of_links):
#     expected_amount_of_links = int(expected_amount_of_links)
#     header_links = context.driver.find_elements(*HEADER_LINKS)
#     print('\n Link count :', len(header_links))
#     assert len(header_links) == expected_amount_of_links, f'expected {expected_amount_of_links}  but got {len(header_links)}'