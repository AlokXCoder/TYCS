from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Step 1: Create a new instance of the Chrome WebDriver using webdriver_manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Maximize the browser window
driver.maximize_window()

# Step 2: Open the URL
driver.get("https://en.wikipedia.org/wiki/Marvel_Cinematic_Universe")

# Step 3: Refresh the browser (optional)
driver.refresh()

# Step 4: Find all checkboxes on the web page using XPATH
elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//input[@type='checkbox']"))
)

# Step 5: Check if checkboxes were found
if elements:
    print(f"Number of checkboxes found: {len(elements)}")
    
    # Count checked and unchecked checkboxes
    checked_count = 0
    unchecked_count = 0

    for element in elements:
        if element.is_selected():  # Check if the checkbox is checked
            checked_count += 1
        else:
            unchecked_count += 1

    print(f"Number of checked checkboxes: {checked_count}")
    print(f"Number of unchecked checkboxes: {unchecked_count}")
else:
    print("No checkboxes found on the web page.")

# Step 6: Close the browser
driver.quit()
