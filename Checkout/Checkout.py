from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import re  # Added to fix the regex issue


@pytest.fixture(scope="function")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_loginValid(driver):
    try:
        driver.get("https://waitermoduleapp.danfesolution.com/login")
        time.sleep(5)

        email = driver.find_element(By.XPATH, "//div[@class='p-2 py-4']//input[@placeholder='Enter email']")
        email.send_keys("admin@momohouse.com")
        time.sleep(2)

        password = driver.find_element(By.XPATH, "//div[@class='p-2 py-4']//input[@placeholder='Enter Password']")
        password.send_keys("Admin@123#")
        time.sleep(2)

        remember_me_checkbox = driver.find_element(By.XPATH, "//div[@class='d-flex justify-content-between mb-4']//input[@id='auth-remember-check']")
        if not remember_me_checkbox.is_selected():
            remember_me_checkbox.click()

        submit = driver.find_element(By.XPATH, "//div[@class='p-2 py-4']//button[@type='submit'][normalize-space()='Sign In']")
        submit.click()
        time.sleep(5)

        if driver.current_url == "https://waitermoduleapp.danfesolution.com/dashboard":
            print("Login successful, redirected to dashboard.")
            time.sleep(5)

            # Open POS
            driver.find_element(By.XPATH, "//button[normalize-space()='POS']").click()
            time.sleep(3)

            if driver.current_url == "https://waitermoduleapp.danfesolution.com/pos":
                print("POS page loaded successfully.")
                time.sleep(3)

                # Select Section and Table
                driver.find_element(By.XPATH, "//div[@class='table-grid-wrapper']//div[2]//div[1]//div[1]//div[1]//i[1]").click()
                time.sleep(3)
                driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[4]/div[2]/div/div[5]").click()
                time.sleep(3)
                driver.find_element(By.XPATH, "//button[normalize-space()='Continue']").click()
                time.sleep(3)

                # Optional: Capture table name (if needed)
                Tableselect = driver.find_element(By.XPATH, "//div[contains(@class,'table-card table-available table-capacity-2')]").text
                print("Selected Table:", Tableselect)

                # Add item to order
                driver.find_element(By.XPATH, "//div[contains(@class,'gx-3 gy-4 mb-3 row')]//div[2]//div[1]//div[1]//div[1]//img[1]").click()
                driver.find_element(By.XPATH, "//button[normalize-space()='Add to Order']").click()
                time.sleep(2)

                # Update and process order
                driver.find_element(By.XPATH, "//button[normalize-space()='Update Order']").click()
                time.sleep(2)
                driver.find_element(By.XPATH, "//button[normalize-space()='Process Transaction']").click()
                time.sleep(3)

                # Get amount text
                amt_text = driver.find_element(By.XPATH, "//div[@class='col-12 order-1 col-lg-5 order-lg-2 col-xl-6 order-xl-2']//div[6]//span[1]").text
                amt_number = re.sub(r'[^\d.]', '', amt_text)
                print("Amount to pay:", amt_number)
                time.sleep(2)

                # Click Cash button
                driver.find_element(By.XPATH, "//div[@id='offcanvasRight']//div[6]//button[1]").click()
                time.sleep(2)

                # Enter cash amount
                cash_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter Amount']")
                cash_input.clear()
                cash_input.send_keys(amt_number)
                time.sleep(2)

                # Confirm transaction
                driver.find_element(By.XPATH, "//div[@class='p-3 rounded-3 border-2 shadow-sm bg-white d-flex justify-content-between sticky-bottom align-items-center']//button[@type='button'][normalize-space()='Confirm']").click()

                print("Transaction confirmed successfully.")

            else:
                print("Failed to load POS page.")

        else:
            print("Login failed, not redirected to dashboard.")

    except Exception as e:
        print(f"Error accessing the website: {e}")
