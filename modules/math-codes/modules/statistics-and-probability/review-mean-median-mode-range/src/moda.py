from collections import Counter

def calculate_mode(items):
  c = Counter(items)
  mode = c.most_common(1)
  return mode[0][0]

if __name__=='__main__':
  scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
  mode = calculate_mode(scores)
  print('A moda(mode) da lista de notas é: {0}'.format(mode))
