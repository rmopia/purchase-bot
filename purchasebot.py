import threading
import time
import requests
import json
from datetime import datetime
from datetime import timedelta
import schedule
import self as self
from selenium import webdriver


driver = webdriver.Chrome(executable_path=r'C:\Users\heybo\Desktop\chromedriver.exe')


def check_product_test():
    req = requests.get('https://www.stussy.com/collections/backpacks-and-bags/products.json')
    products = json.loads(req.text)['products']

    for pr in products:
        if pr['title'] == 'Mesh Beach Tote Bag':
            # print(pr['variants'['title']])
            return 'https://www.stussy.com/collections/backpacks-and-bags/products/' + pr['handle']

    return False


def purchase_test(url):
    driver.get(url)
    driver.find_element_by_xpath('//div[@class="swatch__element ea"]').click()
    driver.find_element_by_xpath('//button[@class="btn product__atc"]').click()
    time.sleep(1.3)
    driver.find_element_by_xpath('//button[@class="btn ajaxcart__checkout"]').click()
    while 1:
        continue


def check_product():
    req = requests.get('https://www.stussy.com/collections/nike/products.json')
    products = json.loads(req.text)['products']

    for pr in products:
        if pr['title'] == 'Stüssy / Nike Air Zoom Spiridon Cage 2' and pr['handle'] != 'afqh9nnue888ffv':
            # print(pr['variants'['title']])
            return 'https://www.stussy.com/collections/nike/products/' + pr['handle']

    return False


def purchase(url):
    driver = webdriver.Chrome(executable_path=r'C:\Users\heybo\Desktop\chromedriver.exe')
    driver.get(url)
    driver.find_element_by_xpath('//div[@data-value="8"]').click()


def handler():
    link = check_product_test()
    if link:
        purchase_test(link)
    else:
        print("oops")

handler()