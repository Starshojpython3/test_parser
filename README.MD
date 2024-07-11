1. Install requirements
   - pip install -r requirements.txt


2. Ebay_parser.py
   - Tested on https://www.ebay.com (USA version)
   - Example usage:
        Welcome to the eBay parsing program!
        Please enter the product link or 'exit' to quit:  link for product (https://www.ebay.com/itm/226166236498?_trkparms=5373%3A0%7C5374%3AFeatured)
   - Example output
        {
            "product_link": "https://www.ebay.com/itm/226166236498?_trkparms=5373%3A0%7C5374%3AFeatured",
            "title": "Dabbsson 2330Wh 2200W Power Station DBS2300Plus Portable Solar Generator Camping",
            "image": "https://i.ebayimg.com/images/g/DicAAOSwPPRmfhRY/s-l1600.jpg",
            "price": "US $1,022.72",
            "seller": "dabbsson_official",
            "shipping_price": "Does not ship to Ukraine"
        }
   

     
3. rest_countries_api.py
    - Example usage:
        Enter 'all' to display all countries or enter a country name in English.
        To exit the program, type 'exit'.
        Please make your choice: 
    - Example output
          +---------+------+----------------+
          | Country Name | Capital Name | Flag URL (png) |
          +---------+------+----------------+
          | Ukraine | Kyiv | https://flagcdn.com/w320/ua.png |
          +---------+------+----------------+