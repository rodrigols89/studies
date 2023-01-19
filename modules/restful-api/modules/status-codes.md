# Status Codes

## Contents

 - [01 - Introdução aos Status Codes](#intro-to-status-codes)
 - [02 - Status Codes e seus significados](#status-codes-list)

---

<div id="intro-to-status-codes"></div>

## 01 - Introdução aos Status Codes

Depois que uma **API REST** recebe e processa uma solicitação **HTTP**, ela retornará uma resposta **HTTP**. Incluído nesta resposta está um <u>código de status HTTP</u>. Este código fornece informações sobre os resultados da solicitação.

**NOTE:**  
Um aplicativo que envia solicitações para a **API** pode verificar o código de status e realizar ações com base no resultado. Essas ações podem:

 - Incluir o tratamento de erros;
 - Ou a exibição de uma mensagem de sucesso para um usuário.

---

<div id="status-codes-list"></div>

## 02 - Status Codes e seus significados

Abaixo está uma lista dos códigos de status mais comuns retornados pelas **APIs REST**:


| Code   | Meaning                 | Description
|--------|-------------------------|---------------------------------------------------------------------------------
| 200	   |  OK                     |	The requested action was successful.
| 201	   | 	Created                |	A new resource was created.
| 202	   | 	Accepted               |	The request was received, but no modification has been made yet.
| 204	   | 	No Content             |	The request was successful, but the response has no content.
| 400	   | 	Bad Request            |	The request was malformed.
| 401	   | 	Unauthorized           |	The client is not authorized to perform the requested action.
| 404	   | 	Not Found              |	The requested resource was not found.
| 415	   | 	Unsupported Media Type |	The request data format is not supported by the server.
| 422	   | 	Unprocessable Entity   |	The request data was properly formatted but contained invalid or missing data.
| 500	   | 	Internal Server Error  |	The server threw an error when processing the request.

**NOTE:**  
Esses dez códigos de status representam apenas um pequeno subconjunto dos [códigos de status HTTP](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) disponíveis. Os códigos de status são numerados com base na categoria do resultado:

| Code range | Category
|------------|----------------------
| 2xx        | Successful operation
| 3xx        | Redirection
| 4xx	       | Client error
| 5xx	       | Server error

**NOTE:**  
Os códigos de status **HTTP** são úteis ao trabalhar com **APIs REST**, pois muitas vezes você precisará executar uma lógica diferente com base nos resultados da solicitação.

---

**Rodrigo Leite -** *drigols*

