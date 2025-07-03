from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import openpyxl
import os

# Step 1: Set up Chrome options to handle SSL/TLS errors (optional)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

# Step 2: Set up the ChromeDriver using Service
service = Service(ChromeDriverManager().install())  # Specify the driver path

# Step 3: Launch the web browser with options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Step 4: Navigate to the webpage with the student table
driver.get("https://www.w3schools.com/html/html_tables.asp")  # Replace with the actual URL

# Step 5: Scrape data from the table
table_data = []
headers = ["Company Name", "Owner", "Country"]

try:
    rows = driver.find_elements(By.XPATH, "//table//tr")  # Locate table rows
    for row in rows[1:]:  # Skip header row
        columns = row.find_elements(By.TAG_NAME, "td")
        if columns:
            student_name = columns[0].text.strip()
            subject = columns[1].text.strip()
            grade = columns[2].text.strip()
            table_data.append([student_name, subject, grade])

except Exception as e:
    print(f"Error while scraping table data: {e}")

# Step 6: Specify the file path to save the Excel file in your "Downloads" directory
file_name = "RealEstate_record_data.xlsx"
file_path = os.path.join(os.path.expanduser("~"), "Downloads", file_name)

# Step 7: Create a new Excel workbook and worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active

# Step 8: Write the table data to the Excel worksheet
worksheet.append(headers)  # Write headers
for row in table_data:
    worksheet.append(row)

# Step 9: Save the Excel file to your "Downloads" directory
workbook.save(file_path)

# Step 10: Print the table data to the console
print("Table Data:")
print('\t'.join(headers))  # Print headers
for row in table_data:
    print('\t'.join(map(str, row)))  # Convert each element to string and print

# Step 11: Close the browser and cleanup
driver.quit()

# Step 12: Print success message with file path
print(f"Excel file saved successfully to: {file_path}")
