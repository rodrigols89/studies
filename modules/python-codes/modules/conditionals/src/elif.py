########################################################
# Rodrigo Leite - drigols                              #
# Last update: 01/11/2021                              #
########################################################

goal = 20000

sales = float(input("Enter sales amount: "))

if sales < goal:
  print("No bonus.")
elif sales > (goal*2):
  bonus = (0.07 * sales) # 7% bonus.
  print("Bonus 7%: {0}".format(bonus))
else:
  bonus = (0.03 * sales) # 3% bonus.
  print("Bonus 3%: {0}".format(bonus))
