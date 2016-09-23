import requests
import json

class Shopify:
	def __init__(self):
		self.page = 1 #intitalisig page class var

	def increment(self):
		self.page += 1

	def fetch(self):
		BASE_URL = "http://shopicruit.myshopify.com/products.json?page="
		data = requests.get(BASE_URL+ str(self.page))
		return data.text

if __name__ == "__main__":
	shop = Shopify()
	sum  = 0.0
	i    = 0

	while i < 5:
		product_data = json.loads(shop.fetch()) # parsing json data
		for data in product_data['products']:
			if data['product_type'] == "Clock" or data['product_type'] == "Watch":
				for variant in data['variants']:
					sum += float(variant['price'])
		shop.increment()
		i += 1
		
	print sum
