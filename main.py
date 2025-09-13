from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[logging.FileHandler("farmers.txt", encoding="utf-8")]
)

file_path = f"https://sadovnik.mobi/"

driver = webdriver.Chrome()
driver.get(file_path)

input_login = driver.find_element(By.NAME, "login")
input_password = driver.find_element(By.NAME, "password")
input_submit = driver.find_element(By.CSS_SELECTOR, "input[value='Вход']")

input_login.send_keys("Hot Blood")
input_password.send_keys("lg0000i")
input_submit.click()

time.sleep(1)

for i in range(49):
    driver.get(f"https://sadovnik.mobi/rating?page={i}")
    list_farmers = driver.find_elements(By.CSS_SELECTOR, "div.block ul:first-child li")
    for index, farmer in enumerate(list_farmers, start=1):
        farmer_name = farmer.find_element(By.TAG_NAME, "a").text
        logging.info(f"{farmer_name}")

time.sleep(3)

# закрываем браузер
driver.quit()