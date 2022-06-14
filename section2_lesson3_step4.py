from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math
import pyperclip

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	button = browser.find_element(By.TAG_NAME, "button")
	button.click()
	confirm = browser.switch_to.alert
	print(confirm.text)
	time.sleep(1)
	confirm.accept()
	x = browser.find_element(By.ID, 'input_value').text
	y = calc(x)
	answer = browser.find_element(By.ID, 'answer').send_keys(y)
	submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
	time.sleep(1)
	alert = browser.switch_to.alert
	alert_text = alert.text.split(':')[-1]
	copy = pyperclip.copy(alert_text)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

