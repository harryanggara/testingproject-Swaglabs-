from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("problem_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(2)
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
time.sleep(2)
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
time.sleep(2)
driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
time.sleep(2)
driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
time.sleep(2)
driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()