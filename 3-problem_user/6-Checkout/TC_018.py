from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

driver.find_element(By. ID, "user-name").send_keys("problem_user")
driver.find_element(By. ID, "password").send_keys("secret_sauce")
driver.find_element(By. ID, "login-button").click()
time.sleep(2)
driver.find_element(By. ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(2)
driver.find_element(By. ID, "shopping_cart_container").click()
time.sleep(2)
driver.find_element(By. ID, "checkout").click()
time.sleep(2)
driver.find_element(By. ID, "first-name").send_keys("coba")
time.sleep(2)
driver.find_element(By. ID, "last-name").send_keys("test")
time.sleep(2)
driver.find_element(By. ID, "postal-code").send_keys("074201")
time.sleep(2)
driver.find_element(By. ID, "continue").click()
time.sleep(2)
driver.find_element(By. ID, "finish").click()
time.sleep(2)
driver.find_element(By. ID, "back-to-products").click()