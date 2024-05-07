#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Standard Library Imports
import math
import time

# Web Automation Imports
from selenium import webdriver
from selenium.webdriver.common.by import By

# HTTP Requests Imports
import requests

# Record the start time
start_time = time.time()

# Initialize WebDriver (assuming Chrome)
driver = webdriver.Chrome()

driver.get("https://www.random.org/bytes/")
driver.maximize_window()

radio_button = driver.find_element(By.XPATH, "//input[@type='radio' and @value='b']")
radio_button.click()

text_input = driver.find_element(By.XPATH, "//input[@type='text' and @value='10']")
text_input.clear()
text_input.send_keys("13")

button_click = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Get Bytes']")
button_click.click()

byte = driver.find_element(By.XPATH, "//pre").text
print(f"\nString: \n{byte}")

byte = ''.join(byte.split())
print(f"\nFormatted string: \n{byte}")

# Remove last four elements
byte = byte[:-4]
print(f"\nFormatted and adjusted string: \n{byte}")

ones = byte.count("1")
print(f"\nCount of ones: \n{ones}")
      
zeros = byte.count("0")
print(f"\nCount of zeros: \n{zeros}")
      
sn = abs(zeros - ones)
print(f"\nAbsolute difference between groups: \n{sn}")
      
sobs = sn/math.sqrt(len(byte))
print(f"\nSobs: \n{sobs}")
      
number = sobs/math.sqrt(2)
print(f"\nNumber: \n{number}")

driver.get("https://www.miniwebtool.com/complementary-error-function-calculator/?number=" + str(number))

# Extract the result from the <div> tag with the id "calculatorresult"
result = driver.find_element(By.XPATH, "//div[@id='calculatorresult']").text
print(f"\n{result}")

# Close the web driver
driver.quit()

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time
print("\nElapsed time:", elapsed_time, "seconds")

