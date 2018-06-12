import requests
from bs4 import BeautifulSoup


url = 'https://www.magazineluiza.com.br/geladeira-refrigerador-consul-frost-free-duplex-437l-bem-estar-crm55abana-branco/p/0888942/ed/elgf/'
type = 'geladeira-refrigerador'

def get_informations(url, ctr):
	r = requests.get(url)

	html_doc = r.text

	soup = BeautifulSoup(html_doc, 'html.parser')

	# SKU (código do produto na loja)
	span = soup.select('small.header-product__code')
	sku = span[0].select('meta')[0].attrs['content']
	sku = sku.split(':')[1]
	# Titulo
	title = soup.title.string

	# soup.select('table.description__box')
	table = soup.select('table.description__box--wildSand')[0]
	t = table.select('td.description__information-right')[0]
	boxes = t.select('table.description__box')
	for box in boxes:
		# Marca
		if(box.select('td.description__information-box-left')[0].text.strip() == 'Marca'):
			brand = box.select('td.description__information-box-right')[0].text.strip()

		# Modelo
		if(box.select('td.description__information-box-left')[0].text.strip() == 'Modelo'):
			model = box.select('td.description__information-box-right')[0].text.strip()

	# Preço
	price = soup.select('span.price-template__text')[0].text

	# Categoria
	category = ctr

	return (sku, title, brand, model, price, category)



