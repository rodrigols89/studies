import numpy as np

def create_array(elements):
  arr = np.array(elements)
  return arr

if __name__ =='__main__':
  lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
  arr = create_array(lst)
  print(arr)
