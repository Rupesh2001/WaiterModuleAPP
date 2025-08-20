from Checkout1 import driver, login, go_to_pos, select_table, add_item_to_order
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import time
def CancelOrder(driver):
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='align-items-center row']"))).click()
    time.sleep(3)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel Selected Order (1)']"))).click()
    time.sleep(3)
    txtbox = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//textarea[@id='remarks']")))
    txtbox.click()
    txtbox.send_keys("Cancelled")
    time.sleep(3)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Yes, Confirm']"))).click()
    toggle = driver.find_element(By.XPATH, "//div[@role='status']")
    print("✅ Order cancelled successfully.")

def test_Cancel_order(driver):
    try:
        login(driver, "admin@momohouse.com", "Admin@123#")
        go_to_pos(driver)
        select_table(driver)
        add_item_to_order(driver)
        CancelOrder(driver)
    except Exception as e:
        print(f"❌ Test failed due to: {e}")
        assert False