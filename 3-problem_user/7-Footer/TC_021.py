from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

driver.find_element(By. ID, "user-name").send_keys("problem_user")
driver.find_element(By. ID, "password").send_keys("secret_sauce")
driver.find_element(By. ID, "login-button").click()
time.sleep(5)

driver.find_element(By.CLASS_NAME, 'social_linkedin').click()
time.sleep(2)
driver._switch_to.window(driver.window_handles[1])