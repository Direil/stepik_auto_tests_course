from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = " http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element(By.ID, 'treasure').get_attribute("valuex")
    y = calc(treasure)

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    checkbox.click()
    robots = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    robots.click()
    submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    time.sleep(1)
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
