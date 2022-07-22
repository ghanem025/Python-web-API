from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from getpass import getpass
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
  
pwd = getpass('Enter Password:')
print(pwd)
gmailId = input("Enter email")
print(gmailId)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(r'https://github.com/login')
driver.implicitly_wait(150)

loginBox = driver.find_element(by=By.XPATH, value='//*[@id ="login_field"]')
loginBox.send_keys(gmailId)

passWordBox = driver.find_element(by=By.XPATH, value='//*[@id ="password"]')
passWordBox.send_keys(pwd)

# passWordBox = driver.find_element_by_xpath(
#     '//*[@id ="password"]/div[1]/div / div[1]/input')
# passWordBox.send_keys(passWord)

element = driver.find_element(by=By.XPATH, value='//input[@type="submit"and @value="Sign in"]')
element.click()


print('Login Successful...!!')
while True:
    time.sleep(1)
