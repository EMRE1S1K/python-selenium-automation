from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

PRIVACY_NOTICE = (By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']")
CUSTOMER_SERVICE = (By.CSS_SELECTOR,".cs-help-title")


@given('Open Amazon T&C page')
def privacy_notice(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')
    sleep(2)


@when('Store original windows')
def store_current_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)


@when('Click on Amazon Privacy Notice link')
def privacy_notice_link(context):
    context.driver.find_element(*PRIVACY_NOTICE).click()


@when('Switch to the newly opened window')
def switch_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    context.driver.switch_to.window(windows[1])
    context.current_window = context.driver.current_window_handle
    print(context.current_window)


@then('Verify Amazon Privacy Notice page is opened')
def new_window_opened(context):
    context.driver.wait.until(EC.text_to_be_present_in_element(CUSTOMER_SERVICE, text_='Help & Customer Service'))



@then('User can close new window and switch back to original')
def close_and_switch_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)
