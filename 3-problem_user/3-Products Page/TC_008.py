from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

driver.find_element(By. ID, "user-name").send_keys("problem_user")
driver.find_element(By. ID, "password").send_keys("secret_sauce")
driver.find_element(By. ID, "login-button").click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').click()
time.sleep(3)
driver.find_element(By.ID, "back-to-products").click()