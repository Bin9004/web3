from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : r"C:\User\User\Desktop\py\지숙 크롤링"}
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = r"C:\Users\User\Desktop\py\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)

driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("레인보우 지숙")
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 3

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height


images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
'''
for image in images:
    try:
        image.click()
        time.sleep(2)
        imgUrl = driver.find_element_by_xpath(r'/*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
        urllib.request.urlretrieve(imgUrl, str(count)+".jpg")
        count += 1
    except:
        pass
driver.close()
'''
