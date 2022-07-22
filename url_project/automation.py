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

repo_name = input("Enter your new github repo name")

repo_description = input("Enter your Repo description")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(r'https://github.com/login')
driver.implicitly_wait(15)

loginBox = driver.find_element(by=By.XPATH, value='//*[@id ="login_field"]')
loginBox.send_keys(gmailId)

passWordBox = driver.find_element(by=By.XPATH, value='//*[@id ="password"]')
passWordBox.send_keys(pwd)

element = driver.find_element(by=By.XPATH, value='//input[@type="submit"and @value="Sign in"]')
element.click()

driver.implicitly_wait(3)

l = driver.find_element(by=By.LINK_TEXT, value='New')
l.click()

repo = driver.find_element(by=By.XPATH, value='//input[@id="repository_name"]')
repo.send_keys(repo_name)

description = driver.find_element(by=By.XPATH, value='//input[@id="repository_description"]')
description.send_keys(repo_description)

time.sleep(2)

if create_repo := driver.find_element(by=By.XPATH, value='//button[@class="btn-primary btn" and @type="submit"]'):
    create_repo.click()

print('Login Successful...!!')
while True:
    time.sleep(1)
