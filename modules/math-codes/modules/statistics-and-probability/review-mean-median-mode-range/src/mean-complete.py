def calculate_mean(items):
  sum_items = sum(items)
  number_items = len(items)
  return sum_items/number_items


if __name__ =='__main__':
  donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]    
  mean = calculate_mean(donations)    
  N = len(donations)    
  print('A Média(mean) de doações nós últimos {0} dias é {1}:'.format(N, mean))
