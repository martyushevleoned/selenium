from selenium import webdriver

options = webdriver.ChromeOptions()
driver = webdriver.Chrome('yandexdriver.exe', options=webdriver.ChromeOptions())
driver.get('https://yandex.ru')
# driver.quit()
