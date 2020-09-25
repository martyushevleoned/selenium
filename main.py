from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from time import sleep

print('enter video name')
request = input()

print('enter time')
time = int(input())

# waiting
while int(datetime.now().strftime("%H%M")) < time:
    print('waiting...')
    sleep(10)

# drivers
# driver = webdriver.Firefox()
# driver = webdriver.Chrome()
driver = webdriver.Chrome('yandexdriver.exe', options=webdriver.ChromeOptions())

# find video
wait = WebDriverWait(driver, 3)
driver.get('https://www.youtube.com/results?search_query={}'.format(request))
wait.until(EC.visibility_of_element_located((By.ID, "video-title")))
driver.find_element_by_id("video-title").click()

sleep(5)

# full screen
f = driver.find_element_by_class_name('ytp-fullscreen-button')
f.click()
print('full screen')
