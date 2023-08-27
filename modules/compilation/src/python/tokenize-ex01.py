class Calc:
    def add(self, x: float, y: float) -> float:
        return x + y

    def sub(self, x: float, y: float) -> float:
        return x - y

    def mult(self, x: float, y: float) -> float:
        return x * y

    def div(self, x: float, y: float) -> float:
        try:
          return x / y
        except ZeroDivisionError:
          print("Sorry! You are dividing by zero ")


if __name__ == "__main__":
   c = Calc()

   x1: float = 10
   x2: float = 20
   x3: float = c.add(x1, x2)
   print("The sum is: ",x3)
