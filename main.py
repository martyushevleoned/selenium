from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from time import sleep

request = input()
# request = 'jerk ıt out cat'
time = int(input())
# time = 50

while int(datetime.now().strftime("%H%M")) < time:
    print('loading...')
    sleep(10)

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located
driver.get('https://www.youtube.com/results?search_query={}'.format(request))
wait.until(visible((By.ID, "video-title")))
driver.find_element_by_id("video-title").click()

sleep(5)
ad = driver.find_element_by_class_name('ytp-ad-text')
try:
    while ad.is_displayed() is True:
        sleep(1)
except Exception as e:
    print('done')

f = driver.find_element_by_class_name('ytp-fullscreen-button')
f.click()

timer = driver.find_element_by_class_name('ytp-play-progress')

while True:
    sleep(30)
    timer.click()
