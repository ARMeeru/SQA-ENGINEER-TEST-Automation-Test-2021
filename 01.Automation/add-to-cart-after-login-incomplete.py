from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
from time import sleep

driver = webdriver.Chrome()

url = 'http://automationpractice.com/index.php'
driver.get(url)
driver.maximize_window()

WebDriverWait(driver, 10).until(
    EC.visibility_of_any_elements_located((By.CLASS_NAME, 'login')))
sign_in = driver.find_element_by_class_name('login')
sign_in.click()

WebDriverWait(driver, 10).until(
    EC.visibility_of_any_elements_located((By.ID, 'email')))
email_address = driver.find_element_by_id('email')
email_address.send_keys('meeru@testing.xyz')

WebDriverWait(driver, 10).until(
    EC.visibility_of_any_elements_located((By.ID, 'passwd')))
email_address = driver.find_element_by_id('passwd')
email_address.send_keys('123456789')

sign_in = driver.find_element_by_id('SubmitLogin')
sign_in.click()

WebDriverWait(driver, 10).until(
    EC.visibility_of_any_elements_located((By.CLASS_NAME, 'sf-with-ul')))
navigate_to_dress = driver.find_element_by_class_name('sf-with-ul')
navigate_to_dress.click()

WebDriverWait(driver, 10).until(
    EC.visibility_of_any_elements_located((By.CLASS_NAME, 'button.ajax_add_to_cart_button.btn.btn-default')))
add_to_cart_1 = driver.find_element_by_class_name(
    'button.ajax_add_to_cart_button.btn.btn-default')
add_to_cart_1.click()
