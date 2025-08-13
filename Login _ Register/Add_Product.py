from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time


driver = webdriver.Chrome()
# Read the JSON file containing product data
with open('product_data.json', 'r') as file:
    product_data = json.load(file)

# Open the login page
driver.get("https://waitermoduleapp.danfesolution.com/login")

# Wait for the login form to load
wait = WebDriverWait(driver, 10)

try:
    # Fill login details
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='p-2 py-4']//input[@placeholder='Enter email']")))
    email.send_keys("admin@momohouse.com")
    time.sleep(2)
    password = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='p-2 py-4']//input[@placeholder='Enter Password']")))
    password.send_keys("Admin@123#")
    time.sleep(2)
    remember_me = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='d-flex justify-content-between mb-4']//input[@id='auth-remember-check']")))
    if not remember_me.is_selected():
        remember_me.click()
    submit = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='p-2 py-4']//button[@type='submit'][normalize-space()='Sign In']")))
    submit.click()
    time.sleep(5)

    # Check if login is successful
    if driver.current_url == "https://waitermoduleapp.danfesolution.com":
        print("Login successful, redirected to dashboard.")
    else:
        print(f"Login failed or redirected to unexpected URL: {driver.current_url}")
        

    # Navigate to Product page (adjust XPath if the link differs)
    wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Product Management']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Products']"))).click()  # Adjust if the link is different
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-success']"))).click()  # Assumes a similar "Add" button
    time.sleep(5)

    # Fill the product form
    wait.until(EC.presence_of_element_located((By.NAME, "name"))).send_keys(product_data["name"])
    wait.until(EC.presence_of_element_located((By.NAME, "slug"))).send_keys(product_data["slug"])
    wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@id='description']"))).send_keys(product_data["description"])
    wait.until(EC.presence_of_element_located((By.NAME, "price"))).send_keys(str(product_data["price"]))
    wait.until(EC.presence_of_element_located((By.NAME, "tags"))).send_keys(product_data["tags"])
    
    # Select Category (assuming a dropdown, adjust selector)
    category_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='css-t3ipsp-control']//div[@class='css-19bb58m']")))
    category_dropdown.click()
    options = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'css-1n6g696-option')]")))
    if options:
        category_index = product_data["categoryId"] if 0 <= product_data["categoryId"] < len(options) else 0
        options[category_index].click()
        print(f"Selected Category at index {category_index}")
    else:
        print("No category options found!")

    # Select Unit (assuming a dropdown, adjust selector)
    unit_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='css-t3ipsp-control']//div[@class='css-19bb58m']")))
    unit_dropdown.click()
    options = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'css-1n6g696-option')]")))
    if options:
        unit_index = product_data["unitId"] if 0 <= product_data["unitId"] < len(options) else 0
        options[unit_index].click()
        print(f"Selected Unit at index {unit_index}")
    else:
        print("No unit options found!")

    # Set Is Hidden and Is Product Sold Out (checkboxes or toggles)
    hide_toggle = wait.until(EC.presence_of_element_located((By.NAME, "isHidden")))
    if product_data["isHidden"] != (hide_toggle.get_attribute("checked") is not None):
        hide_toggle.click()
    sold_out_toggle = wait.until(EC.presence_of_element_located((By.NAME, "isProductSoldOut")))
    if product_data["isProductSoldOut"] != (sold_out_toggle.get_attribute("checked") is not None):
        sold_out_toggle.click()

    # Handle attributes (assuming a dynamic form section to add attributes)
    for attr in product_data["attributes"]:
        add_attribute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add Attribute')]")))  # Adjust XPath
        add_attribute_button.click()
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.NAME, "attributeTitle"))).send_keys(attr["title"])
        wait.until(EC.presence_of_element_located((By.NAME, "attributeValue"))).send_keys(str(attr["value"]))
        active_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "isActive")))
        if attr["isActive"] != active_checkbox.is_selected():
            active_checkbox.click()
        time.sleep(2)

    # Submit the form
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Save']"))).click()
    time.sleep(5)

except Exception as e:
    print(f"An error occurred: {str(e)}")
    print(f"Current URL: {driver.current_url}")
    print(f"Page source: {driver.page_source[:500]}...")  # Print first 500 characters of page source for debugging
finally:
    # Wait to see the result
    time.sleep(2)
    # Close the browser
    driver.quit()