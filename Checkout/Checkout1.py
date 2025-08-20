import pytest
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# -------------------- FUNCTION DEFINITIONS --------------------

def login(driver, email_str, password_str):
    driver.get("https://waitermoduleapp.danfesolution.com/login")
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys(email_str)
    driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys(password_str)

    remember_me = driver.find_element(By.ID, "auth-remember-check")
    if not remember_me.is_selected():
        remember_me.click()

    driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()
    time.sleep(4)

    assert driver.current_url == "https://waitermoduleapp.danfesolution.com/dashboard", "Login failed!"
    print("✅ Login successful.")

def go_to_pos(driver):
    driver.find_element(By.XPATH, "//button[normalize-space()='POS']").click()
    time.sleep(3)
    assert driver.current_url == "https://waitermoduleapp.danfesolution.com/pos", "POS page not loaded."
    print("✅ POS page loaded.")

def select_table(driver):
    driver.find_element(By.XPATH, "//div[@class='table-grid-wrapper']//div[2]//div[1]//div[1]//div[1]//i[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[4]/div[2]/div/div[5]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[normalize-space()='Continue']").click()
    time.sleep(2)
    print("✅ Table selected.")

def add_item_to_order(driver):
    # itemclick
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div/div/div[3]/div[2]/div/div").click()
    driver.find_element(By.XPATH, "//button[normalize-space()='Add to Order']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[normalize-space()='Place Order']").click()
    time.sleep(1)
    print("✅ Item added and order updated.")

def process_transaction(driver):
    driver.find_element(By.XPATH, "//button[normalize-space()='Process Transaction']").click()
    time.sleep(3)

    amt_text = driver.find_element(By.XPATH, "//div[@class='col-12 order-1 col-lg-5 order-lg-2 col-xl-6 order-xl-2']//div[6]//span[1]").text
    amt_number = re.sub(r'[^\d.]', '', amt_text)
    print(f"Amount to pay: {amt_number}")

    driver.find_element(By.XPATH, "//div[@id='offcanvasRight']//div[6]//button[1]").click()
    time.sleep(2)
    

    # Locate the input field
    cash_input = driver.find_element(By.XPATH, "//input[@placeholder='Amount']")
    cash_input.click()
      # clear any existing value

    # Type each character individually to simulate real key presses
    for char in str(amt_number):
        cash_input.send_keys(char)
        time.sleep(0.1)  # optional: small delay to mimic real typing

    driver.find_element(By.XPATH, "//div[@class='p-3 rounded-3 border-2 shadow-sm bg-white d-flex justify-content-between sticky-bottom align-items-center']//button[@type='button'][normalize-space()='Confirm']").click()
    print("✅ Transaction confirmed.")

# -------------------- MAIN TEST CASE --------------------

def test_order_flow(driver):
    try:
        login(driver, "admin@momohouse.com", "Admin@123#")
        go_to_pos(driver)
        select_table(driver)
        add_item_to_order(driver)
        process_transaction(driver)
    except Exception as e:
        print(f"❌ Test failed due to: {e}")
        assert False
