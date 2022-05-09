# Recursos, URI & URL

## Contents

 - [01 - Recursos (Resources)](#resources)  
 - [02 - URI](#uri)  
 - [03 - URL](#url)  

---

<div id="resources"></div>
   
## 01 - Recursos (Resources)

> Recursos são elementos de informação, que através de um **identificador global** podem ser manipulados. Ou seja, recursos são <u>coisas</u>, que podem ser manipuladas através de um __ID__.

**Veja o exemplo de um recurso *usuário* (user):**

```python
recurso: Usuário    id: www.meusite.com/user
```

No exemplo acima temos duas coisas importantes a observar:  
  
 - **Primeiro:**
   - O recurso (resource) é **"usuário"**.
 - **Segundo:**
   - O identificador global é **"/user"**.

> A nomeação de um recurso sempre é formada por um s**substantivo**, nunca um **verbo**.

Isso porque um recurso é sempre algo que você deseja manipular, exemplo:

 - Um usuário.
 - Uma empressora.

---

<div id="uri"></div>

## 02 - URI

> **URI (Uniform Resource Identifier)**, em português significa *"Identificador Uniforme de Recursos"*, é uma cadeia de caracteres compacta usada para **identificar ou denominar um recurso na Internet**.

**Por exemplo, veja o recurso abaixo:**

```python
recurso: Usuário    uri: www.meusite.com/user
```

**NOTE:**  
Por exemplo, lembra que nós temos o recurso __/user__? Então, com a __URI__ nós podemos afirmar que unicamente esse recurso está em meu site. <u>Pode ser que haja esse recurso "/user" em outros sites, mas esse em questão está no meu site</u>.

---

<div id="url"></div>

## 03 - URL  

> **URL (Uniform Resource Locator)**, ou em português, *"Localizador-Padrão de Recursos"*, é o **endereço de um recurso** disponível em uma rede.

**Por exemplo veja o recursos abaixo:**

```python
Ex: recurso: Impressora
url/uri: http://www.meusite.com/print
```
  
Vejam que no exemplo acima nós temos 3 partes importantes:  
  
 - **Recurso:** /print (impressora);  
 - **URI:** www.meusite.com;  
 - **URL:** http://www.meusite.com/print
   - **endereço de um recurso** disponível em uma rede.

Então, uma **URL** nada mais é do que a junção: <u>recurso</u> + <u>URI</u> + <u>protocolo(http/https)</u> = <u>URL</u>.

---

**Rodrigo Leite -** *drigols*
