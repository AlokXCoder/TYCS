# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the WebDriver (using Chrome in this example)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Open the Python website
    driver.get("http://www.python.org")
    
    # Find the search box element by its name attribute
    search_box = driver.find_element(By.NAME, "q")
    
    # Type "lambda" into the search box
    search_box.send_keys("lambda")
    
    # Press the Enter key
    search_box.send_keys(Keys.RETURN)
    
    # Wait for a few seconds to see the results
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
