# Exemplo de função comm *args:
def test_args(first, *args):
  print('O primeiro argumento: {}'.format(first))
  for n in args:
    print('Outro argumento: {}'.format(n))


# Exemplo de função comm **kwargs:
def chave_value(**kwargs):
  for key, value in kwargs.items():
    print('{0}: {1}'.format(key, value))


if __name__ == "__main__":

  test_args('Python', 'é', 'muito', 'legal')
  lista = [20, 30, 40] # Exemplo com lista.
  test_args(10, *lista)
  tupla = ('Amazon', 'Microsoft', 'Apple') # Exemplo com tupla.
  test_args('Google', *tupla)

  print()

  chave_value(empresa='Google')
  dicionario = {'nome': 'Rodrigo Leite da Silva', 'idade': 30}
  chave_value(**dicionario)
