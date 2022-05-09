# REST (Constraints)

## Contents

 - [O que é REST?](#whats-rest)
 - Constraints:
   - [01 - Cliente-Servidor (Client–Server)](#client–server)
   - [02 - Stateless (Sem estado)](#stateless)
   - [03 - Cache (Cacheable)](#cacheable)
   - [04 - Interface Uniforme (Uniform Interface)](#uniform-interface)
   - [05 - Sistema em Camadas (Layered System)](#layered-system)
   - [06 - Código Sob Demanda](#code-on-cemand)




---

<div id="whats-rest"></div>

## O que é REST?

> Antes de iniciar os estudos sobre **REST <u>Constraints</u>** vamos entender como tudo isso começou e foi criado.

O termo transferência de estado representacional **(REST (Representational State Transfer)** foi introduzido e definido no ano de 2000 através de uma tese de Ph.D do Cientista **Roy Fielding**, um dos principais autores da especificação do protocolo **HTTP**.  
  
O intuito geral da tese era a formalização de um conjunto de melhores prática denominadas <u>constraints</u>. Essas <u>constraints</u> tinham como objetivo determinar a forma na qual padrões como **HTTP** e **URI** deveriam ser modelados, aproveitando de fato todos os recurso oferecidos pelos mesmos.  

---

<div id="client–server"></div>

## 01 - Cliente-Servidor (Client–Server)

> A principal característica dessa constraint é **separar as responsabilidades** de diferentes partes de um sistema.
  
 - **Front-end:** Client  
 - **Back-End:** Servidor  
  
Essa divisão pode-se dar de diversas formas, iniciando por exemplo com uma separação entre mecanismos de **interface do usuário** e o **back-end** da aplicação.

> Isso nos permite a evolução e **escalabilidade** destas responsabilidades **de forma independente**.

---

<div id="stateless"></div>

## 02 - Stateless (Sem estado)

Essa característica propõe que **cada requisição** ao servidor **não deve ter ligação com requisições <u>ANTERIORES</u> ou <u>FUTURAS</u>**, ou seja, cada requisição deve conter todas as informações necessárias para que ela seja tratada com sucesso pelo servidor.

---

<div id="cacheable"></div>

## 03 - Cache (Cacheable)

> Para uma melhor performance, um sistema **REST** deve **permitir** que suas respsotas sejam passíveis de **cache**.

---

<div id="uniform-interface"></div>

## 04 - Interface Uniforme (Uniform Interface)

> Bastante esforço deve ser feito para que o sistema possua uma **interface modelada** seguindo alguns padrões importantes.

Quando se fala sobre uma interface, os elementos abaixo devem ser considerados:  
  
 - Recursos.
 - Mensagens autodescritivas
 - Hypermedia...

---

<div id="layered-system"></div>

## 05 - Sistema em Camadas (Layered System)

Com o intuito de permitir que a escalabilidade necessária para grandes sistemas distribuídos, um sistema **REST** deve ter a capacidade de adicionar elementos intermediários e que sejam totalmente transparentes para seus clientes.  
  
> Ex: Balanceador de carga  
  
**NOTE:**  
Por exemplo, suponha que nós temos um sistema que recebe inúmeras requisições, seria importante criar um **balanceador de carga** para dizer:

 - Não, esse acesso aqui que esse IP de determinador computador fez vai ser resolvidor a partir de determinador servidor;
 - E na mesma hora chega outra requisição, então ele diz você aqui vai ser tratado por esse outro servidor.

---

<div id="code-on-cemand"></div>

## 06 - Código Sob Demanda

> **Código sob demanda** é a única constraint **REST** <u>opcional</u>.  
  
A ideia é aumentar a flexibilidade dos clientes, como por exemplo um código JavaScript que só é baixado quando uma determinada página é carregada.

---

**Rodrigo Leite -** *drigols*
