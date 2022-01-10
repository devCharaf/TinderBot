from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import os

URL = "https://tinder.com/"
FB_EMAIL = os.environ['MY_EMAIL']
FB_PASSWORD = os.environ['MY_PASSWORD']

chrome_driver_path = os.environ['MY_DRIVER']

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)

time.sleep(3)
login_button = driver.find_element(By.LINK_TEXT, "Log in")
login_button.click()

time.sleep(3)
fb_button = driver.find_element(By.XPATH, '//*[@id="o-1335420887"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_button.click()

time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(2)
# sign in to facebook
email = driver.find_element(By.XPATH, '//*[@id="email"]')
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

# Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)

time.sleep(10)
print("done")

# Delay by 5 seconds to allow page to load.
time.sleep(3)

# Allow location
allow_location_button = driver.find_element(By.XPATH, '//*[@id="o-1335420887"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

# Disallow notifications
notifications_button = driver.find_element(By.XPATH, '//*[@id="o-1335420887"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

# Allow cookies
cookies = driver.find_element(By.XPATH, '//*[@id="o-1556761323"]/div/div[2]/div/div/div[1]/button')
cookies.click()

time.sleep(10)
# swipe
for n in range(100):

    # Add a 1 second delay between likes.
    time.sleep(1)

    try:
        print("called")
        if n == 0:
            like_button = driver.find_element(By.XPATH,
                                              '//*[@id="o-1556761323"]/div/div[1]/div/main/div[1]/div/div/div[1]/div['
                                              '1]/div/div[4]/div/div[4]/button/span/span')
        else:
            like_button = driver.find_element(By.XPATH,
                                              '//*[@id="o-1556761323"]/div/div[1]/div/main/div[1]/div/div/div[1]/div['
                                              '1]/div/div[5]/div/div[4]/button/span/span')
        like_button.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()

driver.quit()
