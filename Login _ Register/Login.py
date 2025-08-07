from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import faker
from faker import Faker

@pytest.fixture(scope="function")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_login(driver):
    try:
        driver.get("https://waitermoduleapp.danfesolution.com/login")
        time.sleep(5)
        faker = Faker()
        email = driver.find_element(By.XPATH,"//div[@class='p-2 py-4']//input[@placeholder='Enter email']")
        email.send_keys(faker.email())
        time.sleep(2)
        password = driver.find_element(By.XPATH,"//div[@class='p-2 py-4']//input[@placeholder='Enter Password']")
        password.send_keys(faker.password())
        time.sleep(2)
        Remember_me = driver.find_element(By.XPATH,"//div[@class='d-flex justify-content-between mb-4']//input[@id='auth-remember-check']")
        remember_me = Remember_me.is_selected()
        if not remember_me:
            Remember_me.click()
        submit = driver.find_element(By.XPATH,"//div[@class='p-2 py-4']//button[@type='submit'][normalize-space()='Sign In']")
        submit.click()
        time.sleep(5)
        if driver.current_url == "https://waitermoduleapp.danfesolution.com/pos":
            print("Login successful, redirected to dashboard.")
        else:
            print("Login failed, not redirected to dashboard.")

    except Exception as e:
        print(f"Error accessing the website: {e}")
        # driver.save_screenshot("Fail_login_page.png")
def test_loginValid(driver):
    try:
        driver.get("https://waitermoduleapp.danfesolution.com/login")
        time.sleep(5)
        faker = Faker()
        email = driver.find_element(By.XPATH,"//div[@class='p-2 py-4']//input[@placeholder='Enter email']")
        email.send_keys("Validemail")
        time.sleep(2)
        password = driver.find_element(By.XPATH,"//div[@class='p-2 py-4']//input[@placeholder='Enter Password']")
        password.send_keys("Validpassword")
        time.sleep(2)
        Remember_me = driver.find_element(By.XPATH,"//div[@class='d-flex justify-content-between mb-4']//input[@id='auth-remember-check']")
        remember_me = Remember_me.is_selected()
        if not remember_me:
            Remember_me.click()
        submit = driver.find_element(By.XPATH,"//div[@class='p-2 py-4']//button[@type='submit'][normalize-space()='Sign In']")
        submit.click()
        time.sleep(5)
        if driver.current_url == "https://waitermoduleapp.danfesolution.com/pos":
            print("Login successful, redirected to dashboard.")
        

    except Exception as e:
        print(f"Error accessing the website: {e}")
        