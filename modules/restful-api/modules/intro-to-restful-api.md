# Introdução ao RESTFul API

## Contents

 - [01 - Introdução a API](#intro-to-api)
 - [02 - Formatos mais comuns para representar dados (objetos) uma API (XML, JSON, YAML)](#api-representation)
 - [03 - Introdução ao REST](#intro-to-rest)
 - [04 - REST x RESTful](#rest-x-restful)








---

<div id="intro-to-api"></div>

## 01 - Introdução a API

> Para começar vamos dar uma breve introdução sobre **API** que é um acrônimo do inglês **Application Programming Interface** (Em português, significa Interface de Programação de Aplicações)

Uma **API** trata-se de um conjunto de rotinas e padrões estabelecidos e documentados por uma aplicação **"A"**, para que outras aplicações consigam utilizar as funcionalidades desta aplicação **"A"**, sem precisar conhecer detalhes da implementação do software.  

Desta forma, entendemos que as __APIs__ permitem uma <u>interoperabilidade</u> entre aplicações. Em outras palavras, a comunicação entre aplicações e entre os usuários.  
  
__Exemplo de API: Twitter Developers__  
  
![restful-api](images/api-01.png)

---

<div id="api-representation"></div>

## 02 - Formatos mais comuns para representar dados (objetos) uma API (XML, JSON, YAML)

Como nós sabemos uma **API** permite a **interoperabilidade entre usuários e aplicações**, isso reforça ainda mais a importância (necessidade) de pensarmos em algo padronizado e, de preferência, de fácil representação e compreensão por humanos e máquinas.

Os formatos mais comuns de representar dados (objetos) em uma **API** são:

 - XML
 - JSON
 - YAML

Veja esses três exemplos abaixo:  

**XML**  
```xml
<endereco>  
  <rua>  
    Rua Pedro  
  </rua>  
  <cidade>  
    Rodrigo Leite  
  </cidade>  
</endereco>  
```

**JSON**  
```json  
{ 
  "endereco":  
  {  
    "rua": "Rua Pedro",  
    "cidade": "Rodrigo Leite"  
  }  
}  
```

**YAML**
```yaml  
endereco:  
rua: rua Pedro  
cidade: Rodrigo Leite  
```  
  
Qual deles você escolheria para informar o endereço em uma carta? Provavelmente o último, por ser de fácil entendimento para humanos, não é mesmo? Contudo, as 3 representações são válidas, pois nosso entendimento final é o mesmo, ou seja, a semântica é a mesma.  
  
 - Por outro lado, você deve concordar comigo que a primeira representação (formato XML) é mais verbosa, exigindo um esforço extra por parte de quem está escrevendo;
 - No segundo exemplo (formato JSON) já é algo mais leve de se escrever;
 - Já o último (formato YAML), é praticamente como escrevemos no dia a dia.

---

<div id="intro-to-rest"></div>

## 03 - Introdução ao REST

> **REST** significa **Representational State Transfer**. Em português, "Transferência de Estado Representacional".

**NOTE:**  
Trata-se de uma abstração da arquitetura da Web. Resumidamente, o **REST** consiste em **Princípios**, **Regras** e **Constraints** que, quando seguidas, permitem a criação de um projeto com interfaces bem definidas. Desta forma, permitindo, por exemplo, que aplicações se comuniquem.

---

<div id="rest-x-restful"></div>

## 04 - REST x RESTful  
  
Existe uma certa confusão quanto aos termos **REST** e **RESTful**. Entretanto, ambos representam os mesmo princípios. A diferença é apenas gramatical.

> Em outras palavras, sistemas que utilizam os <u>princípios</u> **REST** são chamados de **RESTful**.  
  
 - **REST:** Conjunto de <u>princípios</u> de arquitetura;  
 - **RESTful:** Capacidade de determinado sistema aplicar os <u>princípios</u> **REST**.

**NOTE:**  

> Logo, uma **RESTFul API** é uma **API** que tem capacidade de aplicar os <u>princípios</u> **REST**.

---

**Rodrigo Leite -** *drigols*
