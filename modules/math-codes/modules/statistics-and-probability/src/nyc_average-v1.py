########################################################
# Rodrigo Leite - drigols                              #
# Last update: 26/09/2021                              #
########################################################

def create_plot(x, y):
  from pylab import plot, show, savefig
  plot(x, y)
  savefig('../images/new-york-tem-01.png', format='png')
  show()  

if __name__ =='__main__':

  x_numbers = [1, 2, 3] # Create a list to represent axis-X.
  y_numbers = [2, 4, 6] # Create a list to represent axis-y.

  create_plot(x_numbers, y_numbers)
