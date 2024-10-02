import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# List of User-Agent strings
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1"
    # Add more User-Agent strings as needed
]

# Set up Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")

# Choose a random User-Agent from the list
random_user_agent = random.choice(user_agents)
chrome_options.add_argument(f"--user-agent={random_user_agent}")

# Create a new instance of ChromeDriver with the desired options
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.seleniumhq.org/download/")

time.sleep(5)

# Get user Agent with execute_script
driver_ua = driver.execute_script("return navigator.userAgent")
print("User agent:")
print(driver_ua)

# Close the driver
driver.quit()
