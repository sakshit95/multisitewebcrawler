from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd


def shoclues_searching(driver, product_name, timeout=5):
    elem = driver.find_element_by_id("autocomplete")
    elem.clear()
    elem.send_keys(product_name)
    elem.send_keys(Keys.RETURN)
    sleep(timeout)

def text_price_to_real_price(price):
    if 'Rs.' in price:
        price=price[3:]
    price=price.replace(',','')
    return float(price)

def get_product_data(container,link):
    title = container.find_element_by_tag_name('h1').text
    try:rating =float(container.find_element_by_css_selector('.prd_ratings span').text)
    except:rating = 0.0
    try:reviews=int(container.find_element_by_css_selector('span.prd_reviews').text.split()[0])
    except:reviews= 0
    sale_price=container.find_element_by_class_name('f_price').text
    try:striked_price=container.find_element_by_id('sec_list_price_').text
    except:striked_price = sale_price
    try:price=container.find_element_by_class_name('o_price').text
    except:price = sale_price
    sale_price=text_price_to_real_price(sale_price)
    striked_price=text_price_to_real_price(striked_price)
    price=text_price_to_real_price(price)
    try:availability =container.find_element_by_id('iscod').text
    except:availability="not available"

    return {
        'name': title,
        'price': price,
        'sale_price': sale_price,
        'availability': availability,
        'reviews': reviews,
        'rating': rating,
        'links': link,
        'Striked Price': striked_price
    }


def main(query="mobiles"):
    driver = webdriver.Chrome('chromedriver')
    driver.get("http://www.shopclues.com")
    main_window = driver.current_window_handle
    shoclues_searching(driver, query)

    all_products = driver.find_element_by_id('product_list')
    rows = all_products.find_elements_by_class_name('row')
    product_list =[]
    for row in rows:
        product_items = row.find_elements_by_class_name('search_blocks')
        for product_item in product_items:
            product_link = product_item.find_element_by_tag_name('a')
            link=product_link.get_attribute('href')
            product_link.send_keys(Keys.CONTROL + Keys.RETURN)
            sleep(5)
            driver.switch_to.window(driver.window_handles[1])
            open_window = driver.current_window_handle
            print(driver.title)
            container = driver.find_element_by_id('main_data')
            data=get_product_data(container,link)
            product_list.append(data)
            driver.close()
            driver.switch_to.window(main_window)
            driver.switch_to.default_content()
        print('next row')
    print('finish')
    df=pd.DataFrame(product_list)
    df.to_csv("database/"+query+"_shopclues.csv")
    print('saved output to ',"database/"+query+"_shopclues.csv")

if __name__ == "__main__":
    main(query="mobiles")