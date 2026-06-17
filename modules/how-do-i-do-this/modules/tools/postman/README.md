# Postman

## Conteúdo

 - [`Começando com o Postman`](#getting-postman)
 - [`Testando um método POST (Cadastrando um Gestor)`](#testing-post-method)
 - [`Testando um método GET (Listando um Gestor)`](#testing-get-method)
 - [`Testando um método POST que recebe um argumento`](#testing-post-method-with-argument)
<!---
[WHITESPACE RULES]
- "20" Whitespace character.
--->




















---

<div id="getting-postman"></div>

## `Começando com o Postman`

- Abra o Postman.
- Clique em:
  - New Request
- Escolha:
  - GET
  - POST
  - PUT
  - DELETE
- Dependendo do endpoint:
  - Digite a URL:
    - http://localhost:8000/health
- Clique em:
  - Send




















---

<div id="testing-post-method"></div>

## `Testando um método POST (Cadastrando um Gestor)`

Imagine que nós temos um endpoint salva um novo gestor no banco de dados:

Comece selecionando o método POST no Postman:

```text
POST
```

Depois adicione a aqui que vai receber a requisição:

```text
http://localhost:8000/gestores
```

Agora clique em:

 - Body
   - raw
     - Dentro deve ter um checkbox, você selecionar JSON.

Agora, você deve enviar um JSON válido, por exemplo:

```json
{
  "nome": "Izoneide Fidelis Virgínio",
  "telefone": "+55 83 9835-4221",
  "escola": "Rafael Clementino (Sítio Coelho)",
  "pode_pedir_gas": true,
  "pode_pedir_agua": true
}
```

**OUTPUT:**
```json
{
    "id":21,
    "nome":"João de Deus",
    "telefone":"+55 83 0000-4221",
    "escola":"Rafael Clementino (Sítio Coelho)",
    "pode_pedir_gas":true,
    "pode_pedir_agua":true,
    "ativo":true
}
```

> **Informação importante:**  
> `"id": 21`, você precisará dele para criar pedidos.




















---

<div id="testing-get-method"></div>

## `Testando um método GET (Listando um Gestor)`

> Agora vamos consultar todos os gestores cadastrados.

Imagine que nós temos um endpoint que lista todos os gestores cadastrados no banco de dados:

Comece selecionando o método GET no Postman:

```text
GET
```

Depois adicione a aqui que vai receber a requisição:

```text
http://localhost:8000/gestores
```

Agora é só clicar em `"Send"`.




















---

<div id="testing-post-method-with-argument"></div>

## `Testando um método POST que recebe um argumento`

> Vamos imaginar que nós temos um endpoint precisa do ID de um gestor existente para fazer um pedido.

Comece selecionando o método POST no Postman:

```text
POST
```

Depois adicione a URL aqui que vai receber a requisição:

```text
http://localhost:8000/pedidos
```

Agora clique em:

 - Body
   - raw
     - Dentro deve ter um checkbox, você selecionar JSON.

Agora, você deve enviar um JSON válido, por exemplo:

**Exemplo 1 - Pedido de gás**
```json
{
    "gestor_id": 1,
    "comando": "/gas"
}
```

**Exemplo 2 - Pedido de água**
```json
{
    "gestor_id": 1,
    "comando": "/agua"
}
```

**Resposta Esperada algo parecido com:**
```json
{
    "id": 1,
    "gestor_id": 1,
    "tipo": "GAS",
    "quantidade": 1,
    "criado_em": "2026-06-02T12:30:00"
}
```

> **NOTE:**  
> Agora se você fizer um novo pedido de água ou gás para esse gestor no mesmo dia não vai funcionar: `{"detail":"A 'agua' request has already been made today."}`

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**
