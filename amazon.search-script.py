from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

service = Service('https://github.com/EMRE1S1K/python-selenium-automation.git/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get('https://www.amazon.com/')
sleep(3)


driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee')
driver.find_element(By.ID, 'nav-search-submit-button').click()


expected_result = '"coffee"'
actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
print(actual_result)

print('Test Case Passed')
driver.quit()
