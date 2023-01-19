# cURL

## Contents

 - [Introdução ao cURL](#intro-to-curl)
 - Parâmetros do cURL:
   - [-H](#minus-h)
   - [-d](#minus-d)
   - [-i, -include](#minus-i)
   - [-I, -head](#minus-ii)
   - [-X, -request](#minus-x)
 - [Testando o cURL com JSONPlaceholder](#curl-testing)

---

<div id="intro-to-curl"></div>

## Introdução ao cURL

> https://curl.haxx.se/

O **cURL** é uma ferramenta para **CRIAR REQUISIÇÕES** em diversos protocolos **(incluindo HTTP, HTTPS e FTP, entre muitos outros)** e obter conteúdo remoto. Ele existe como ferramenta de linha de comando, e também como biblioteca (libcurl).

Uma requisição com **cURL** é composta:
  
 - Da palavra **curl**;
 - Da **URL** a qual você quer acessar;
 - E um ****conjunto de opções** que permitem você modificar qualquer coisa na requisição que será enviada.

---

<div id="minus-h"></div>

## -H

É um atalho para **Header**. Essa opção permite <u>adicionar</u> ou <u>substituir</u> campos do cabeçalho **HTTP**.

```python
curl -H "Content-Type: application/json"
```

---

<div id="minus-d"></div>

## -d

> É um atalho para **data**. É esta opção que vamos usar quando queremos **enviar dados para o servidor**.

**Exemplo com um payload JSON:**
```python
curl -d '{"name": "Rodrigo Leite"}'
```

---

<div id="minus-i"></div>

## -i, -include

Quando usamos esta opção, o **cURL** não mostrará apenas o corpo da resposta enviada do servidor, mas também o **cabeçalho/HEADER**.

---

<div id="minus-ii"></div>

## -I, -head

> Esta opção diz ao **cURL** para fazer uma requisição do tipo **HEAD** que irá **trazer apenas o cabeçalho do documento sem o corpo**.

---

<div id="minus-x"></div>

## -X, -request

> Esta opção **especifica qual verbo/método HTTP** que queremos usar.

**NOTE:**  
O padrão (default) é o **GET** mas nós podemos usar também:

 - GET
 - POST
 - PUT
 - PATCH
 - DELETE

---

<div id="curl-testing"></div>

## Testando o cURL com JSONPlaceholder
  
Um site bem interessante para quem está começando é o __JSONPlaceholder__. Esse site prover recursos no qual podemos utilizar como teste. A própria descrição do site deixa bem claro __"Fake Online REST API for Testing and Prototyping"__.  
  
> https://jsonplaceholder.typicode.com/  
  
Lá você tem vários recursos que podem ser utilizado para testes:  
  
__Resources:__  
```  
/posts  
/comments  
/albums  
/photos  
/todos  
/users  
```  
  
Por exemplo, se você clicar em __/users__ vão ter vários recursos usuários que você pode requisitar para teste:  
  
```json  
[
  {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
      "name": "Romaguera-Crona",
      "catchPhrase": "Multi-layered client-server neural-net",
      "bs": "harness real-time e-markets"
    }
  },
  {
    "id": 2,
    "name": "Ervin Howell",
    "username": "Antonette",
    "email": "Shanna@melissa.tv",
    "address": {
      "street": "Victor Plains",
      "suite": "Suite 879",
      "city": "Wisokyburgh",
      "zipcode": "90566-7771",
      "geo": {
        "lat": "-43.9509",
        "lng": "-34.4618"
      }
    },
    "phone": "010-692-6593 x09125",
    "website": "anastasia.net",
    "company": {
      "name": "Deckow-Crist",
      "catchPhrase": "Proactive didactic contingency",
      "bs": "synergize scalable supply-chains"
    }
  }
]  
```  
  
Vamos utilizar o __curl__ para fazer uma requisição HTTP e pegar o segundo usuário com o seu cabeçalho. Lembrando que para pegar o cabeçalho basta utilizar a opção __-i__:  
  
__Input:__  
```  
curl -i https://jsonplaceholder.typicode.com/users/2  
```  
  
__Output:__  
```json  
HTTP/1.1 200 OK
Date: Sat, 03 Mar 2018 19:43:51 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 509
Connection: keep-alive
Set-Cookie: __cfduid=d8758bb1707981074092ebd73e94f47a81520106231; expires=Sun, 03-Mar-19 19:43:51 GMT; path=/; domain=.typicode.com; HttpOnly
X-Powered-By: Express
Vary: Origin, Accept-Encoding
Access-Control-Allow-Credentials: true
Cache-Control: public, max-age=14400
Pragma: no-cache
Expires: Sat, 03 Mar 2018 23:43:51 GMT
X-Content-Type-Options: nosniff
Etag: W/"1fd-XTG63SYhaP/Uo6/vgmARnL3rpBk"
Via: 1.1 vegur
CF-Cache-Status: REVALIDATED
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Server: cloudflare
CF-RAY: 3f5e9829d9954c18-GRU

{
  "id": 2,
  "name": "Ervin Howell",
  "username": "Antonette",
  "email": "Shanna@melissa.tv",
  "address": {
    "street": "Victor Plains",
    "suite": "Suite 879",
    "city": "Wisokyburgh",
    "zipcode": "90566-7771",
    "geo": {
      "lat": "-43.9509",
      "lng": "-34.4618"
    }
  },
  "phone": "010-692-6593 x09125",
  "website": "anastasia.net",
  "company": {
    "name": "Deckow-Crist",
    "catchPhrase": "Proactive didactic contingency",
    "bs": "synergize scalable supply-chains"
  }
```  
  
Vejam que realmente nós pegamos o corpo(dados) do recurso "users/" com o "id=1" e seu cabeçalho HTTP. Outro exemplo, suponha que agora nós precisamos pegar só o cabeçalho(header) da requisição como fazer? Simples, basta utilizar a opção __-I__:  

__Input:__  
```  
curl -I https://jsonplaceholder.typicode.com/users/2  
```  
  
__Output:__  
```json  
HTTP/1.1 200 OK
Date: Sat, 03 Mar 2018 19:50:56 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 509
Connection: keep-alive
Set-Cookie: __cfduid=dfb642d31c1d639894d7c6342a90abd2a1520106656; expires=Sun, 03-Mar-19 19:50:56 GMT; path=/; domain=.typicode.com; HttpOnly
X-Powered-By: Express
Vary: Origin, Accept-Encoding
Access-Control-Allow-Credentials: true
Cache-Control: public, max-age=14400
Pragma: no-cache
Expires: Sat, 03 Mar 2018 23:50:56 GMT
X-Content-Type-Options: nosniff
Etag: W/"1fd-XTG63SYhaP/Uo6/vgmARnL3rpBk"
Via: 1.1 vegur
CF-Cache-Status: HIT
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Server: cloudflare
CF-RAY: 3f5ea2896b3a4b39-GRU  
```

---

**Rodrigo Leite -** *drigols*
