import os #operating system

products = []

if os.path.isfile('product.csv'):
	print('The file is here')
	with open('product.csv','r', encoding = 'utf-8')as f: 

		for line in f:
			if 'products, price' in line:
				continue 
			name_1, price_1 = line.strip().split(',')
			products.append([name_1, price_1 ])
	print(products)
else:
	print('The file cannot be found')


#read file
with open('product.csv','r', encoding = 'utf-8')as f:

	for line in f:
		if 'products, price' in line:
			continue 
		name_1, price_1 = line.strip().split(',')
		products.append([name_1, price_1 ])
print(products)

# users to input
while True:
	name = input('Please input product name: ')
	if name == 'q':
		break
	price = input('Please input product price: ')
	price = int(price)
	#p = []
	#p.append(name)
	#p.append(price)
	products.append([name, price])
print(products)
print(products[1])

products[0][0] #1st name and price and the 1st item -> name"

for p in products:
	print('The price of', p[0], 'is', p[1])

#write file
with open('product.csv', 'w' , encoding='utf-8') as f:
	f.write('Product, Price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') #+ -> need to str + str.  p[1] is int. Therefore, it needs to change to string.
		#\n is next line