from time import sleep

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# product_name = "mobiles"


def perform_amazon_search(driver, product_name, timeout=5):
    elem = driver.find_element_by_name("field-keywords")
    elem.clear()
    elem.send_keys(product_name)
    elem.send_keys(Keys.RETURN)
    sleep(timeout)


def find_product_detail(product_link, driver):
    try:
        product_name = driver.find_element_by_id("productTitle").text
    except:
        product_name = 'N/A'
    try:
        product_price = driver.find_element_by_id("priceblock_ourprice").text
    except:
        product_price = 0
    try:
        product_strikeprice = driver.find_element_by_class_name("a-text-strike").text
    except:
        product_strikeprice = 0
    try:
        sale_price = driver.find_element_by_id("priceblock_saleprice").text
    except:
        sale_price = 0
    try:
        availability = driver.find_element_by_css_selector("#availability > span").text
    except:
        availability = "in stock"
    try:
        total_reviews = driver.find_element_by_class_name("acrCustomerReviewText").text
    except:
        total_reviews = "not reviewed"
    try:
        ratings = driver.find_element_by_id('acrPopover').get_attribute('title')
    except:
        ratings = "0"

    return {
        'name': product_name,
        'price': product_price,
        'sale_price': sale_price,
        'availability': availability,
        'reviews': total_reviews,
        'rating': ratings,
        'links': product_link,
        'Striked Price': product_strikeprice
    }


TIMEOUT = 5


def crawl_product(product_name):
    driver = webdriver.Chrome()
    driver.get("http://www.amazon.in")
    perform_amazon_search(driver, product_name)
    result_list = driver.find_elements_by_css_selector("#s-results-list-atf > li .s-color-twister-title-link")
    links = [link.get_attribute('href') for link in result_list]
    dataset = []
    for link in links:
        print(link)
        driver.get(link)
        detail = find_product_detail(link, driver)
        print(detail)
        dataset.append(detail)
        try:
            driver.back()
        except Exception as e:
            print(e)
        # sleep(TIMEOUT)
    df = pd.DataFrame(dataset)
    df.to_csv(f'database/amazon_{product_name}_details.csv')
    driver.quit()


#crawl_product()
