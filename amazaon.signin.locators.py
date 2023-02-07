from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

service = Service('https://github.com/EMRE1S1K/python-selenium-automation.git/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get('https://www.amazon.com/')
sleep(2)
#SEARCH STRATEGY
driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()

#TODO HOMEWORK2


#AMAZONLOGO
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

#EMAIL FIELD
driver.find_element(By.XPATH, "//input[@class='a-input-text a-span12 auth-autofocus auth-required-field']")

#CONTINUE BUTTON
driver.find_element(By.ID, "continue")

#NEED HELP LINK
driver.find_element(By.XPATH, '//span[@clas="a-expander-prompt"]//span[contains (text(), "Need Help")]')

#FORGOT YOUR PASW. LINK
driver.find_element(By.XPATH, '//a[@id="auth-fpp-link-bottom"]//a[contains (text(), "Forgot your password")]')

#Other issues with Sign-In link
driver.find_element(By.ID, "ap-other-signin-issues-link")

#Create your Amazon account button
driver.find_element(By.ID, "createAccountSubmit")
driver.find_element(By.XPATH, '//a[text()= "createAccountSubmit"]//a[@class="a-button-text"]')

#*Conditions of use link
driver.find_element(By.XPATH,'//a[@href="/gp/help/customer/display.html/ref=ap_desktop_footer_cou?"]//a[contains(text(), "Conditions Of Use")]')

#*Privacy Notice link
driver.find_element(By.XPATH, '//a[@href="/gp/help/customer/display.html/ref=ap_desktop_footer_privacy_notice?"]//a[contains(text(),"Privacy Notice")]')