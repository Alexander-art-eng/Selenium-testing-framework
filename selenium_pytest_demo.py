import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--no-sandbox")  # Prevent issues with sandboxing in CI
    options.add_argument("--disable-dev-shm-usage")  # Address shared memory issues in CI

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_form_submission(driver):
    driver.get("https://trytestingthis.netlify.app/")
    driver.find_element(By.ID, "fname").send_keys("Alexander")
    driver.find_element(By.ID, "lname").send_keys("Tesfay")
    time.sleep(3)
    print("Test Completed")