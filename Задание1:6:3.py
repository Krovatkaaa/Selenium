from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = "http://suninjuly.github.io/simple_form_find_task.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# пустая строка в конце скрипта




from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import match
link = "https://suninjuly.github.io/find_link_text"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    link=browser.find_element(By.LINK_TEXT, "224592")
    link.click()
    
    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# пустая строка в конце скрипта



from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.CSS_SELECTOR, "input")
    for element in elements:
        element.send_keys("Мой ответ")     
    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# пустая строка в конце скрипта



from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements(By.CSS_SELECTOR, "input")
    for element in elements:
        element.send_keys("Мой ответ")     
    button = browser.find_element(By.XPATH,"//button[@type='submit']")
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# пустая строка в конце скрипта




from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/registration1.html")
    elements = browser.find_elements(By.XPATH, "//input[@required]")
    for element in elements:
        element.send_keys("Мой ответ")     
    button = browser.find_element(By.XPATH,"//button[@type='submit']")
    button.click()

    #пауза для загрузки страницы
    time.sleep(2)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully register!" == welcome_text
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# пустая строка в конце скрипта




from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/registration2.html")
    elements = browser.find_elements(By.XPATH, "//input[@required]")
    for element in elements:
        element.send_keys("Мой ответ")
        time.sleep(10)
    button = browser.find_element(By.XPATH,"//button[@type='submit']")
    button.click()

    #пауза для загрузки страницы
    time.sleep(2)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully register!" == welcome_text
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# пустая строка в конце скрипта





from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Инициализация браузера
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")
    
    # Получаем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    # Вводим ответ
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)
    
    # Отмечаем чекбокс
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()
    
    # Выбираем радиокнопку
    robots_rule = browser.find_element(By.ID, "robotsRule")
    robots_rule.click()
    
    # Отправляем форму
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    
    # Даем время увидеть результат
    time.sleep(10)
    
finally:
    # Закрываем браузер
    browser.quit()





from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Инициализация браузера
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/get_attribute.html")
    
    # Получаем значение x
    x_element = browser.find_element(By.XPATH, "//img [@valuex]")
    x_element = x_element.get_attribute("valuex")
    x = x_element.text
    y = calc(x)
    
    # Вводим ответ
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)
    
    # Отмечаем чекбокс
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()
    
    # Выбираем радиокнопку
    people_radio = browser.find_element(By.ID, "peopleRule")
    people_radio.click()
    
    # Отправляем форму
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    
    # Даем время увидеть результат
    time.sleep(10)
    
finally:
    # Закрываем браузер
    browser.quit()
