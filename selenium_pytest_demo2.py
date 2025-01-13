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
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--no-sandbox")  # Prevent issues with sandboxing in CI
    options.add_argument("--disable-dev-shm-usage")  # Address shared memory issues in CI

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

@pytest.mark.parametrize("username, password", [
    ("test", "test"),
])

def test_login(driver, username, password):
    driver.get("https://trytestingthis.netlify.app/")
    driver.find_element(By.ID, "uname").send_keys(username)
    driver.find_element(By.ID, "pwd").send_keys(password)
    time.sleep(5)
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    assert "Successful" in driver.page_source
    time.sleep(3)