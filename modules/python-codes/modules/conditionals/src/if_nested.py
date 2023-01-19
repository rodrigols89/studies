########################################################
# Rodrigo Leite - drigols                              #
# Last update: 31/10/2021                              #
########################################################

grade = float(input("Enter you grade: "))

if grade >= 7:
  print("Aproved!")
else:
  if grade >= 5:
    print("Retake test!")
  else:
    print("Reproved!")
