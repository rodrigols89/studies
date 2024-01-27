import numpy as np

def checkShape(array):
  print(array.shape)

if __name__ =='__main__':
  lst = [1, 2, 3, 5, 5]
  arr = np.array(lst)
  checkShape(arr)
