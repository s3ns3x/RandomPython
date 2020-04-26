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
password.send_keys('najihahcomel')
time.sleep(1)
password.send_keys(Keys.RETURN)
time.sleep(5)
#TWEET


#driver.find_element_by_class_name('css-1dbjc4n r-urgr8i r-42olwf r-sdzlij r-1phboty r-rs99b7 r-1w2pmg r-vlx1xi r-zg41ew r-1jayybb r-17bavie r-icoktb r-15bsvpr r-o7ynqc r-6416eg r-lrvibr').click()
#write stuffs
twt = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div')
twt.send_keys('Tweeting from python!')

twtButton = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]')
twtButton.click()
