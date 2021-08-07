from selenium import webdriver

driver = webdriver.Chrome('C:/Users/Family/Desktop/Лев/My project/DriverChrome/chromedriver.exe')
driver.get('https://www.youtube.com/')
search = driver.find_element_by_xpath('//*[@id="search"]')
search.send_keys('Hello, world!')
#//*[@id="search-icon-legacy"]/yt-icon
button