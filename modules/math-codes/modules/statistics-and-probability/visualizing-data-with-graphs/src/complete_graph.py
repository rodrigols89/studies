import matplotlib.pyplot as plt

# Cria uma lista para representar as temperaturas de New York no ano de 2000
nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]

# Cria uma lista para representar as temperaturas de New York no ano de 2006
nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]

# Cria uma lista para representar as temperaturas de New York no ano de 2012
nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]

# Months representation
months = range(1, 13)

plt.plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
plt.legend([2000, 2006, 2012]) # Adiciona legenda para cada ano respectivamente.
plt.title('Tendências mensais de temperatura em Nova York - NYC')
plt.xlabel('Meses')
plt.ylabel('Temperatura')
plt.savefig('../images/plot-05.png', format='png')
plt.show()
