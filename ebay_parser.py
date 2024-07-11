import json
import re

import requests
from bs4 import BeautifulSoup


class EbayParser:
    def __init__(self):
        self.dict_parse = {
            "product_link": "",
            "title": "",
            "image": "",
            "price": "",
            "seller": "",
            "shipping_price": "",
        }
        self.soup = ""

    def collect_important_data(self):
        # title
        title_tag = self.soup.find(class_="x-item-title__mainTitle")
        if title_tag:
            self.dict_parse["title"] = title_tag.get_text(strip=True)
        else:
            print("Failed to find the product title.")

        # image link
        image_tag = self.soup.find_all("div", class_="ux-image-carousel zoom img-transition-medium")
        if image_tag:
            image_links = []
            for tag in image_tag:
                img_tags = tag.find_all('img')
                for img in img_tags:
                    data_zoom_src = img.get('data-zoom-src')
                    src = img.get('src')
                    if data_zoom_src:
                        image_links.append(data_zoom_src)
                    elif src:
                        image_links.append(src)

            image_links = [link for link in image_links if link.startswith('http')]
            self.dict_parse["image"] = image_links[0] if image_links else ""
        else:
            print("Failed to find product images.")

        # price
        price_tag = self.soup.find("div", class_="x-price-primary")
        if price_tag:
            span_tag = price_tag.find("span", class_="ux-textspans")
            self.dict_parse["price"] = span_tag.get_text(strip=True)
        else:
            print("Failed to find the product price.")

        # seller
        seller_tag = self.soup.find("div", class_="x-sellercard-atf__info__about-seller")
        if seller_tag:
            self.dict_parse["seller"] = seller_tag.get('title')
        else:
            print("Failed to find seller information.")

        # delivery price
        label_html_elements = self.soup.select('.ux-labels-values__labels')
        for label_html_element in label_html_elements:
            if 'Shipping:' in label_html_element.text:

                shipping_price_html_element = label_html_element.next_sibling.select_one('.ux-textspans--BOLD')
                if shipping_price_html_element is not None:
                    self.dict_parse["shipping_price"] = shipping_price_html_element.get_text(strip=True)
                    # break
        else:
            print("Failed to find shipping cost information.")

    def create_json(self):
        json_data = json.dumps(self.dict_parse, indent=4, ensure_ascii=False)
        print(json_data)

    def get_page_html(self):
        try:
            response = requests.get(self.dict_parse["product_link"])
            response.raise_for_status()
            html_content = response.content
            self.soup = BeautifulSoup(html_content, "html.parser")
        except requests.RequestException as e:
            print(f"Error loading page: {e}")
            self.soup = ""

    def main(self):
        print("Welcome to the eBay parsing program!")
        while True:
            product_link = input("Please enter the product link or 'exit' to quit: ")
            if product_link.lower() == 'exit':
                print("Exiting the program...")
                break
            elif not re.match(r'https?://', product_link):
                print("Invalid link. Please enter a valid link.")
                continue

            self.dict_parse["product_link"] = product_link

            self.get_page_html()

            if self.soup:

                self.collect_important_data()


                self.create_json()
            else:
                print("Failed to load the page. Please try again.")

if __name__ == "__main__":
    parser = EbayParser()
    parser.main()
