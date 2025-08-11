from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

# Set up the WebDriver (ensure ChromeDriver is installed and in PATH)
driver = webdriver.Chrome()

# Read the JSON file
with open('category_data.json', 'r') as file:
    data = json.load(file)

# Open the category form page
driver.get("https://waitermoduleapp.danfesolution.com/login")
email = driver.find_element(By.XPATH,"//div[@class='p-2 py-4']//input[@placeholder='Enter email']")
email.send_keys("admin@momohouse.com")
time.sleep(2)
password = driver.find_element(By.XPATH,"//div[@class='p-2 py-4']//input[@placeholder='Enter Password']")
password.send_keys("Admin@123#")
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
# Wait for the form to load
wait = WebDriverWait(driver, 10)

#go to the category page
wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Product Management']"))).click()
wait.until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Category']"))).click()
wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-success']"))).click()
# Fill the form
time.sleep(5)
wait.until(EC.presence_of_element_located((By.NAME, "name"))).send_keys(data["name"])
wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@id='description']"))).send_keys(data["description"])
time.sleep(5)
# Select Parent Category (assuming it's a dropdown, adjust selector if needed)
#parent_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='css-t3ipsp-control']//div[@class='css-19bb58m']")))
'''
cost_center_dropdown = wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]"))).click()
options = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'css-') and contains(@class,'option')]"))
)

#  Select the first option
if options:
    options[0].click()
else:
    print("No dropdown options found!")

'''
# Note: Selecting a specific option requires the option value or text, e.g., driver.find_element(By.XPATH, "//option[@value='someValue']").click()
#time.sleep(5)
# Fill Category Position
wait.until(EC.presence_of_element_located((By.NAME, "categoryPosition"))).clear()
wait.until(EC.presence_of_element_located((By.NAME, "categoryPosition"))).send_keys(data["categoryPosition"])
time.sleep(5)
# Select Cost Center (assuming it's a dropdown, adjust selector if needed)
cost_center_dropdown = wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]"))).click()
options = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'css-') and contains(@class,'option')]"))
)

# Select the first option
if options:
    options[data[ "costCenterId"]].click()
else:
    print("No dropdown options found!")
# Note: Selecting a specific option requires the option value or text, e.g., driver.find_element(By.XPATH, "//option[@value='" + str(data["costCenterId"]) + "']").click()

# Set Active Status (checkbox)
active_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "isActive")))
if data["isActive"] != active_checkbox.is_selected():
    active_checkbox.click()
time.sleep(5)
# Set Hide Status (toggle, adjust selector if needed)
hide_toggle = wait.until(EC.presence_of_element_located((By.NAME, "isHidden")))
if data["isHidden"] != (hide_toggle.get_attribute("checked") is not None):
    hide_toggle.click()
time.sleep(5)
# Submit the form
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Save']"))).click()
time.sleep(5)
# Wait to see the result
time.sleep(2)

# Close the browser
driver.quit()