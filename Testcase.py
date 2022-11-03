// developed by Gutnik Philipp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup

need_to_find = ["Головной офис", "Москва, Пресненская набережная, 12", "Офис разработки", "Тюмень, ул. Малыгина 84 к1, 7 этаж", 
"+7 (499) 113-68-89", "mail@crtweb.ru"]

driver = webdriver.Firefox()
driver.get("http://www.yandex.ru")


searcher = driver.find_element_by_id('text')

searcher.send_keys('Creative Тюмень')
searcher.submit()

driver.find_element_by_link_text("Аутсорсинг веб программистов и разработки мобильных...").click()

driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_css_selector('nav.nav.d-flex.pl-20').click()

time.sleep(5)

driver.find_element_by_link_text("контакты").click()

url = driver.current_url
print(url)



response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
strings = soup.find_all('div', class_='tn-atom')
strings_2 = soup.find_all('a', class_='tn-atom')

for string in strings:
	for i in need_to_find:
		if i == string.text:
			print(string.text + " - найдено")
    
    
for string in strings_2:
	for i in need_to_find:
		if i == string.text:
			print(string.text + " - найдено")
