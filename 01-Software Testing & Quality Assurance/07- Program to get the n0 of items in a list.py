from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 1: Launch the web browser and navigate to the webpage
driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH or specify the path to the driver
driver.implicitly_wait(5)  # Set an implicit wait time of 5 seconds for loading elements

# Step 2: Open the target webpage
driver.get("https://www.tutorialspoint.com/about/about_careers.htm")

# Step 3: Identify elements with the class attribute "chapters"
l = driver.find_elements(By.CLASS_NAME, "chapters")  # Find all elements with the class "chapters"

# Step 4: Count the number of elements found
s = len(l)  # The length of the list 'l' will give the number of elements

# Step 5: Print the count of elements
print('Count is:')
print(s)  # Print the count of elements

# Step 6: Close the browser after the task is done
driver.quit()  # This closes the browser
