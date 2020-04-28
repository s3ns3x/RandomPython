from selenium import webdriver
import pyautogui as pyg
from selenium.webdriver.common.keys import Keys
import time

# open the web browser
driver = webdriver.Firefox(executable_path="C:\\Users\imani\Documents\Dev\RandomPython\geckodriver.exe")
driver.get('https://twitter.com/login')
time.sleep(5)

#LOGIN
username = driver.find_element_by_name('session[username_or_email]')
username.send_keys('imnirfn')
time.sleep(1)
password = driver.find_element_by_name('session[password]')
password.send_keys('')
time.sleep(1)
password.send_keys(Keys.RETURN)
time.sleep(5)

#SEARCH USERNAME
search_username = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')
search_username.send_keys('frssufyann')
time.sleep(5)

click_username = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[2]/div/div[3]/div[1]/li')
click_username.click()

button_el = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]')
button_el.click()

report_butt = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div/div/div[4]')
report_butt.click()

click_final = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]')
click_final.click()

#TWEET






