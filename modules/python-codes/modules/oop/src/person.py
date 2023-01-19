########################################################
# Rodrigo Leite - drigols                              #
# Last update: 07/11/2021                              #
########################################################

class Person:
  
  def __init__(self, nome, idade=None, numero_olhos = 2, naturalidade = "Brazil"):
    self.nome = nome
    self.idade = idade
    self.numero_olhos = numero_olhos
    self.naturalidade = naturalidade
    
if __name__ == "__main__":
  p = Person('Rodrigo')
  print(p.__dict__)
