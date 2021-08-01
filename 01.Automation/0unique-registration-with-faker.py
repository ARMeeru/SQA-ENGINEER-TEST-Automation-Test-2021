# This script solved the point 1 and 2 of first problem
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
import random
import string
from time import sleep
# This should be installed https://stackoverflow.com/a/61175792 to avoid related error
from faker import Faker


def random_characters(y):
    return ''.join(random.choice(string.ascii_letters) for _x in range(y))


def random_hexdigits(y):
    return ''.join(random.choice(string.hexdigits) for _x in range(y))


driver = webdriver.Chrome()

url = 'http://automationpractice.com/index.php'
driver.get(url)
driver.maximize_window()

WebDriverWait(driver, 10).until(
    EC.visibility_of_any_elements_located((By.CLASS_NAME, 'login')))
sign_in = driver.find_element_by_class_name('login')
sign_in.click()

WebDriverWait(driver, 10).until(
    EC.visibility_of_any_elements_located((By.ID, 'email_create')))
email_registration = driver.find_element_by_id('email_create')

fake = Faker()
proper_email = fake.ascii_email()
email_registration.send_keys(proper_email)

create_account = driver.find_element_by_id('SubmitCreate')
create_account.click()

WebDriverWait(driver, 10).until(
    EC.visibility_of_any_elements_located((By.ID, 'account-creation_form')))

button_mister = driver.find_element_by_id('id_gender1')
button_mister.click()

# uncomment next two lines for using mrs
# button_missus = driver.find_element_by_id('id_gender2')
# button_missus.click()

customer_firstname = driver.find_element_by_id('customer_firstname')
firstname = fake.first_name()
customer_firstname.send_keys(firstname)

customer_lastname = driver.find_element_by_id('customer_lastname')
lastname = fake.last_name()
customer_lastname.send_keys(lastname)

password_field = driver.find_element_by_id('passwd')
password = fake.password(10)
password_field.send_keys(password)

dropdown_days = Select(driver.find_element_by_id('days'))

WebDriverWait(driver, 10).until(
    EC.visibility_of_any_elements_located((By.ID, 'uniform-days')))

birth_date = random.randint(1, 28)  # avoiding february mishappen
dropdown_days.select_by_index(birth_date)

dropdown_months = Select(driver.find_element_by_id('months'))

WebDriverWait(driver, 10).until(
    EC.visibility_of_any_elements_located((By.ID, 'uniform-months')))

birth_month = random.randint(0, 12)
dropdown_months.select_by_index(birth_month)

dropdown_years = Select(driver.find_element_by_id('years'))

WebDriverWait(driver, 10).until(
    EC.visibility_of_any_elements_located((By.ID, 'uniform-years')))

index_year = random.randint(19, 90)
dropdown_years.select_by_index(index_year)


def get_year_by_index(value):
    keys_list = list(range(19, 91))
    values_list = list(range(2002, 1930, -1))
    zip_iterator = zip(keys_list, values_list)
    year_dictionary = dict(zip_iterator)
    return year_dictionary[value]


birth_year = get_year_by_index(index_year)

date_of_birth = f'{birth_date}-{birth_month}-{birth_year}'

signup_for_newsletter = driver.find_element_by_id('newsletter')
signup_for_newsletter.click()

receive_special_offers = driver.find_element_by_id('optin')
receive_special_offers.click()

firstname_your_address = driver.find_element_by_id('firstname')
firstname_your_address.send_keys(firstname)

lastname_your_address = driver.find_element_by_id('lastname')
firstname_your_address.send_keys(lastname)

company_info = driver.find_element_by_id('company')
company = random_characters(15).lower()
company_info.send_keys(company)

address_field_1 = driver.find_element_by_id('address1')
address = fake.street_address()
address_field_1.send_keys(address)

address_field_2 = driver.find_element_by_id('address2')
address = fake.street_address()
address_field_2.send_keys(address)

city_field = driver.find_element_by_id('city')
city = fake.city()
city_field.send_keys(city)

dropdown_states = Select(driver.find_element_by_id('id_state'))

WebDriverWait(driver, 10).until(
    EC.visibility_of_any_elements_located((By.ID, 'uniform-id_state')))

index_state = random.randint(1, 53)
dropdown_states.select_by_index(index_state)

index_state_dict = {1: 'Alabama', 2: 'Alaska', 3: 'Arizona', 4: 'Arkansas', 5: 'California', 6: 'Colorado', 7: 'Connecticut', 8: 'Delaware', 9: 'District of Columbia', 10: 'Florida', 11: 'Georgia', 12: 'Hawaii', 13: 'Idaho', 14: 'Illinois', 15: 'Indiana', 16: 'Iowa', 17: 'Kansas', 18: 'Kentucky', 19: 'Louisiana', 20: 'Maine', 21: 'Maryland', 22: 'Massachusetts', 23: 'Michigan', 24: 'Minnesota', 25: 'Mississippi', 26: 'Missouri', 27: 'Montana',
                    28: 'Nebraska', 29: 'Nevada', 30: 'New Hampshire', 31: 'New Jersey', 32: 'New Mexico', 33: 'New York', 34: 'North Carolina', 35: 'North Dakota', 36: 'Ohio', 37: 'Oklahoma', 38: 'Oregon', 39: 'Pennsylvania', 40: 'Puerto Rico', 41: 'Rhode Island', 42: 'South Carolina', 43: 'South Dakota', 44: 'Tennessee', 45: 'Texas', 46: 'US Virgin Islands', 47: 'Utah', 48: 'Vermont', 49: 'Virginia', 50: 'Washington', 51: 'West Virginia', 52: 'Wisconsin', 53: 'Wyoming'}

selected_state = index_state_dict[index_state]
sleep(3)
postcode_field = driver.find_element_by_id('postcode')
postcode = fake.postalcode()
postcode_field.send_keys(postcode)

additional_information = driver.find_element_by_id('other')
ai = random_characters(15).lower()
additional_information.send_keys(ai)

home_phone_field = driver.find_element_by_id('phone')
home_phone = fake.random_number(11)
home_phone_field.send_keys(home_phone)

phone_mobile_field = driver.find_element_by_id('phone_mobile')
phone_mobile = fake.random_number(11)
phone_mobile_field.send_keys(phone_mobile)

alias_field = driver.find_element_by_id('alias')
alias = random_characters(5).lower()
alias_field.send_keys(alias)

register_button = driver.find_element_by_id('submitAccount')
register_button.click()

WebDriverWait(driver, 10).until(
    EC.visibility_of_any_elements_located((By.CLASS_NAME, 'logout')))
logout_button = driver.find_element_by_class_name('logout')
logout_button.click()

driver.close()
# Last completion time was 3m 50s which could be a network issue
