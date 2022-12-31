
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from Facebook.BaseTest.login_locators import *

driver = webdriver.Chrome()

def test_login_cor_username_and_password():
    # when login facebook by username and password fild

    driver = webdriver.Chrome()
    driver.get(facebook_path)
    fb_user = driver.find_element(By.XPATH, login_email_path1)
    fb_user.send_keys("0533831350")
    time.sleep(3)
    fb_password = driver.find_element(By.XPATH, login_password_path)
    fb_password.send_keys("fikae22fikae22")
    time.sleep(3)
    driver.find_element(By.XPATH, login_button_path).click()
    time.sleep(20)






def test_login_inc_mail():

    # when login facebook by incorrect username and password fild
    driver.get(facebook_path)
    driver.maximize_window()
    login_email_feild = driver.find_element(By.XPATH, login_email_path1)
    login_email_feild.clear()
    login_email_feild.send_keys('werkinehfikadu@gmail')
    time.sleep(5)
    login_pass_feild = driver.find_element(By.XPATH, login_password_path)
    login_pass_feild.clear()
    login_pass_feild.send_keys('')
    time.sleep(5)
    driver.find_element(By.XPATH, login_button_path).click()
    time.sleep(10)

def login_inc_pass_cor_username():
    # when login facebook by correct username and incorrect password fild

    driver.get(facebook_path)
    driver.maximize_window()
    login_email_feild = driver.find_element(By.XPATH, login_email_path1)
    login_email_feild.clear()
    login_email_feild.send_keys('0533831350')
    time.sleep(5)
    login_pass_feild = driver.find_element(By.XPATH, login_password_path)
    login_pass_feild.clear()
    login_pass_feild.send_keys('fikae22fikae22')
    time.sleep(5)
    driver.find_element(By.XPATH, login_button_path).click()
    time.sleep(10)
    erro_maasege = driver.find_element(By.XPATH, ErrorMassege)
    assert ErrorMassege == erro_maasege
    time.sleep(5)

    # login_inc_pass()

def test_login_inc_pass_and_email():
    # when login facebook by incorrect username and incorrect password fild

    driver.get(facebook_path)
    driver.maximize_window()
    login_email_feild = driver.find_element(By.XPATH, login_email_path1)
    login_email_feild.clear()
    login_email_feild.send_keys('werkinehfikadu')
    time.sleep(5)
    login_pass_feild = driver.find_element(By.XPATH, login_password_path)
    login_pass_feild.clear()
    login_pass_feild.send_keys('fikae22fikae22')
    time.sleep(5)
    driver.find_element(By.XPATH, login_button_path).click()
    time.sleep(10)

def test_login_cor_username_and_empty_password():
    # when login facebook by correct username and empty password fild

    driver.get(facebook_path)
    driver.maximize_window()
    login_email_feild = driver.find_element(By.XPATH, login_email_path1)
    login_email_feild.clear()
    login_email_feild.send_keys(' ')
    time.sleep(5)
    login_pass_feild = driver.find_element(By.XPATH, login_password_path)
    login_pass_feild.clear()
    login_pass_feild.send_keys('')
    time.sleep(5)
    driver.find_element(By.XPATH, login_button_path).click()
    time.sleep(10)

def test_login_correct_pass_and_empty_email():
    # when login facebook by empty username and correct password fild

    driver.get(facebook_path)
    driver.maximize_window()
    login_email_feild = driver.find_element(By.XPATH, login_email_path1)
    login_email_feild.clear()
    login_email_feild.send_keys(' ')
    time.sleep(5)
    login_pass_feild = driver.find_element(By.XPATH, login_password_path)
    login_pass_feild.clear()
    login_pass_feild.send_keys('')
    time.sleep(5)
    driver.find_element(By.XPATH, login_button_path).click()
    time.sleep(10)


