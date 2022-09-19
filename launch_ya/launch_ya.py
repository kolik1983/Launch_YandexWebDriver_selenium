import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


options = Options()
service = Service("chromedriver.exe")
options.binary_location = "C:/Users/erigo/AppData/Local/Yandex/YandexBrowser/Application/browser.exe"
driver = webdriver.Chrome(options=options, service=service)
driver.get('http://mail.ru/')
driver.quit()
