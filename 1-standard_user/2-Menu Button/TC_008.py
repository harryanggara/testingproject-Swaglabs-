from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(10)

driver.find_element(By. ID, "user-name").send_keys("standard_user")
driver.find_element(By. ID, "password").send_keys("secret_sauce")
driver.find_element(By. ID, "login-button").click()
time.sleep(3)
driver.find_element(By. ID, 'shopping_cart_container').click()
time.sleep(3)
driver.find_element(By. ID, "react-burger-menu-btn").click()
time.sleep(3)
driver.find_element(By. ID, 'inventory_sidebar_link').click()