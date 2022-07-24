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
driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
    'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
    '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
driver.implicitly_wait(15)


print('Login Successful...!!')
while True:
    time.sleep(1)
