from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import pyautogui as pg
import time

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")
target = "'Your Friends name'"
xpath = '//span[@title='+target+']'
driver.find_element(By.XPATH, xpath).click()
string = 'Your message'
tb_id = "'_2S1VP copyable-text selectable-text'"
input_box =  driver.find_element(By.XPATH, '//div[@class='+tb_id+']')
for i in range(100):
	input_box.send_keys(string+Keys.ENTER)