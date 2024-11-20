# Simple Calculate

line_1 = input().split()
product_1 = int(line_1[0])
quantidade_1 = int(line_1[1])
price_1 = float(line_1[2])

line_2 = input().split()
product_2 = int(line_2[0])
quantidade_2 = int(line_2[1])
price_2 = float(line_2[2])

total = (quantidade_1 * price_1) + (quantidade_2 * price_2)

print('VALOR A PAGAR: R$ {:.2f}'.format(total))
