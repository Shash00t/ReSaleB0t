import json
import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def save_selenium(url):
    link = url
    options = webdriver.FirefoxOptions()
    options.set_preference("general.useragent.override", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36')
    try:
        driver = webdriver.Firefox(
            executable_path='C:\\projects\\selenium\\geckodriver.exe',
            options=options,
        )
        driver.get(url=link)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(driver.page_source)
    except Exception as ex:
        print(ex)
    finally:

        cena_steam=[]

        with open('nazvania_lis.json') as f:
            mas = json.load(f)
        for i in range(0, len(mas), len(mas)):
            mas=mas[i:i+5]

        for i in range(len(mas)):
            eml = driver.find_element("xpath" ,'//*[@id="findItemsSearchBox"]').send_keys(mas[i])
            butt=driver.find_element("xpath" ,'//*[@id="findItemsSearchSubmit"]').click()
            time.sleep(2)
            pri=driver.find_element("xpath", '//*[@id="result_0"]/div[1]/div[2]/span[1]/span[1]').text
            cena_steam.append(pri)
            eml1=driver.find_element("xpath" ,'//*[@id="findItemsSearchBox"]').click()
            ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
            ActionChains(driver).key_down(Keys.DELETE).perform()
            time.sleep(2)

        cena_steam1=[]
        for i in range(len(cena_steam)):
            s=str(cena_steam[i])
            s=s[1:]
            s=s[:-4]
            s=float(s)
            cena_steam1.append(round(s*80,2))

        with open("cena_steam.json", "w", encoding="utf-8") as f:
            json.dump(cena_steam1, f, indent=4, ensure_ascii=False)
        time.sleep(1)
        driver.close()
        driver.quit()

def main():
    save_selenium(r'https://steamcommunity.com/market/search?appid=730')

if __name__ == '__main__':
    main()
