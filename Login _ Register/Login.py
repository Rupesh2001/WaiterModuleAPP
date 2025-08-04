from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

@pytest.fixture(scope="function")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login(driver):
    try:
        driver.get("https://waitermoduleapp.danfesolution.com/login")
        time.sleep(2)  # Consider using WebDriverWait for better stability
        driver.save_screenshot("Pass_login_page.png")
    except Exception as e:
        print(f"Error accessing the website: {e}")
        driver.save_screenshot("Fail_login_page.png")

        