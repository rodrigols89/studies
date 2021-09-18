# Object-oriented programming (OOP)

# 01 - Palavra reservada "self"

> Os métodos de classe devem ter um primeiro parâmetro extra na definição do método - ***self***
Nós não damos um valor para este parâmetro quando chamamos o método, o Python fornece. Se temos um método que não aceita argumentos, ainda assim temos que ter um argumento - ***self***

```python
# Uma classe simples
class Test:
  
  # Um simples método de exemplo.
  def fun(self):
    print('Hello!')

if __name__ == "__main__":
  obj = Test() # Cria uma instância da classe Test.
  obj.fun() # Chama o método fun() da classe Test.
```

# 02 - Construtor - Init

O método **"init"** é semelhante aos construtores em C++ e Java. É executado assim que um objeto de uma classe é instanciado. O método é útil para fazer qualquer inicialização que você queira fazer com seu objeto. Veja o exemplo abaixo:

```python
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
```

# 03 - x


**Rodrigo Leite** *- Software Engineer*
