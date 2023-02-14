from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

service = Service('https://github.com/EMRE1S1K/python-selenium-automation.git/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get('https://www.amazon.com/')
sleep(3)

driver.find_element(By.ID, 'twotabsearchtextbox').click()
#BY CSS using ID
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
#BY CSS using attributes
#BY CSS using  multiple attributes
#BY CSS using class  + atributtes
#BY CSS using attributes,partial match *=

#for from parents to child
#(watch svetlena from 1.10)


