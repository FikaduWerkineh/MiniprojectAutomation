import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Atidstore.BaseTest.locators import *
import pytest

driver = webdriver.Chrome()


def test_store_buy_product():
    driver.get("http://www.atid.store/")
    driver.find_element(By.XPATH, store_test).click()

    time.sleep(2)
    driver.find_element(By.XPATH, stor_product).click()

    time.sleep(1)
    driver.find_element(By.XPATH, store_add_cart).click()
    time.sleep(1)
    driver.find_element(By.XPATH, store_view_cart).click()

    time.sleep(1)
    coupon = driver.find_element(By.XPATH, coupon_code)
    coupon.send_keys("true")
    driver.find_element(By.XPATH, applyCoupon).click()


def test_cart_men():
    driver.get("http://www.atid.store/")
    driver.find_element(By.XPATH, test_men).click()

    time.sleep(3)
    driver.find_element(By.XPATH, men_product).click()

    time.sleep(3)
    driver.find_element(By.XPATH, add_men_product).click()
    time.sleep(3)
    driver.find_element(By.XPATH, viw_men_product).click()

    time.sleep(3)
    coupon = driver.find_element(By.NAME, men_coupon)
    coupon.clear()
    coupon.send_keys("hagsy2354")
    time.sleep(2)

    button = driver.find_element(By.XPATH, apply_men_product)
    button.click()


def test_cart_women():
    driver.find_element(By.XPATH, test_women).click()

    time.sleep(3)
    driver.find_element(By.XPATH, women_product).click()

    time.sleep(2)
    driver.find_element(By.XPATH, add_to_cart_women_pro).click()
    time.sleep(2)
    driver.find_element(By.XPATH, view_women_produ_on_cart).click()
    time.sleep(2)

    copoun = driver.find_element(By.XPATH, women_coupon)
    copoun.clear()
    copoun.send_keys("true")
    time.sleep(3)
    driver.find_element(By.XPATH, apply_women_coupon).click()
    time.sleep(3)


def test_cart_accessories():
    driver.find_element(By.XPATH, test_accessory).click()

    time.sleep(3)
    driver.find_element(By.XPATH,accessory_product).click()

    time.sleep(2)
    driver.find_element(By.XPATH, accessory_add_cart).click()
    time.sleep(2)
    driver.find_element(By.XPATH,view_accessory_product_on_cart).click()

    time.sleep(2)

    coupon = driver.find_element(By.XPATH, accessory_coupon)
    coupon.clear()
    coupon.send_keys("true")
    time.sleep(3)
    driver.find_element(By.XPATH, apply_to_buy_accessory_product).click()
    time.sleep(3)
