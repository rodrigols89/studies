# Cria uma classe para uma pessoa
class Person:
  
  def __init__(self, name=None):
    self.name = name
    
  def say_name(self):
    print('Olá, meu nome é', self.name)
    
if __name__ == "__main__":
  p = Person('Rodrigo') # Cria uma instância da classe Person.
  p.say_name() # Chama o método say_name().

  # Cria uma instância da classe Person, mas não passa nenhum argumento.
  # Como a não classe tem um valor default para o construtor nós podemos
  # omitir o nome da pessoa.
  p2 = Person()
  p2.say_name()
