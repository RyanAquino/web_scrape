"""
Author: Ryan Aquino
Description: Scrape Amazon.com Best seller cellphone accessories Device Name, Ratings and Price.
"""
from bs4 import BeautifulSoup
import requests


def get_details(item):
    """
    Helper function to get the scrape the name of the item

    :param item: html item
    :return: json details of item
    """
    sibling = item.find('span').find(class_='zg-item')
    device_name = sibling.find('a').get_text()
    rating = sibling.findAll('a')[2].get_text()
    price = sibling.find(class_='a-row').find('span').get_text()

    data = {
        'name': device_name.strip(),
        'rating': rating.strip(),
        'price': price.strip()
    }

    print(data)
    return data


def scrape(url):
    """
    Scrape Amazon.com Best seller cellphone accessories

    :param url: url to be scraped
    :return: json list of best seller cellphone accessories
    """
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findAll(class_='zg-item-immersion')

    for item in items:
        get_details(item)


if __name__ == '__main__':
    scrape('https://www.amazon.com/Best-Sellers-Cell-Phone-Accessories/zgbs/wireless/2407755011/ref=zg_bs_nav_1_wireless')
