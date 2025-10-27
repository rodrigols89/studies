# Estatística

## Conteúdo

 - **Fundamentos:**
   - `Ninguém cria nada se não tiver um problema (Profa. Adriana Silva).`
   - [`Qual a diferença de um Modelo (equação) Deterministico vs. Estatístico?`](#deterministic-vs-statistic-model)
   - [`Defina (com exemplos) o que são dados, observações, variáveis e contexto?`](#data-observation-variable-context)
   - [`Popoulação vs. Amostra`](#population-vs-sample)
   - [`Parâmetro vs. Estatística`](#parameter-vs-statistic)
 - [**REFERÊNCIAS**](#ref)
<!---
[WHITESPACE RULES]
- Same topic = "10" Whitespace character.
- Different topic = "200" Whitespace character.
--->









































































































<!--- ( Fundamentos ) --->

---

<div id="deterministic-vs-statistic-model"></div>

## `Qual a diferença de um Modelo (equação) Deterministico vs. Estatístico?`

> **Você saberia me responder qual a diferença entre em um *Modelo (Equação) Determinístico* e um *Estatístico*?**

<details>

<summary>RESPOSTA</summary>

<br/>

Em resumo:

 - Um **Modelo (Equação) Determinístico** é *sempre a mesma coisa*, *não existe uma mudança*, *não existe uma variação*:
   - A minha equação é perfeita;
   - Onde acontecer muito isso? Na física:
     - "Se eu jogar uma pedrinha em uma posição x, quanto tempo ela levar para chegar no chão?"
     - Bem, se você souber o peso do objeto e a distância do projeto você consegue "determinar" o tempo.
     - **NOTE:** Ou seja, é sempre o mesmo modelo (equação) que sempre funciona sem variabilidade.
 - Um **Modelo (Equação) Estatístico** é aquele que por mais que eu queira eu não consigo ter uma equação precisa o tempo inteiro:
   - Vai ter momentos que nós vamos errar um pouco para cima; vai ter momento que nós vamos errar um pouco para baixo.
   - **NOTE:** Ou seja, um modelo (equação) estatístico é aquele que carrega um `erro`.

</details>










---

<div id="data-observation-variable-context"></div>

## `Defina (com exemplos) o que são dados, observações, variáveis e contexto?`

> **Qual a diferença entre *"dados"*, *"observações"*, *"variáveis"* e *"contexto"*?**

<details>

<summary>RESPOSTA</summary>

<br/>

Bem, em resumo:

 - **Dados:**
   - Os dados também conhecidos como *"Base de Dados"*, tem.
     - `Linhas:`
       - Linhas são os nossos `objetos de estudo` que nada mas são do que as nossas `observações`.
       - Por que `objeto de estudo`? Porque é aquele *"negócio"* que eu estou interessado em gerar alguma análise.
       - Que "negócio" é esse? Pode ser um indivíduo, um produto, pode ser qualquer coisa (vai depender do contexto).
     - `Colunas:`
       - São `informações` sobre os nossos `objeto de estudo`.
       - Isso é o que nós conhecemos na estatística/programação/matématica de `variáveis/atributos/features`.
 - **Observações:**
   - São as entidades a respeito das quais se coletam os dados *(objeto de estudo)*.
 - **Variáveis:**
   - Variáveis são aquilo que descrevem o nosso `objeto de estudo`.
 - **Contexto:**
   - É a `lógica desses dados`, sem isso você não consegue interpretar nada! Tudo é Contexto!

</details>










---

<div id="population-vs-sample"></div>

## `Popoulação vs. Amostra`

> **Qual a diferença entre *"população"* e *"amostra"*?**

<details>

<summary>RESPOSTA</summary>

<br/>

Bem, em resumo:

 - **Uma População:**
   - É o *"todo do seu estudo"*.
   - É o *"todo do seu problema"*.
   - É o *"todo do seu contexto"*.
   - EXEMPLO-01:
 - **Uma Amostra:**
   - É um *"pedaço desse todo"*.

Vejam a tabela abaixo para ficar mais claro:

| **Situação**                                                             | **População (conjunto total de interesse)**              | **Amostra (parte representativa da população)**               |
| ------------------------------------------------------------------------ | -------------------------------------------------------- | ------------------------------------------------------------- |
| 1️⃣ Pesquisa sobre hábitos alimentares de estudantes de uma universidade | Todos os estudantes matriculados na universidade         | 200 estudantes escolhidos aleatoriamente de diferentes cursos |
| 2️⃣ Estudo sobre a renda familiar em uma cidade                          | Todas as famílias residentes na cidade                   | 300 famílias selecionadas de forma aleatória por bairro       |
| 3️⃣ Avaliação do desempenho de alunos do ensino médio em matemática      | Todos os alunos do ensino médio de um estado             | 10 escolas sorteadas e todos os alunos dessas escolas         |
| 4️⃣ Pesquisa de satisfação de clientes de uma empresa                    | Todos os clientes que compraram na empresa no último ano | 500 clientes que responderam a um questionário online         |
| 5️⃣ Análise da produtividade de uma fábrica                              | Todos os funcionários da fábrica                         | 50 funcionários escolhidos de diferentes turnos de trabalho   |

#### 💡 Resumidamente

 - **População** → O todo que queremos estudar.
 - **Amostra** → Uma parte desse todo, usada quando não é viável estudar todos os elementos.

</details>










---

<div id="parameter-vs-statistic"></div>

## `Parâmetro vs. Estatística`

> **Qual a diferença entre *"parâmetro"* e *"estatística"*?**

<details>

<summary>RESPOSTA</summary>

<br/>

Em resumo:

 - **Parâmetro** → É uma medida usada para descrever uma característica da População.
 - **Estatística** → Vem de uma *amostra*.

#### 🎯 1️⃣ Conceito básico

| Termo           | Definição                                                                                                   | Onde se aplica |
| --------------- | ----------------------------------------------------------------------------------------------------------- | -------------- |
| **Parâmetro**   | É uma **medida numérica** que descreve uma **característica da população** (ou seja, do todo).              | População      |
| **Estatística** | É uma **medida numérica** que descreve uma **característica da amostra** (ou seja, da parte que estudamos). | Amostra        |

#### 📊 2️⃣ Exemplo prático

Imagine que queremos saber a média de altura dos estudantes de uma universidade:

| Situação                                                                | Tipo            | Descrição                                                                              |
| ----------------------------------------------------------------------- | --------------- | -------------------------------------------------------------------------------------- |
| A **média verdadeira da altura** de todos os estudantes da universidade | **Parâmetro**   | Representa o valor real da população (geralmente desconhecido, pois não medimos todos) |
| A **média de altura** dos 200 estudantes escolhidos aleatoriamente      | **Estatística** | É o valor calculado a partir da amostra — usado para **estimar o parâmetro**           |

🧠 3️⃣ Outros exemplos

| Exemplo                                                  | Parâmetro                             | Estatística                                           |
| -------------------------------------------------------- | ------------------------------------- | ----------------------------------------------------- |
| Percentual de eleitores que votariam em um candidato     | Percentual real de todos os eleitores | Percentual obtido em uma pesquisa com 1.000 eleitores |
| Média de renda mensal de todas as famílias de uma cidade | Média verdadeira da cidade            | Média calculada com base em 300 famílias pesquisadas  |
| Desvio padrão do peso de todos os alunos de uma escola   | Desvio padrão real (de toda a escola) | Desvio padrão dos 50 alunos medidos                   |

> **E como diferenciar um parâmetro de uma estatística em um estudo?**

É comum usarmos letras gregas para representar parâmetros e letras latinas para representar estatísticas:

![img](images/parameter-vs-statistic-01.png)  

</details>










































































































<!--- ( REFERÊNCIA ) --->

---

<div id="ref"></div>

## REFERÊNCIA

 - **Cursos:**
   - [Licenciatura - Matemática](https://www.faculdadeunica.com.br/graduacao/ead/matematica-3080)
   - [Entendendo Estatística Divertidamente](https://lp.asn.rocks/eed-a)

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

<details>

<summary></summary>

<br/>

RESPOSTA

```bash

```

![img](images/)  

</details>
