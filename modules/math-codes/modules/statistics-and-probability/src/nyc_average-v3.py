########################################################
# Rodrigo Leite - drigols                              #
# Last update: 26/09/2021                              #
########################################################

def create_plot(x, y):
  import matplotlib.pyplot as plt

  # Display to each "x" the temperature average "y".
  for year, average_temp in zip(x, y):
    print("In year {0} the average New York temperature was {1}°".format(year, average_temp))

  plt.plot(x, y, marker='o')
  plt.savefig('../images/new-york-tem-03.png', format='png')
  plt.show()

if __name__ =='__main__':

  # Create a list to represent New York temperatures from 2000 to 2021.
  nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]

  # Use range() function to create a predefined list (2000 to 2021).
  # NOTE: Remember that range() function never display the last element. That is from 2000 to 2013.
  years = range(2000, 2013)

  # Cria a plot with create_plot() function.
  create_plot(years, nyc_temp)
