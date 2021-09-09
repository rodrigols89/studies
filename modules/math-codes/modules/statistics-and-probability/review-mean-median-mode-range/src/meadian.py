def calculate_median(items):
    
  n_items = len(items)
  items.sort()

  if n_items % 2 == 0:
    m1 = n_items/2
    m2 = (n_items/2) + 1  
    m1 = int(m1) - 1
    m2 = int(m2) - 1        
    median = (items[m1] + items[m2])/2
  else:
    m = (n_items+1)/2
    m = int(m) - 1
    median = items[m]
        
  return median

if __name__ == '__main__':
  donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
  median = calculate_median(donations)
  N = len(donations)
  print('A Mediana(median) de doações nós últimos {0} dias é {1}:'.format(N, median))
