import numpy as np

def create_zeros(*args):
  arrZeros = np.zeros(args)
  return arrZeros

if __name__=='__main__':
  arr = create_zeros(10)
  print(arr, "\n")

  lst = [5, 2]
  arr = create_zeros(*lst)
  print(arr, "\n")

  lst_two = [5, 5]
  arr = create_zeros(*lst_two)
  print(arr)
