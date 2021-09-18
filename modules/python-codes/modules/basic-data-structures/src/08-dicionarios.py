# Exemplo de um dicionário para representar um cadastro de uma pessoa.
pessoa = {"nome": 'Rodrigo', 'idade': 29, 'cidade': 'Campina Grande'}
print(pessoa)
print(type(pessoa))

print('')

# Não é possível acessar um elemento de um dicionário por um índice como na lista.
# Devemos acessar por sua "chave":
print(pessoa['nome'])
print(pessoa['idade'])

print('')

# Se precisarmos adicionar algum elemento, por exemplo o "país", basta fazermos:
pessoa['país'] = 'Brasil'
print(pessoa)

print('')

# Um dicionário possui um método para retornar as suas keys - keys()
print(pessoa.keys())
# Um dicionário também possui um método para retornar valores - values()
print(pessoa.values())

print('')

# Também podemos criar dicionários utilizando a função - dict()
a = dict(um=1, dois=2, três=3)
print(a)
