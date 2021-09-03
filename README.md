# web3
22222
from selenium import webdriver
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://m.place.naver.com/rest/vaccine?vaccineFilter=used&x=126.9352215&y=37.5588604&bounds=126.8991726%3B37.5445875%3B126.9712704%3B37.5731305")
driver.find_element_by_xpath("/html/body/div[3]/div/div/a").click()

while True:
    try:
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[2]/a").click()
        time.sleep(1.15)
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div/div/div[4]/ul/li[1]/div[2]/div[1]/a").click()
        time,sleep(0.7)
    except:
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/a").click()
    finally:
        continue




##https://v-search.nid.naver.com/reservation/info?key=0HmcxkNVA5W1L9z

##https://www.youtube.com/watch?v=RQ_UU8g_f3A





[{"name":"잔여백신","url":"naver.com","initWait":0,"startTime":"","enable":true,"startType":"auto","loadType":"window","hotkey":"Ctrl + Shift + A","batch":{"refresh":false,"repeat":999999,"repeatInterval":0.2},"actions":[{"name":"","initWait":0,"elementFinder":"ClassName::_1MCHh","value":"ClickEvents","repeat":0,"repeatInterval":0,"addon":{"elementFinder":"","value":"","condition":"","valueExtractor":"","recheck":0,"recheckInterval":0,"recheckOption":"stop"},"settings":{"retry":0,"retryOption":"skip"}},{"name":"","initWait":0,"elementFinder":"//*[@id=\"_list_scroll_container\"]/div/div/div[3]/ul/li/div[2]/div[1]/a","value":"ClickEvents","repeat":0,"repeatInterval":0,"addon":{"elementFinder":"","value":"","condition":"","valueExtractor":"","recheck":0,"recheckInterval":0,"recheckOption":"stop"},"focus":true,"settings":{"retry":0,"retryOption":"skip"}},{"name":"","initWait":0,"elementFinder":"//*[@id=\"reservation_confirm\"]","value":"ClickEvents","repeat":0,"repeatInterval":0,"addon":{"elementFinder":"","value":"","condition":"","valueExtractor":"","recheck":0,"recheckInterval":0,"recheckOption":"stop"},"focus":true,"settings":{"retry":3,"retryInterval":0.1,"retryOption":"skip"}}]}]




라틴어(1) 1주차 숙제

2017163055 정종빈

숙제1.

1. Gladius(검) 2. Vinciō(승리하다) 3. Principia(원리) 4.liberta(자유민) 5.impromptu(즉흥곡)

숙제2.

1. 에라스무스 – 우신예찬 
2. 토머스 모어 – 유토피아
3. 아이작 뉴튼 - 프린키피아 
4. 데카르트 – 철학 원리
5. 코페르니쿠스 – 천구의 회전에 관하여

숙제 3.
키케로, 크라수스, 스파르타쿠스, 폼페이우스, 카이사르

