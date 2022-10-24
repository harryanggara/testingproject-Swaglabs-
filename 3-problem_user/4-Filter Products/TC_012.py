from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

driver.find_element(By. ID, "user-name").send_keys("problem_user")
driver.find_element(By. ID, "password").send_keys("secret_sauce")
driver.find_element(By. ID, "login-button").click()

driver.find_element(By.CLASS_NAME, 'product_sort_container').click()
selectAZ = Select(driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div[2]/span/select'))

time.sleep(2)
selectAZ.select_by_value('hilo')
time.sleep(2)