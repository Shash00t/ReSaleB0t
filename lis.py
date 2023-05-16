import json
import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

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
        body = driver.find_element(by=By.CLASS_NAME, value="body")
        print(body.text)
        time.sleep(3)
        driver.close()
        driver.quit()

def parse_url():
    with open('index.html', 'r', encoding='utf8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    nazvlis=[]
    cenalis=[]
    for title in soup.find_all('div', {"class":'name-inner'}):
        nazvlis.append(title.get_text())
    for cena in soup.find_all('div', {"class":'price'}):
        cenalis.append(cena.get_text())

    with open("nazvania_lis.json", "w", encoding="utf-8") as f:
        json.dump(nazvlis, f, indent=4, ensure_ascii=False)

    with open("cena_lis.json", "w", encoding="utf-8") as f:
        json.dump(cenalis, f, indent=4, ensure_ascii=False)


def main():
    #save_selenium(r'https://lis-skins.ru/market/csgo/?sort_by=date_desc')

    parse_url()

if __name__ == '__main__':
    main()
