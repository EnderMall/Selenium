from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math

def calc(x): return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "num1")
    x = x_element.get_attribute("textContent")

    z_element = browser.find_element(By.ID, "num2")
    z = z_element.get_attribute("textContent")
    print(z)
    y = int(x)+int(z)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(y))

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()