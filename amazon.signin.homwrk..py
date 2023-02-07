from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

service = Service('https://github.com/EMRE1S1K/python-selenium-automation.git/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get('https://www.amazon.com/')
sleep(2)

driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()
expected_result = driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
actual_result = driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
print(actual_result)

print('test case passed')