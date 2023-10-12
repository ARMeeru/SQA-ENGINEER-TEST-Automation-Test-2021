from selenium import webdriver
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from faker import Faker
import random

def random_string(y, chars=string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(y))

def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))

fake = Faker()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://automationpractice.com/index.php')

# Start Registration
wait_for_element(driver, By.CLASS_NAME, 'login').click()
wait_for_element(driver, By.ID, 'email_create').send_keys(fake.ascii_email())
driver.find_element_by_id('SubmitCreate').click()

# Personal Details
wait_for_element(driver, By.ID, 'account-creation_form')
driver.find_element_by_id('id_gender1').click()
first_name, last_name = fake.first_name(), fake.last_name()
driver.find_element_by_id('customer_firstname').send_keys(first_name)
driver.find_element_by_id('customer_lastname').send_keys(last_name)
driver.find_element_by_id('passwd').send_keys(fake.password(10))
Select(driver.find_element_by_id('days')).select_by_index(random.randint(1, 28))
Select(driver.find_element_by_id('months')).select_by_index(random.randint(1, 12))
Select(driver.find_element_by_id('years')).select_by_index(random.randint(19, 90))
driver.find_element_by_id('newsletter').click()
driver.find_element_by_id('optin').click()

# Address Details
driver.find_element_by_id('company').send_keys(random_string(15).lower())
driver.find_element_by_id('address1').send_keys(fake.street_address())
driver.find_element_by_id('address2').send_keys(fake.street_address())
driver.find_element_by_id('city').send_keys(fake.city())
Select(driver.find_element_by_id('id_state')).select_by_index(random.randint(1, 53))
driver.find_element_by_id('postcode').send_keys(fake.zipcode())
driver.find_element_by_id('other').send_keys(random_string(15).lower())
driver.find_element_by_id('phone').send_keys(fake.phone_number())
driver.find_element_by_id('phone_mobile').send_keys(fake.phone_number())
driver.find_element_by_id('alias').send_keys(random_string(5).lower())
driver.find_element_by_id('submitAccount').click()

# Logout and Close
wait_for_element(driver, By.CLASS_NAME, 'logout').click()
driver.close()
