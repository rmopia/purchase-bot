import time
import requests
import json
import schedule
from selenium import webdriver


driver = webdriver.Chrome(executable_path=r'C:\Users\heybo\Desktop\chromedriver.exe')


def check_product_test():
    req = requests.get('https://www.stussy.com/collections/backpacks-and-bags/products.json')
    products = json.loads(req.text)['products']

    for pr in products:
        if pr['title'] == 'Mesh Beach Tote Bag':
            for var in pr['variants']:
                if 'EA' in var['title']:
                    print(str(var['id']) + " " + var['title'])
                    return 'https://www.stussy.com/collections/backpacks-and-bags/products/' + pr['handle'] \
                           + '?variant=' + str(var['id'])

    return False


def purchase_test(url):
    driver.get(url)

    element = driver.find_element_by_xpath('//button[@class="btn product__atc"]')
    if element.is_enabled():
        element.click()
        time.sleep(0.5)
        driver.find_element_by_xpath('//button[@class="btn ajaxcart__checkout"]').click()
        time.sleep(0.5)
        driver.execute_script('document.getElementById("checkout_email_or_phone").value="sample@gmail.com";')
        driver.execute_script('document.getElementById("checkout_shipping_address_first_name").value="Chester";')
        driver.execute_script('document.getElementById("checkout_shipping_address_last_name").value="Tester";')
        driver.execute_script('document.getElementById("checkout_shipping_address_address1").value="123 Apple Street";')
        driver.execute_script('document.getElementById("checkout_shipping_address_city").value="San Marcos";')
        driver.execute_script('document.getElementById("checkout_shipping_address_zip").value="91912";')
        driver.find_element_by_xpath('//button[@class="step__footer__continue-btn btn"]').click()
    else:
        print('oopsy')


def check_product():
    req = requests.get('https://www.stussy.com/collections/nike/products.json')
    products = json.loads(req.text)['products']

    for pr in products:
        if pr['title'] == 'Stüssy / Nike Air Zoom Spiridon Cage 2' and pr['handle'] != 'afqh9nnue888ffv':
            for var in pr['variants']:
                if "8" in var['title']:
                    print(str(var['id']) + " " + var['title'])
                    return 'https://www.stussy.com/collections/nike/products/' + pr['handle'] \
                           + '?variant=' + str(var['id'])

    return False


def purchase(url):
    driver.get(url)
    driver.find_element_by_xpath('//div[@data-value="8"]').click()


def handler():
    link = check_product_test()
    if link:
        purchase_test(link)
    else:
        print("oops")


handler()

# schedule.every().day.at("11:06:02").do(handler)
# schedule.every().day.at("10:00:00").do(handler)

'''while True:
    schedule.run_pending()
    time.sleep(0.5)'''
