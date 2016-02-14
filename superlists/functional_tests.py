from selenium import webdriver

browser = webdriver.Chrome('drivers/chrome')
browser.get('http://localhost:8000')

assert 'Django' in browser.title