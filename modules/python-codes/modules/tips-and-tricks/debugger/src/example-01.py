def say_hello(name, age):
  return 'Hello, my name is {name}, age {age}'


if __name__ =="__main__":
  name = "Rodrigo"
  age  = "32"

  breakpoint()

  msg = say_hello(name, age)

  # TEST!
  assert msg == 'Hello, my name is Rodrigo, age 32'
