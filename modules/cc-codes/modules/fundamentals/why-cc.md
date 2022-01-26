# Por que C++?

## Conteúdo

 - [01 - Desempenho por $](#01)
 - [02 - Paradigmas do C++](#02)
 - [03 - Vantagens & Desvantagens](#03)

---

<div id="01"></div>

## 01 - Desempenho por $

Bem, não sei se vocês sabem, mas o **C++** é a melhor linguagem de programação quando estamos falando em ***desempenho por $*** - **What?**

Não entendeu? Veja a imagem abaixo para ficar mais claro:

![img](images/desempenho-01.png)  

Por exemplo:

 - ***Desempenho por Watts:***
   - **Bateria de um celular:**
     - Você não quer que o seu celular descarregue tão rápido não é?
     - Se, seu aplicativo demorar muito para processar mais bateria (energia) vai ser gasta.
   - **Resfriamento de um Data Center:**
     - Todo Data Center tem (ou deveria ter) um Sistema de Resfriamento que é acionado quando o processamento aumenta;
     - Ou seja, quanto mais rápido ele termina a tarefa (ou as tarefas), menos Resfriamento vai ser necessário (ou seja, menos energia).
 - ***Desempenho por Transistores:***
   - **Imagine a placa de um celular:**
     - Não dá para colocar o mesmo número de transistores de um computador pessoal;
     - Ou seja, para algumas aplicações o tamanho é limitado.
 - ***Desempenho por ciclo:***
   - **Imagine um sistema que detecta uma imagem (a partir de um celular):**
     - Nesse, caso o nosso sistema tem que aproveitar o máximo de ciclos possíveis, para dar uma melhor experiência interativa para o usuário.

---

<div id="02"></div>

## 02 - Paradigmas do C++

Bem, não são todos, mas o C++ é muito famoso por ter esses 3 paradigmas como filosofia:

![img](images/cc-paradigm.png)  

---

<div id="03"></div>

## 03 - Vantagens & Desvantagens

 - **Vantagens:**
   - **Portabilidade:**
     - Suponha que você escreva um programa no sistema operacional **Linux** e, por algum motivo aparente, mude para o sistema operacional **Windows**, você também poderá executar o mesmo programa no **Windows** sem nenhum erro. Este recurso prova ser de grande conveniência para o programador.
   - **Orientado a Objetos**
   - **Multi-Paradigma:**
     - *C++* é uma linguagem de programação multiparadigma. O termo *“Paradigma”* refere-se ao estilo de programação.
   - **Manipulação de baixo nível:**
     - Como o *C++* está intimamente associado ao *C*, que é uma linguagem procedural intimamente relacionada à linguagem de ***máquina***, o *C++* permite a manipulação de dados de baixo nível em um determinado nível. *Sistemas embarcados* e *compiladores* são criados com a ajuda de C++.
   - **Gerenciamento de Memória:**
     - *C++* dá ao programador o controle total sobre o gerenciamento de memória. Isso pode ser considerado um ativo e um passivo, pois aumenta a responsabilidade do usuário de gerenciar a memória em vez de ser gerenciada pelo coletor de lixo. Este conceito é implementado com a ajuda de **DMA (alocação dinâmica de memória)** usando *ponteiros*.
   - **Compatibilidade com C**
   - **Escalabilidade:**
     - A escalabilidade refere-se à capacidade de um programa de escalar. Isso significa que o programa *C++* é capaz de rodar tanto em pequena escala quanto em grande escala de dados. Também podemos criar aplicativos que consomem muitos recursos.
   - **Ampla gama de aplicações:**
     - *C++* é útil para fazer GUIs assim como jogos;
     - *C++* também é útil para desenvolver gráficos e simulação algébrica em tempo real
     - Portanto, *C++* é benéfico em todos os fluxos.
 - **Desvantagens:**
   - **Uso de Ponteiros:**
     - Ponteiros em C/C++ são um conceito relativamente difícil de entender e consome muita memória. O uso indevido de ponteiros como ponteiros selvagens pode fazer com que o sistema falhe ou se comporte de forma anômala.
   - **Ausência do Garbage Collector (Coletor de Lixo):**
     - Conforme discutido anteriormente, C++ dá ao usuário controle completo do gerenciamento da memória do computador usando DMA. O C++ não possui o recurso de um coletor de lixo para filtrar automaticamente dados desnecessários.
   - **Não permite funções de primeira classe**
   - **Inseguro:**
     - *C++* é inseguro em um sentido forte. A presença de ponteiros, variáveis globais, etc. é a principal razão por trás desses problemas de segurança. Isso significa que é possível corromper o programa inteiro usando apenas uma parte da memória como um tipo incorreto.

---

**REFERÊNCIAS:**  
[Curso de Programação C++ | Aula 00 - Introdução | Computador | Linguagem | Aprenda a Programar](https://www.youtube.com/watch?v=ZFaGnEKEjFs&t=5238s)
