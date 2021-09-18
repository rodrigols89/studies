def create_plot(x, y):
  from pylab import plot, show, savefig
  plot(x, y)
  savefig('../images/plot-01.png', format='png')
  show()  

if __name__ =='__main__':
  x_numbers = [1, 2, 3] # Cria uma lista para representar as coordenadas "X".
  y_numbers = [2, 4, 6] # Cria uma lista para representar as coordenadas "Y".

  create_plot(x_numbers, y_numbers)
