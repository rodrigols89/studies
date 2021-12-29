########################################################
# Rodrigo Leite - drigols                              #
# Last update: 29/12/2021                              #
########################################################

def list_traditional_approach(product_prices):
  taxes = []
  for item in product_prices:
    taxes.append(item * 0.3)
  print("Tradicional List approach:", taxes)

def list_comprehension_approach(product_prices):
  taxes = [price * 0.3 for price in product_prices]
  print("List Comprehension approach:", taxes)


if __name__ =="__main__":

  product_prices = [100, 150, 300, 5500]

  list_traditional_approach(product_prices)
  list_comprehension_approach(product_prices)
