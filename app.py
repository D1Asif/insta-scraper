from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

def main():
    driver = webdriver.Chrome()
    url = "https://www.instagram.com/accounts/login/"

    # visit insta login page
    driver.get(url)

    # target the username and password field
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    # enter the fields
    username.clear()
    username.send_keys(os.getenv("INSTA_USERNAME"))
    password.clear()
    password.send_keys(os.getenv("INSTA_PASSWORD"))

    # target the button
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    button.click()
    print("Clicked login button")

    # After successful login a box appears asking whether user wants to save login. Need to click the not now button here. Then a pop up for turning on notification comes. Need to click not now here as well.

    # target and click not now button of save login
    buttons = driver.find_elements(By.CSS_SELECTOR, "div[role='button']")
    for button in buttons:
        if button.get_attribute("innerHTML") == "Not now":
            button.click()
            print("clicked not now button for save login")
            break

    time.sleep(5)
    # target not now button for turn on notification
    buttons = driver.find_elements(By.CSS_SELECTOR, "button")
    for button in buttons:
        if button.get_attribute("innerHTML") == "Not Now":
            button.click()
            print("clicked not now button for notification")
            break
        
    time.sleep(5)

    # Click the search icon to open the search box
    search_icon = driver.find_element(By.CSS_SELECTOR, "svg[aria-label='Search']")
    search_icon.click()

    time.sleep(5)
    # target the search input write the search term and press enter
    search_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")
    search_input.clear()
    keyword="cat"
    search_input.send_keys(f"#{keyword}")

    time.sleep(5)

    search_input.send_keys(Keys.DOWN)
    time.sleep(5)
    first_item = driver.find_element(By.XPATH, "//a[contains(@href, '/explore/tags')]")
    first_item.click()

    print("Showing search result")

    time.sleep(5)

    driver.execute_script("window.scroll(0, 4000)")

    time.sleep(5)

    images = driver.find_elements(By.TAG_NAME, "img")
    image_urls = [{"Image Url" : image.get_attribute("src")} for image in images]
    result = image_urls[2:]

    df = pd.DataFrame(data=result, columns=["Image Url"])
    df.to_csv("insta_scraped_image_urls.csv", index=False)

    # print(image_urls)

    time.sleep(5)
    driver.close()

if __name__ == "__main__":
    main()
    
    

