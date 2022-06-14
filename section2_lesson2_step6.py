from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = " http://SunInJuly.github.io/execute_script.html"

try:
  browser = webdriver.Chrome()
  browser.get(link)

  x = browser.find_element(By.ID, 'input_value').text
  y = calc(x)


  time.sleep(1)
  answer = browser.find_element(By.CSS_SELECTOR, "#answer")
  answer.send_keys(y)
  checkbox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
  browser.execute_script('return arguments[0].scrollIntoView(true);', checkbox)
  # checkbox.location_once_scrolled_into_view
  checkbox.click()
  robots = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
  robots.click()
  submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn')
  submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

не забываем оставить пустую строку в конце файла
