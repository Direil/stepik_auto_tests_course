from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    n1 = browser.find_element(By.ID, 'num1').text
    n2 = browser.find_element(By.ID, 'num2').text
    okay = int(n1) + int(n2)

    dropdwn = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    dropdwn.select_by_value(str(okay))
    submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
