

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from Facebook.BaseTest.login_locators import *

# driver = webdriver.Chrome()

from Facebook.BaseTest.register_locatorsss import *

def test_register():
    driver = webdriver.Chrome()
    driver.get(facebook_navigate)
    driver.maximize_window()
    time.sleep(7)
    driver.find_element(By.XPATH, create_account).click()
    time.sleep(7)
    driver.find_element(By.NAME, first_name).send_keys("werkineh")
    time.sleep(2)
    driver.find_element(By.NAME, last_name).send_keys("fikadu")
    time.sleep(2)
    driver.find_element(By.NAME, email).send_keys("0533831350")
    time.sleep(2)
    driver.find_element(By.XPATH, Password).send_keys("fikae22fikae22")
    time.sleep(2)
    driver.find_element(By.ID, Month).send_keys("Jan")
    time.sleep(2)
    driver.find_element(By.ID, Day).send_keys("27")
    time.sleep(2)
    driver.find_element(By.ID, Year).send_keys("1995")
    time.sleep(2)
    driver.find_element(By.NAME, Sex).send_keys("Male")
    time.sleep(2)
    driver.find_element(By.XPATH, gender).click()
    time.sleep(2)
    driver.find_element(By.XPATH, SignIn).click()
    time.sleep(30)

def test_register_inc_first_name():
    driver = webdriver.Chrome()
    driver.get(facebook_navigate)
    driver.maximize_window()
    time.sleep(7)
    driver.find_element(By.XPATH, create_account).click()
    time.sleep(7)
    driver.find_element(By.NAME, first_name).send_keys("qwertyu")
    time.sleep(2)
    driver.find_element(By.NAME, last_name).send_keys("fikadu")
    time.sleep(2)
    driver.find_element(By.NAME, email).send_keys("0533831350")
    time.sleep(2)
    driver.find_element(By.XPATH, Password).send_keys("fikae22fikae22")
    time.sleep(2)
    driver.find_element(By.ID, Month).send_keys("Jan")
    time.sleep(2)
    driver.find_element(By.ID, Day).send_keys("27")
    time.sleep(2)
    driver.find_element(By.ID, Year).send_keys("1995")
    time.sleep(2)
    driver.find_element(By.NAME, Sex).send_keys("Male")
    time.sleep(2)
    driver.find_element(By.XPATH, gender).click()
    time.sleep(2)
    driver.find_element(By.XPATH, SignIn).click()
    time.sleep(30)


def test_register_inc_last_name():
    driver = webdriver.Chrome()
    driver.get(facebook_navigate)
    driver.maximize_window()
    time.sleep(7)
    driver.find_element(By.XPATH, create_account).click()
    time.sleep(7)
    driver.find_element(By.NAME, first_name).send_keys("werkineh")
    time.sleep(2)
    driver.find_element(By.NAME, last_name).send_keys("asdfghj")
    time.sleep(2)
    driver.find_element(By.NAME, email).send_keys("0533831350")
    time.sleep(2)
    driver.find_element(By.XPATH, Password).send_keys("fikae22fikae22")
    time.sleep(2)
    driver.find_element(By.ID, Month).send_keys("Jan")
    time.sleep(2)
    driver.find_element(By.ID, Day).send_keys("27")
    time.sleep(2)
    driver.find_element(By.ID, Year).send_keys("1995")
    time.sleep(2)
    driver.find_element(By.NAME, Sex).send_keys("Male")
    time.sleep(2)
    driver.find_element(By.XPATH, gender).click()
    time.sleep(2)
    driver.find_element(By.XPATH, SignIn).click()
    time.sleep(30)

def test_register_inc_email():
    driver = webdriver.Chrome()
    driver.get(facebook_navigate)
    driver.maximize_window()
    time.sleep(7)
    driver.find_element(By.XPATH, create_account).click()
    time.sleep(7)
    driver.find_element(By.NAME, first_name).send_keys("werkineh")
    time.sleep(2)
    driver.find_element(By.NAME, last_name).send_keys("fikadu")
    time.sleep(2)
    driver.find_element(By.NAME, email).send_keys("0512345678")
    time.sleep(2)
    driver.find_element(By.XPATH, Password).send_keys("fikae22fikae22")
    time.sleep(2)
    driver.find_element(By.ID, Month).send_keys("Jan")
    time.sleep(2)
    driver.find_element(By.ID, Day).send_keys("27")
    time.sleep(2)
    driver.find_element(By.ID, Year).send_keys("1995")
    time.sleep(2)
    driver.find_element(By.NAME, Sex).send_keys("Male")
    time.sleep(2)
    driver.find_element(By.XPATH, gender).click()
    time.sleep(2)
    driver.find_element(By.XPATH, SignIn).click()
    time.sleep(30)


def test_register_inc_password():
    driver = webdriver.Chrome()
    driver.get(facebook_navigate)
    driver.maximize_window()
    time.sleep(7)
    driver.find_element(By.XPATH, create_account).click()
    time.sleep(7)
    driver.find_element(By.NAME, first_name).send_keys("werkineh")
    time.sleep(2)
    driver.find_element(By.NAME, last_name).send_keys("fikadu")
    time.sleep(2)
    driver.find_element(By.NAME, email).send_keys("0512345678")
    time.sleep(2)
    driver.find_element(By.XPATH, Password).send_keys("fikaeasdfghj")
    time.sleep(2)
    driver.find_element(By.ID, Month).send_keys("Jan")
    time.sleep(2)
    driver.find_element(By.ID, Day).send_keys("27")
    time.sleep(2)
    driver.find_element(By.ID, Year).send_keys("1995")
    time.sleep(2)
    driver.find_element(By.NAME, Sex).send_keys("Male")
    time.sleep(2)
    driver.find_element(By.XPATH, gender).click()
    time.sleep(2)
    driver.find_element(By.XPATH, SignIn).click()
    time.sleep(30)


def test_register_inc_month():
    driver = webdriver.Chrome()
    driver.get(facebook_navigate)
    driver.maximize_window()
    time.sleep(7)
    driver.find_element(By.XPATH, create_account).click()
    time.sleep(7)
    driver.find_element(By.NAME, first_name).send_keys("werkineh")
    time.sleep(2)
    driver.find_element(By.NAME, last_name).send_keys("fikadu")
    time.sleep(2)
    driver.find_element(By.NAME, email).send_keys("0512345678")
    time.sleep(2)
    driver.find_element(By.XPATH, Password).send_keys("fikae22fikae22")
    time.sleep(2)
    driver.find_element(By.ID, Month).send_keys("jun")
    time.sleep(2)
    driver.find_element(By.ID, Day).send_keys("27")
    time.sleep(2)
    driver.find_element(By.ID, Year).send_keys("1995")
    time.sleep(2)
    driver.find_element(By.NAME, Sex).send_keys("Male")
    time.sleep(2)
    driver.find_element(By.XPATH, gender).click()
    time.sleep(2)
    driver.find_element(By.XPATH, SignIn).click()
    time.sleep(30)


def test_register_inc_day():
    driver = webdriver.Chrome()
    driver.get(facebook_navigate)
    driver.maximize_window()
    time.sleep(7)
    driver.find_element(By.XPATH, create_account).click()
    time.sleep(7)
    driver.find_element(By.NAME, first_name).send_keys("werkineh")
    time.sleep(2)
    driver.find_element(By.NAME, last_name).send_keys("fikadu")
    time.sleep(2)
    driver.find_element(By.NAME, email).send_keys("0512345678")
    time.sleep(2)
    driver.find_element(By.XPATH, Password).send_keys("fikae22fikae22")
    time.sleep(2)
    driver.find_element(By.ID, Month).send_keys("Jan")
    time.sleep(2)
    driver.find_element(By.ID, Day).send_keys("28")
    time.sleep(2)
    driver.find_element(By.ID, Year).send_keys("1995")
    time.sleep(2)
    driver.find_element(By.NAME, Sex).send_keys("Male")
    time.sleep(2)
    driver.find_element(By.XPATH, gender).click()
    time.sleep(2)
    driver.find_element(By.XPATH, SignIn).click()
    time.sleep(30)


def test_register_inc_year():
    driver = webdriver.Chrome()
    driver.get(facebook_navigate)
    driver.maximize_window()
    time.sleep(7)
    driver.find_element(By.XPATH, create_account).click()
    time.sleep(7)
    driver.find_element(By.NAME, first_name).send_keys("werkineh")
    time.sleep(2)
    driver.find_element(By.NAME, last_name).send_keys("fikadu")
    time.sleep(2)
    driver.find_element(By.NAME, email).send_keys("0512345678")
    time.sleep(2)
    driver.find_element(By.XPATH, Password).send_keys("fikae22fikae22")
    time.sleep(2)
    driver.find_element(By.ID, Month).send_keys("Jan")
    time.sleep(2)
    driver.find_element(By.ID, Day).send_keys("27")
    time.sleep(2)
    driver.find_element(By.ID, Year).send_keys("1998")
    time.sleep(2)
    driver.find_element(By.NAME, Sex).send_keys("Male")
    time.sleep(2)
    driver.find_element(By.XPATH, gender).click()
    time.sleep(2)
    driver.find_element(By.XPATH, SignIn).click()
    time.sleep(30)


def test_register_inc_sex():
    driver = webdriver.Chrome()
    driver.get(facebook_navigate)
    driver.maximize_window()
    time.sleep(7)
    driver.find_element(By.XPATH, create_account).click()
    time.sleep(7)
    driver.find_element(By.NAME, first_name).send_keys("werkineh")
    time.sleep(2)
    driver.find_element(By.NAME, last_name).send_keys("fikadu")
    time.sleep(2)
    driver.find_element(By.NAME, email).send_keys("0512345678")
    time.sleep(2)
    driver.find_element(By.XPATH, Password).send_keys("fikae22fikae22")
    time.sleep(2)
    driver.find_element(By.ID, Month).send_keys("Jan")
    time.sleep(2)
    driver.find_element(By.ID, Day).send_keys("27")
    time.sleep(2)
    driver.find_element(By.ID, Year).send_keys("1995")
    time.sleep(2)
    driver.find_element(By.NAME, Sex).send_keys("f")
    time.sleep(2)
    driver.find_element(By.XPATH, gender).click()
    time.sleep(2)
    driver.find_element(By.XPATH, SignIn).click()
    time.sleep(30)


def test_register_empty_gender():
    driver = webdriver.Chrome()
    driver.get(facebook_navigate)
    driver.maximize_window()
    time.sleep(7)
    driver.find_element(By.XPATH, create_account).click()
    time.sleep(7)
    driver.find_element(By.NAME, first_name).send_keys("werkineh")
    time.sleep(2)
    driver.find_element(By.NAME, last_name).send_keys("fikadu")
    time.sleep(2)
    driver.find_element(By.NAME, email).send_keys("0512345678")
    time.sleep(2)
    driver.find_element(By.XPATH, Password).send_keys("fikae22fikae22")
    time.sleep(2)
    driver.find_element(By.ID, Month).send_keys("Jan")
    time.sleep(2)
    driver.find_element(By.ID, Day).send_keys("27")
    time.sleep(2)
    driver.find_element(By.ID, Year).send_keys("1995")
    time.sleep(2)
    driver.find_element(By.NAME, Sex).send_keys("Male")
    time.sleep(2)
    driver.find_element(By.XPATH, ).click()
    time.sleep(2)
    driver.find_element(By.XPATH, SignIn).click()
    time.sleep(30)