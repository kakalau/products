products = []

while True:
	name = input('Please input product name: ')
	if name == 'q':
		break
	price = input('Please input product price: ')
	#p = []
	#p.append(name)
	#p.append(price)
	products.append([name, price])
print(products)
print(products[1])

products[0][0] #1st name and price and the 1st item -> name"