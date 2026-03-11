import math
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


@pytest.mark.parametrize("link", links)
def test_alien_message(browser, link):
    wait = WebDriverWait(browser, 20)
    browser.get(link)

    # --- ЛОГИН ---
    login_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth_login"))
    )
    login_btn.click()

    email = wait.until(
        EC.visibility_of_element_located((By.ID, "id_login_email"))
    )
    email.send_keys("karceva631@gmail.com")

    password = browser.find_element(By.ID, "id_login_password")
    password.send_keys("13113105Love")

    browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()

    # ждём пока появится поле ответа
    textarea = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.textarea"))
    )

    textarea.clear()

    # ⚠ ВАЖНО — считаем ответ ПРЯМО ПЕРЕД вводом
    answer = str(math.log(int(time.time())))
    textarea.send_keys(answer)

    # ждём активную кнопку
    submit_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
    )
    submit_btn.click()

    # ждём появления фидбека
    feedback = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    )

    feedback_text = feedback.text

    assert feedback_text == "Correct!", f"\nAlien message: {feedback_text}\n"