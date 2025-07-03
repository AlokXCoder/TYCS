from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Launch the web browser and navigate to the web page
driver = webdriver.Chrome()  # Make sure the path to chromedriver is in your PATH or specify the path here.
driver.get("https://www.marvel.com/")

# Step 2: Wait for elements to become available (adjust the timeout as needed)
wait = WebDriverWait(driver, 10)
elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*")))  # XPath for all elements

# Step 3: Count the total number of elements
total_elements = len(elements)

# Step 4: Print the total count
print(f"Total number of objects on the web page: {total_elements}")

# Step 5: Close the browser
driver.quit()
