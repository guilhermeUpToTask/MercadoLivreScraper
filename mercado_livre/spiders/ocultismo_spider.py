from pathlib import Path
import scrapy
from mercado_livre.items import MercadoLivreItem
import re

def extract_uid_regex(url):
  # Improved pattern to capture ID before extension (if present)
  match = re.search(r'MLB-?(\d+)', url)
  if match:
    return match.group(1)  # Return the captured group (UID)
  else:
    return '0'  # Handle cases where no UID is found   
  


class OcultismoSpider(scrapy.Spider):
    name = "ocultismo"

    start_urls = ["https://lista.mercadolivre.com.br/ocultismo-magia"]

    def parse(self, response):
        for product in response.css('li.ui-search-layout__item'):
            price_fraction = product.css('div.ui-search-price__second-line span.andes-money-amount__fraction::text').get()
            price_cents = product.css('div.ui-search-price__second-line span.andes-money-amount__cents::text').get()
            
            if price_cents is None:
                price_cents = '00'
            if price_fraction is None:
                price = '0.0'
            else:
                price = price_fraction + '.' + price_cents

            name = product.css('h2.ui-search-item__title::text').get()

            url = product.css('div.ui-search-item__group--title a::attr(href)').get()
            if url is not None:
                id = extract_uid_regex(url)
            else:
               id = '0'

            rating_number = product.css('span.ui-search-reviews__rating-number::text').get()
            if (rating_number is None):
                    rating_number = '0'
            rating_amount = product.css('span.ui-search-reviews__amount::text').get()
            if (rating_amount is None):
                    rating_amount = '0'

            id = int(id)
            price = float(price)        
            rating_number= float(rating_number)
            rating_amount= int(rating_amount.strip('()'))
            
            yield MercadoLivreItem(id=id, name=name, price=price, url=url, rating_number=rating_number, rating_amount=rating_amount)

            next_page=response.css('li.andes-pagination__button--next  a.andes-pagination__link::attr(href)').get()
            print()
            print()
            print('next page...')
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
