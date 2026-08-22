# Diagramas de Venn (Conjuntos)

## Conteúdo

 - **Fundamentos:**
   - [`Como criar um conjunto que foi definido por compreensão?`](#ccucqfdpc)
 - [**Complementar de um conjunto**:](#complement-of-sets)
 - [**Diferença de Conjuntos**:](#diff-of-sets)
 - **Intersecção de Conjuntos:**
   - [`Como resolver um problema de "Intersecções de Conjuntos"`](#crupdic)
<!---
[WHITESPACE RULES]
- Same topic = "10" Whitespace character.
- Different topic = "200" Whitespace character.
--->






































































































<!--- ( Fundamentos ) --->

---

<div id="ccucqfdpc"></div>

## `Como criar um conjunto que foi definido por compreensão?`

Dados os conjuntos $A = \{x \mid x \text{ é par}\}$, $B = \{x \mid x \text{ é múltiplo de 3}\}$ e $C = \{x \mid x \text{ é múltiplo de 6}\}$, assinale uma relação correta entre $A$, $B$ e $C$.

- **A)** $A \cup B = C$
- **B)** $A \cap B = C$
- **C)** $A - B = C$
- **D)** $B - A = C$
- **E)** $A \cap C = B$

<details>

<summary>RESPOSTA</summary>

<br/>

Para resolver um problema de conjunto onde é dada uma regra (o conjunto é feito por compreensão), nós devemos montar esse conjunto a partir dessa regra:

- **A = { x ∣ x é par }**
  - A = {2, 4, 6, 8, 10, 12, 14, 16, 18, …}
- **B = { x ∣ x é múltiplo de 3 }**
  - B = { 3x1=3, 3x2=6, 3x3=9, 3x4=12, 3x5=15,  3x6=18,... }
  - B = {3, 6, 9, 12, 15, 18}
- **C = { x ∣ x é múltiplo de 6 }**
  - C = { 6x1=6, 6x2=12,  6x3=18,...}
  - C = {6, 12, 18}

> **NOTE:**  
> Como o intuito aqui não é apenas entender como montar um conjunto por compreensão (que segue uma regra), vamos resolver apenas a questão verdadeira.

Vejamos a alternativa **B**: $A ∩ B = C$

- A ∩ B = {6, 12, 18}  
- C = {6, 12, 18}
- A ∩ B = C (VERDADEIRO)

**Gabarito:** Letra B

</details>







































































































<!--- ( Complementar de um conjunto ) --->

---

<div id="complement-of-sets"></div>

## `Complementar de um conjunto`

> **Como resolver um problema de “complementar de conjuntos”?**

De acordo com as leis de De Morgan, o complementar da interseção é igual à união dos complementares. Assim, dado um conjunto universo U, seja $X^{c}$ o complementar de X em relação a U. Considere o conjunto universo: U = {1,2,3,4,5} e os subconjuntos: A = {1,2} e B = {2,4}. O conjunto $A^{c} \cup B^{c}$ é igual a:

- **A)** {3,5}
- **B)** {2,3,4,5}
- **C)** {1,2,3,4,5}
- **D)** {1,3,4,5}

<details>

<summary>RESPOSTA</summary>

<br/>

- **O conjunto universo é:**
  - U = {1,2,3,4,5}
- **Os subconjuntos dados são:**
  - A = {1,2}
  - B = {2,4}

Primeiro, calculamos os complementares em relação ao conjunto universo.

- **O complementar de A é formado pelos elementos de U que não pertencem a A:**
  - $A^{C} = \{3,4,5\}$
- **O complementar de B é formado pelos elementos de U que não pertencem a B:**
  - $B^{C} = \{1,3,5\}$

Agora fazemos a união desses conjuntos:

$A^{C} \cup B^{C} = \{3,4,5\} \cup \{1,3,5\}$
 
A união de dois conjuntos é feita reunindo todos os elementos de ambos os conjuntos **sem repetir**:

$A^{C} \cup B^{C} = \{1,3,4,5\}$
 
Portanto, o conjunto obtido é **{1,3,4,5}**.

**Gabarito:** Letra D.

</details>







































































































<!--- ( Diferença de Conjuntos ) --->

---

<div id="diff-of-sets"></div>

## `Diferença de Conjuntos`

> **Como resolver um problema de “diferença de conjuntos”?**

Sejam os conjuntos $A = \{-2, 0, 4, 5\}$, $B = \{-4, -3, 1, 5\}$ e $C = \{-1, 0, 3, 7\}$, a quantidade de elementos do conjunto solução da operação abaixo é um número natural que está entre:

$A - \left[(A-B) \cap (C-A)\right] \cup (B-A)$

- **A)** 0 e 2, incluindo 0 e 2.  
- **B)** 6 e 8, incluindo 6 e excluindo 8.  
- **C)** 3 e 5, excluindo 3 e incluindo 5.  
- **D)** 5 e 7, incluindo 5 e excluindo 7.  
- **E)** 7 e 9, excluindo 7 e incluindo 9.

<details>

<summary>RESPOSTA</summary>

<br/>

Antes de resolvermos essa operação, precisamos lembrar de algumas coisas (conceitos): 

 - A `união entre os conjuntos` **P** e **Q** é o conjunto formado por todos os elementos que pertencem a pelo menos um desses conjuntos;
 - A `intersecção entre os conjuntos` **P** e **Q** é o conjunto formado por todos os elementos que pertencem simultaneamente a esses conjuntos;
 - A `diferença (P−Q)` **entre dois conjuntos**, nessa ordem, é o conjunto formado por:
   - Todos os elementos que pertencem ao primeiro (P) conjunto e não pertencem ao segundo conjunto (Q);

Ótimo, agora vamos identificar os conjunto que nós temos:

- A = {−2, 0, 4, 5}
- B = {−4, −3, 1, 5}
- C = {−1, 0, 3, 7}

Agora, a partir dos conjuntos acima nós devemos resolver a expressão lógica abaixo:

${ A – [ (A − B) \cap (C − A) ] } \cup (B – A)$

Vamos começar criando as `diferenças` necessárias:
 
- (A−B) = {−2,0,4}
- (C−A) = {−1,3,7}
- (B−A) = {−4,−3,1}

Substituindo, na expressão lógica nós teremos:

$\{ \{−2,0,4,5\} – [ \{−2,0,4\} \cap \{−1,3,7\} ] \} \cup \{−4,−3,1\}$

Resolvendo a intersecção dos colchetes, ficaremos com:

$\{ {−2, 0, 4, 5} – ∅\} \cup \{−4, −3, 1\}$

Agora, resolvendo a diferença das chaves, vamos obter:

$\{−2, 0, 4, 5\} \cup \{−4, −3, 1\}$

Por último, fazendo a união dos conjuntos resultantes, ficaremos com o seguinte conjunto: 

$\{−4, −3, −2, 0, 1, 4, 5\}$
 
Notem que esse conjunto tem 7 elementos...
 
**Gabarito:** Letra B

</details>







































































































<!--- ( Intersecção de Conjuntos ) --->

---

<div id="crupdic"></div>

## `Como resolver um problema de "Intersecções de Conjuntos"?`

Em uma enquete, várias pessoas foram entrevistadas acerca de suas preferências em relação a três esportes:

 - Volei (V);
 - Basquete (B);
 - Tênis (T).

Cujos dados estão indicados na tabela a seguir:

 - **ESPORTE / N DE PESSOAS:**
   - V / 300
   - B / 260
   - T / 200
   - V e B / 180
   - V e T / 130
   - B e T / 100
   - V, B e T / 50
   - Nenhum / 40

De acordo com esses dados, é correto afirmar que, nessa enquete, o número de pessoas entrevistadas foi:

 - a) 400
 - b) 440 
 - c) 490
 - d) 530
 - e) 570


<details>

<summary>RESPOSTA</summary>

<br/>

Para resolver um problema de Intersecção de Conjuntos nós podemos seguir os seguintes passos:

**ADICIONAR OS ELEMENTOS QUE NÃO PERTENCEM A NENHUM GRUPO (CONJUNTO):**

- Nenhum = N(40)

**ADICIONAR O TOTAL DE ELEMENTOS DE CATEGORIA (CONJUNTO):**

- Volei = V(300)
- Basquete = B(260)
- Tênis = T(200)

Até o momento nós vamos ter a seguinte equação.

N(40) + V(300) + B(260) + T(200)

**⚠️ PROBLEMA:**  
Como nós também temos elementos que pertencem a mais de uma categoria (conjunto), como V/B, V/T e B/T, os elementos acima vão ser contados mais de uma vez.

**APLICAR O PRINCÍPIO DA EXCLUSÃO PARA ELEMENTOS REPITIDOS:**

Para resolver esse problema de contar várias vezes o mesmo elemento, vamos aplicar o `Princípio da Exclusão`, subtraindo os elementos que pertencem a dois conjuntos ao mesmo tempo (removendo a contagens duplicadas):

N(40) + V(300) + B(260) + T(200) - V/B(180) - V/T(130) - B/T(100)

**⚠️ PROBLEMA:**  
Agora, nós entramos em outro problema… os elementos que estavam em mais de um conjunto foram subtraídos duas vezes além da conta, então devem ser somados de volta.

**Para resolver esse problema, basta adicionar os elementos que pertencem a todas categorias (conjuntos):**

N(40) + V(300) + B(260) + T(200) - V/B(180) - V/T(130) - B/T(100) + V/B/T(50)

Logo, o resultado será:

40 + 300 + 260 + 200 - 180 - 130 - 100 + 50 = 440

Uma maneira inteligente de resolver é somar todos os positivos e subtrair dos negativos:

(40 + 300 + 260 + 200 + 50) - (-180 - 130 - 100)
             850            -       410

```bash
 850
-410
----
 440
```

Logo, o número de pessoas entrevistadas foi "440".

**Gabarito:** Letra B.

</details>

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
