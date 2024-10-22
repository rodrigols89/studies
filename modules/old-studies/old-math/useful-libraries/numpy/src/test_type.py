import numpy as np

def test_type(tp):
  print("Type: ", type(tp))

def create_array(elements):
  arr = np.array(elements)
  return arr

if __name__ =='__main__':
  lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
  print(lst)
  test_type(lst)

  arr = create_array(lst)
  print(arr)
  test_type(arr)
