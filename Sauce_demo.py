from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


# Set options for not prompting DevTools information
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

print("Testing started")
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
sleep(3)

# Get page title
title = driver.title

# Test if title is correct
assert "Swag Labs" in title
print("TEST 0: Test Passed")

# Task 3: Extract the entire contents of the webpage
page_source = driver.page_source

# Save the page source to a text file
file_name = "webpage_task_11.txt"
with open(file_name, 'w', encoding='utf-8') as f:
    f.write(page_source)
    print(f"Page source saved to '{file_name}'")

# Close the driver
driver.quit()
