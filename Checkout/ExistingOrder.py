import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Checkout1 import driver, login, go_to_pos
import time
from webcolors import rgb_to_hex
import re

def ExistingOrder(driver):
    print("Existing Order Function Called")
    section = driver.find_element(By.XPATH,"//div[@id='offcanvasRight']//div[3]//div[1]//div[1]//div[1]")
    section.click()
    table = driver.find_element(By.XPATH,"//div[contains(@class,'table-card table-occupied table-capacity-12')]")
    table.click()
    time.sleep(3)
    background_color = table.value_of_css_property("background-color")
    # Check if the background color is red (in rgb format, e.g., 'rgb(255, 0, 0)')
    print("background color:", background_color)
    match = re.search(r'rgba?\((\d+),\s*(\d+),\s*(\d+)', background_color)
    if match:
        r, g, b = map(int, match.groups())
        hex_color = rgb_to_hex((r, g, b))
        print("Background color (Hex):", hex_color)
        return hex_color
    else:
        print("⚠️ Could not parse RGB color:", background_color)
    if hex_color.lower() == '#fee2e2':
        print("✅ The background color is red.")
    elif hex_color:
        print("❌ The background color is NOT red.")
def test_existing_order(driver):
    try:
        login(driver, "admin@momohouse.com", "Admin@123#")
        go_to_pos(driver)
        ExistingOrder(driver)
    except Exception as e:
        print(f"❌ Test failed due to: {e}")
        assert False