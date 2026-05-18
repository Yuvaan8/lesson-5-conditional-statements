actual_cost = float(input('Enter the actual price of the product: '))
sale_amount= float(input('Enter the selling price of the product: '))
if (sale_amount > actual_cost):
  amount = sale_amount - actual_cost
  print('Profit is', amount)
else:
  print('No profit')

