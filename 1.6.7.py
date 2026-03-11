from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")

    elements = browser.find_elements(By.CSS_SELECTOR, "input[required]")
    for element in elements:
        element.send_keys("1")

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла
