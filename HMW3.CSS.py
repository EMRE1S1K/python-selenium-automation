from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

service = Service('https://github.com/EMRE1S1K/python-selenium-automation.git/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get('https://www.amazon.com/')
sleep(1)
#CSS SELECTORS HMW3

#Amazon logo
driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")
#Create account
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
#Name section
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")
#Mobile or email section
driver.find_element(By.CSS_SELECTOR, "input[data-validation-id='email']")
#password section
driver.find_element(By.CSS_SELECTOR, "input[name='password']")
#password re-entry section
driver.find_element(By.CSS_SELECTOR, "input[name='passwordCheck']")
#length of char. section
driver.find_element(By.CSS_SELECTOR, "div.a-alert-content")
#continue section ##*= is not working.
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")
#privacy notice sec. ##*+not working!:(
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")
#already have an account sec.
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis[href='/ap/signin?showRmrMe=1&openid.pape.max_auth_age=0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&accountStatusPolicy=P1&pageId=webcs-yourorder&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcss%2Forder-history%3Fie%3DUTF8%26ref_%3Dnav_orders_first&prevRID=NMFYZ4WVT5DQHWDT5PC6&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0']").click()

