from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math



def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"


# try:
browser = webdriver.Chrome()
browser.get(link)
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
browser.find_element_by_css_selector("button.btn").click()
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_css_selector("#solve").click()


# finally:
# закрываем браузер после всех манипуляций
# browser.quit()

# не забываем оставить пустую строку в конце файла
