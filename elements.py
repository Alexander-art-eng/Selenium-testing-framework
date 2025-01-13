# This script uses Selenium WebDriver to automate the Chrome browser.
# It installs the ChromeDriver using the webdriver_manager package,
# which ensures that the correct version of ChromeDriver is downloaded and used.
# The ChromeDriver is then used to create a new instance of the Chrome browser.
# The script navigates to Google, searches for "Selenium WebDriver", and clicks the search button.

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("https://www.google.com")
# time.sleep(2)
# cookies = driver.find_element(By.ID, "W0wltc")
# cookies.click()
# googleSearchBox = driver.find_element(By.ID, "APjFqb")
# googleSearchBox.send_keys("Selenium WebDriver")
#
# # Wait for the search button to be clickable
# search_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.NAME, "btnK"))
# )
# search_button.send_keys(Keys.RETURN)

driver.get("https://trytestingthis.netlify.app/")
driver.find_element(By.ID, "fname").send_keys("Alexander")
driver.find_element(By.ID, "lname").send_keys("Tesfay")
time.sleep(3)
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
time.sleep(3)
driver.quit()