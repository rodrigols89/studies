def dados(nome=None, idade=None):
  print('nome: {}'.format(nome))
  if(idade is not None):
    print('idade: {}'.format(idade))
  else: print('idade: não informada')

if __name__ == "__main__":
  dados('Rodrigo Leite', 30) # Passa o nome e idade.
  dados('Rodrigo Leite') # Passa só o nome.

  # Específica o atributo idade para passar a idade como argumento
  # diretamente para o campo correto.
  dados(idade=30)
