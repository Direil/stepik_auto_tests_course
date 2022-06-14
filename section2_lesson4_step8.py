from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import math
import pyperclip

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/explicit_wait2.html"
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

try:
	browser = webdriver.Chrome(options=chrome_options)
	browser.get(link)
	price = WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5#price'), '$100'))
	print('yeah')
	button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, 'book')))
	button.click()
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

