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

@pytest.mark.parametrize("username, password", [
    ("test", "test"),
])

def test_login(setup, username, password):
    setup.get("https://trytestingthis.netlify.app/")
    setup.find_element(By.ID, "uname").send_keys(username)
    setup.find_element(By.ID, "pwd").send_keys(password)
    time.sleep(5)
    setup.find_element(By.XPATH, "//input[@value='Login']").click()
    assert "Successful" in setup.page_source
    time.sleep(3)