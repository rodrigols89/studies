# Feature Engineering

## Conteúdo

 - [01 - Introdução ao Feature engineering](#intro-to-fe)
 - [02 - O que são Features?](#whats-f)
 - [03 - Selecionando Features com maior correlação com a variável target](#corr)
 - [04 - Por que utilizar feature engineering?](#why-use-fe)
 - **05 - Algumas técnicas de Feature Engineering:**
   - [05.1 - Criação de Features](#feature-creation)
   - [05.2 - Transformações de Features](#features-transformation)
   - [05.3 - Seleção de Features](#features-selection)

---

<div id="intro-to-fe"></div>

## 01 - Introdução ao Feature engineering

Para quem nunca ouviu falar sobre o termo **"Feature engineering"** pode ser um pouco complicado, mas veja as definições (não formais) abaixo:

> **Feature engineering** é o processo no qual é possível **transformar**, **extrair** e **criar novas features** a partir dos `dados disponíveis`, com o objetivo de melhorar o desempenho dos algoritmos de Machine Learning.

> **Feature engineering** não se trata apenas de selecionar boas features para um modelo preditivo. Esse processo também abrange **transformações matemáticas** nas features existentes para extrair o máximo potencial dos dados e **criação de novas features**.

> **Feature engineering** é o termo utilizado para definir um conjunto de técnicas utilizado na **criação** e **manipulação** de `features (recursos)`, tendo como objetivo desenvolver um bom modelo de Machine Learning.

---

<div id="whats-f"></div>

## 02 - O que são Features?

Praticamente todos os algoritmos de Machine Learning possuem **entradas** e **saídas**. As entradas são formadas por colunas de dados estruturados, onde cada coluna recebe o nome de feature, também conhecido como variáveis independentes ou atributos.

As **saídas**, por sua vez, são chamadas de **variáveis dependentes** ou **target**, e essa é a variável que estamos tentando prever.

---

<div id="corr"></div>

## 03 - Selecionando Features com maior correlação com a variável target

Bem, eu não sei se vocês sabem, mas:

> Quanto maior a correlação entre uma **feature** e a variável que se quer **prever (target)**, mais importante essa feature é. 

**NOTE:**  
Mas precisamos tomar alguns cuidados. Por exemplo: se uma feature distância é importante e ela está em quilômetros, também podemos considerar inseri-la em metros no modelo. Porém, isso vai fazer com que o modelo considere essa informação como sendo mais relevante do que realmente é, já que ele a recebeu duas vezes.

**NOTE:**  
Portanto, o **feature engineering** não se trata apenas de selecionar boas features, esse processo também abrange a **transformações matemáticas** nas features existentes para extrair o máximo potencial dos dados e criação de novas features.

**NOTE:**  
Criar novas features a partir das existentes é ainda mais importante quando temos poucos dados, pois modelos que utilizam poucas instâncias tendem a realizar **overfiting**. 

---

<div id="why-use-fe"></div>

## 04 - Por que utilizar feature engineering?

Pense que você vai fazer sua receita favorita. Você vai precisar dos seguintes ingredientes:

 - Tomate;
 - Alho;
 - Carne;
 - Macarrão.

Então, você coloca tudo dentro da panela:

 - Os tomates;
 - Alhos inteiros e com casca;
 - Carne crua;
 - Massa com o plástico.

**NOTE:**  
Com certeza o resultado final vai passar longe de um **macarrão à bolonhesa**. Você vai precisar descascar, cortar, cozinhar a carne, retirar a massa do pacote...

**NOTE:**  
O mesmo acontece com os recursos: eles precisam ser **pré-processados** para colocá-los no modelo preditivo e obter um bom resultado final. Seu modelo não vai pegar os dados cheio de valores faltantes, variáveis duplicadas, inconsistências e resolver tudo em um passe de mágica.

**NOTE:**  
Outro motivo para se preocupar é que conforme o tempo passa, tendemos a ter mais dados disponíveis, o que torna a seleção de quais desses dados são mais relevantes ainda mais trabalhosa e, ao mesmo tempo, cada vez mais importante, pois vai ser cada vez mais fácil selecionar features erradas em um mar de dados.

---

<div id="feature-creation"></div>

## 05.1 - Criação de Features

A primeira coisa a se fazer ao começar um processo de **Feature Engineering** é:

> Entender todas as variáveis preditoras importantes que precisam ser incluídas no modelo.

Depois, você deve se fazer as seguintes perguntas:

 - Eu tenho esses dados?
 - Consigo criar esses dados?

**NOTE:**  
Um dos erros mais comuns é focar nos dados disponíveis ao invés de se questionar quais dados são necessários. Esse equívoco faz com que variáveis essenciais para o negócio sejam deixadas de lado, pois não existem nos dados.

**NOTE:**  
Se muitas dessas variáveis essenciais não estiverem disponíveis para processamento, vale voltar para a etapa de coleta de dados. Criar novas features pode trazer à tona informações que são de extrema importância, mas não estavam explícitas nos dados.

---

<div id="features-transformation"></div>

## 05.2 - Transformações de Features

A **transformação de features** leva em consideração o tipo de dados e sua compatibilidade com o modelo e também se o tipo da variável passa a maior quantidade de informação possível. Algumas técnicas de transformação mais comuns são:

 - Missing Values;
 - Manipulação de outliers;
 - Binning;
 - One-hot encoding;
 - Grouping...

---

<div id="features-selection"></div>

## 05.3 - Seleção de Features

> Ao final da transformação das features, é preciso escolher quais delas vão para o modelo, pois às vezes possuímos recursos demais e o modelo de previsão não vai conseguir aguentar todas as variáveis possíveis, ou o tempo de treinamento do modelo vai aumentar muito.

**NOTE:**  
Passar todas as features para o modelo pode fazer ele considerar relações que não existem e, até mesmo, considerar uma feature como mais importante do que ela realmente é. Por exemplo, se você tem uma grande quantidade de dados, algumas coincidências podem ter ocorrido e ficaram guardadas nos dados, e a máquina pode acabar considerando isso como uma regra com baixa correlação.

**NOTE:**  
Essa etapa é um pouco exaustiva e manual, mas vai ser preciso testar várias combinações de features e medir qual gera a maior acurácia do modelo preditivo.

---

**REFERÊNCIAS:**  
[Feature Engineering: Preparando dados para o aprendizado de máquina](https://ateliware.com/blog/feature-engineering)  

---

**Rodrigo Leite -** *drigols*
