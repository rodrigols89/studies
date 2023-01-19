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
  p1 = Person('Rodrigo', 32, 2, "EUA")
  p2 = Person(nome="Isaac Newton", idade=80, numero_olhos=1, naturalidade="Reino Unido")

  print(p1.__dict__)
  print(p2.__dict__)
