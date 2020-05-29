from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/selects1.html"


# try:
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_id("robotCheckbox").click()
browser.find_element_by_id("robotsRule").click()
browser.find_element_by_css_selector("button.btn").click()

# finally:
# закрываем браузер после всех манипуляций
# browser.quit()

# не забываем оставить пустую строку в конце файла
