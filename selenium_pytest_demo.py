import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_form_submission(setup):
    setup.get("https://trytestingthis.netlify.app/")
    setup.find_element(By.ID, "fname").send_keys("Alexander")
    time.sleep(3)
    print("Test Completed")