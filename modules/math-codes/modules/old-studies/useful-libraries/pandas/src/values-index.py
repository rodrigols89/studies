from pandas import Series

def print_valuesAndIndex(obj):
  print(obj.values)
  print(obj.index)

if __name__=='__main__':
  lst = [1, 2, 3, 4]
  obj = Series(lst)
  print_valuesAndIndex(obj)
