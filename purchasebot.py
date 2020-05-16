import time
import requests
import json
import schedule
from selenium import webdriver
from info import info_dict


driver = webdriver.Chrome(executable_path=r'C:\Users\heybo\Desktop\chromedriver.exe')


def check_product():
    req = requests.get('https://www.stussy.com/collections/nike/products.json')
    products = json.loads(req.text)['products']

    for pr in products:
        if pr['title'] == 'Stüssy / Nike Air Zoom Spiridon Cage 2' and pr['handle'] != 'afqh9nnue888ffv' and pr['handle'] != 'vdkyj5zn8gv':
            for var in pr['variants']:
                if "8" in var['title']:
                    return 'https://www.stussy.com/collections/nike/products/' + pr['handle'] \
                           + '?variant=' + str(var['id'])
    return False


def purchase(url):
    driver.get(url)

    element = driver.find_element_by_xpath('//button[@class="btn product__atc"]')
    if element.is_enabled():
        element.click()
        time.sleep(0.6)
        driver.find_element_by_xpath('//button[@class="btn ajaxcart__checkout"]').click()
        driver.execute_script('document.getElementById("checkout_email_or_phone").value="' + info_dict['email'] + '";')
        driver.execute_script(
            'document.getElementById("checkout_shipping_address_first_name").value="' + info_dict['fname'] + '";')
        driver.execute_script(
            'document.getElementById("checkout_shipping_address_last_name").value="' + info_dict['lname'] + '";')
        driver.execute_script(
            'document.getElementById("checkout_shipping_address_address1").value="' + info_dict['addr'] + '";')
        driver.execute_script(
            'document.getElementById("checkout_shipping_address_city").value="' + info_dict['city'] + '";')
        driver.execute_script(
            'document.getElementById("checkout_shipping_address_zip").value="' + info_dict['zip'] + '";')
        driver.find_element_by_xpath('//button[@class="step__footer__continue-btn btn"]').click()

    else:
        print('error')


def handler():
    link = check_product()
    if link:
        purchase(link)
    else:
        print("oops")

schedule.every().day.at("10:00:00").do(handler)  # desired time we want function to start at

while True:
    schedule.run_pending()
    time.sleep(0.5)
