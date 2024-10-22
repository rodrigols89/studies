import numpy as np

def create_arrange(start, stop, step=None):
  arr = np.arange(start, stop, step)
  return arr

if __name__ =='__main__':
  arr = create_arrange(1, 20, 2)
  print(arr)
