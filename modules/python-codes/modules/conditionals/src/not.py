########################################################
# Rodrigo Leite - drigols                              #
# Last update: 01/11/2021                              #
########################################################

email = input("Enter you E-mail address: ")

if not '@' in email:
  print("Email:", email)
  print("Don't have @")
else:
  print("Email:", email)
  print("Has @")
