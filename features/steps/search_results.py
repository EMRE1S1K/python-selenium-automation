from selenium.webdriver.common.by import By
from behave import given, when, then
#from time import sleep

PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")

@then('Verify that text {expected_result} is shown')
def verify_text_result(context, expected_result):
    context.app.search_results_page.verify_signin_shown(expected_result)
    # actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    # assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'



    # print('\n find elements:')
    # elements = context.driver.find_element(*HAMBURGER_MENU)
    # print(elements)
     # assert len(elements) == 1, f'Expected 1 element but got {len(elements)}'


@then('Verify {category} department selected')
def verify_text_result(context, category):
    context.app.search_results_page.verify_selected_department(category)