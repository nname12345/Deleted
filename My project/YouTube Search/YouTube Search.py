from selenium import webdriver

driver = webdriver.Chrome('C:/Users/Family/Desktop/Лев/My project/DriverChrome/chromedriver.exe')
driver.get('https://www.youtube.com/')
search = driver.find_element_by_xpath('//*[@id="search"]')
search.send_keys('Шевроле Кобальт')
button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
button.click()
video = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[2]/div[1]/div/div[1]/div/h3/a/yt-formatted-string')
video.click()
