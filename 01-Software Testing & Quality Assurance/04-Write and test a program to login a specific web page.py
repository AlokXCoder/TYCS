from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Import Service from selenium to handle the ChromeDriver path
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Step 1: Set up Chrome WebDriver (with WebDriver Manager, if you installed it)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Step 2: Navigate to the login page
driver.get("https://practicetestautomation.com/practice-test-login/")

# Step 3: Enter credentials and login
username = "student"
password = "Password123"

# Wait for the username field to be visible and interactable
username_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "username"))
)
username_field.send_keys(username)

# Wait for the password field to be visible and interactable
password_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "password"))
)
password_field.send_keys(password)

# Click the login button programmatically
submit_button = driver.find_element(By.ID, "submit")
submit_button.click()

# Step 4: Wait for the login process to complete
time.sleep(5)  # Wait for 5 seconds to observe the login process

# Optionally, you can check if the login was successful by waiting for a specific element
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "logout")))

# Step 5: Keep the webpage open for 15 seconds after login to demonstrate
time.sleep(15)

# Step 6: Close the browser
driver.quit()
