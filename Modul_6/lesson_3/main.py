from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Открываем страницу входа на сайт
driver.get("https://brainapps.ru/signin")

time.sleep(5)

# Вводим логин
enter_point = driver.find_element(By.ID, 'username')
enter_point.click()
enter_point.send_keys('p636341@gmail.com')

time.sleep(3)

# Нажимаем кнопку продолжения
enter_button = driver.find_element(By.ID, 'continueWithEmailButton')
enter_button.click()

time.sleep(3)

# Вводим пароль
enter_password = driver.find_element(By.ID, 'userpass')
enter_password.click()
enter_password.send_keys('Faraon77!')

time.sleep(3)

# Нажимаем кнопку входа
enter_entry = driver.find_element(By.ID, 'continueWithPasswordButton')
enter_entry.click()

time.sleep(3)

# Находим и нажимаем кнопку "Пройти тест"
enter_test = driver.find_element(By.CSS_SELECTOR, 'a.customBtn--large.customBtn--green')
enter_test.click()

time.sleep(3)

# Прокручиваем страницу вниз
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(3)

# Находим ссылку "О проекте" и кликаем по ней
enter_link = driver.find_element(By.LINK_TEXT, 'О проекте')
enter_link.click()

# Ждем несколько секунд для выполнения действия
time.sleep(5)

# Закрываем браузер
driver.quit()
