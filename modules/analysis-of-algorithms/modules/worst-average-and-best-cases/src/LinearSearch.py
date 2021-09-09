def search(arr, element):
  for index, value in enumerate(arr):
    if value == element:
      return index
  return -1

if __name__ =="__main__":
  arr = [1, 10, 30, 15]
  element = 30

  print(element, "is present at index ", search(arr, element))
