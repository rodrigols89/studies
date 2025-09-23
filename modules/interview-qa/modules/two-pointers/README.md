# Two Pointers

## Contents

 - **Fundamentals:**
   - [`O que é, quanto (ou não) utilizar, vantagem e desvantagem da técnica "Two Pointers"?`](#oqvdt)
 - **Two Pointers (same direction):**
 - **Two Pointers (opposite ends):**
 - **Fast and Slow Pointers (Floyd's Tortoise and Hare):**
   - [`141. Linked List Cycle`](#141-llc)
<!---
[WHITESPACE RULES]
- Same topic = "10" Whitespace character.
- Different topic = "200" Whitespace character.
--->









































































































<!--- ( Fundamentals ) --->

---

<div id="oqvdt"></div>

## `O que é, quanto (ou não) utilizar, vantagem e desvantagem da técnica "Two Pointers"?`

> **O que é, quanto (ou não) utilizar, vantagem e desvantagem da técnica "Two Pointers"?**

<details>

<summary>RESPOSTA</summary>

<br/>

### 📌 O que é "Two Pointers"?

> É uma técnica onde usamos dois índices (ponteiros) para percorrer uma lista/array/string, em vez de apenas um.

Esses ponteiros podem se mover em direções diferentes:

 - Ambos indo para frente;
 - Um do início e outro do fim;
 - Um rápido e outro lento.

> **NOTE:**  
> 👉 Isso geralmente ajuda a reduzir a complexidade de um algoritmo de **O(n²)** para **O(n)** em problemas que envolvem busca, pares ou subsequências.

### 📌 Quando utilizar?

Usamos A técnica **"Two Pointers"** quando:

 - **O problema envolve arrays ou strings ordenados (ou que podem ser ordenados).**
   - Ex: encontrar soma de dois números que dá um alvo (Two Sum em array ordenado).
 - **Precisa buscar pares ou subsequências que satisfazem uma condição:**
   - Ex: verificar se uma string é palíndromo.
 - **Problemas de janelas deslizantes (sliding window) → encontrar subarray com certas condições:**
   - Ex: maior substring sem caracteres repetidos.
 - **Quando há necessidade de comparar elementos do começo e do fim de uma estrutura.**

### 📌 Quando não utilizar?

Evite utilizar a técnica **"Two Pointers"** quando:

 - **Os dados não permitem um movimento "ordenado" dos ponteiros**
   - Ex: se o array não está ordenado e ordenar mudaria a resposta.
 - **Quando o problema exige backtracking, recursion ou brute force inevitável:**
   - Ex: combinações complexas ou problemas de grafos.
 - **Se não é possível determinar um critério claro de movimento dos ponteiros.**
   - *(Se você ficar sem saber se anda com o ponteiro da esquerda ou da direita, talvez o padrão não seja adequado.)*

### 📌 Vantagens

 - **Reduz a complexidade:** muitos problemas que seriam `O(n²)` passam para `O(n)`.
 - **Menos memória extra:** geralmente feito em place (sem precisar de estruturas extras).
 - **Código limpo:** uma vez que você entende o padrão, fica mais fácil de implementar.

### 📌 Desvantagens

 - **Difícil de identificar:** no começo, nem sempre fica claro quando aplicar.
 - **Depende de ordenação:** muitos problemas exigem array ordenado. Isso pode custar `O(n log n)`.
 - **Fácil errar nos índices:** se não tomar cuidado, dá bug *(off-by-one errors)*.

</details>


















































































































<!--- ( Fast and Slow Pointers (Floyd's Tortoise and Hare) ) --->

---

<div id="141-llc"></div>

## `141. Linked List Cycle`

> Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

 - There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer:
   - Existe um ciclo em uma lista encadeada se houver algum nó na lista que possa ser alcançado novamente seguindo continuamente o ponteiro `next`.
 - Internally, `pos` is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
   - Internamente, `pos` é usado para denotar o índice do nó ao qual o ponteiro`next` da cauda está conectado.
   - **Observe que `pos` não é passado como parâmetro**.
 - Return `true` if there is a cycle in the linked list. Otherwise, return false.
 - **Constraints:**
   - The number of the nodes in the list is in the range [0, 104].
   - `-105 <= Node.val <= 105`
   - `pos` is `-1` or a valid index in the linked-list.

**Example 1:**  
![img](images/141-llc-01.png)  

```bash
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

**Example 2:**  
![img](images/141-llc-02.png)  

```bash
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

**Example 3:**  
![img](images/141-llc-03.png)  

```bash
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

<details>

<summary>RESPOSTA</summary>

<br/>

Para começar vamos identificar as entradas e as saídas:

 - **Entrada:**
   - `head` → Referência para o primeiro nó da lista encadeada.
 - **Saída:**
   - `true` → Se existir um ciclo.
   - `false` → se não existir ciclo.

Inicialmente o problema nos deu o seguinte:

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pass
```

 - Vamos começar verificando se `head` é `None` ou se `head.next` é `None`:
   - Ou seja, lista tem 0 ou 1 nó → impossível ter ciclo → retorna False

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:  # O(1)
            return False               # O(1)
```

Continuando, agora nós vamos criar 2 ponteiros `slow` e `fast` que vão ter como referência o `head` da Linked-List:

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:  # O(1)
            return False               # O(1)
        slow = fast = head             # O(1)
```

 - Aqui o ponteiro `fast` vai receber `head` como referência; e o `slow` vai receber o ponteiro `fast` como referência:
   - Ou seja, os dois estão apontando para o mesmo nó/node (head).
 - **NOTE:** Esses ponteiros vão se movimentar de forma diferente (um devagar e outro rápido).

Agora vamos criar um loop que vai:

 - **Caso não exista ciclo**, o ponteiro `fast` chega ao *fim (None)* e o loop acaba.
 - **Caso exista ciclo**, os ponteiros `slow` e `fast` se encontram dentro de no máximo `n` passos:
   - Isso vai ser uma condição que vamos criar dentro do loop.

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:  # O(1)
            return False               # O(1)
        slow = fast = head             # O(1)
        while fast and fast.next:      # O(n)
            slow = slow.next           # O(1)
            fast = fast.next.next      # O(1)
            if slow == fast:           # O(1)
                return True            # O(1)
        return False                   # O(1)
```

Vejam que:

 - `while fast and fast.next:`
   - O loop while vai ser executado enquanto `fast` e `fast.next` não forem `None`.
   - Ou seja, se não tiver um ciclo, `fast.next` vai ser `None` e o loop vai parar retornando `False`.
 - `Dentro do loop while nós estamos incrementando os ponteiros:`
   - *Um devagar (anda um nó/node por vez):* `slow = slow.next`
   - *E o outro rápido (anda dois nós/nodes por vez):* `fast = fast.next.next`
 - `Se os ponteiros se encontrarem, ou seja, temos um loop, vamos retornar True e parar o loop.`
   - `return True`

No fim nosso código vai ficar assim:

[141-linked-list-cycle.py](src/141-linked-list-cycle.py)
```python
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None         


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:  # O(1)
            return False               # O(1)
        slow = fast = head             # O(1)
        while fast and fast.next:      # O(n)
            slow = slow.next           # O(1)
            fast = fast.next.next      # O(1)
            if slow == fast:           # O(1)
                return True            # O(1)
        return False                   # O(1)


if __name__ == '__main__':
    s = Solution()
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = head
    print(s.hasCycle(head))
```

**OUTPUT:**
```bash
True
```

- **Time Complexity:**
  - `Worst Case: O(n)`  
    - O loop percorre a lista inteira até confirmar que não há ciclo, analisando cada nó.  
  - `Best Case: O(1)`  
    - Se a lista for vazia, tiver apenas um nó, ou se o ciclo for detectado logo no início, retorna imediatamente.  
  - `Average Case: O(n)`  
    - Em média, é necessário percorrer uma boa parte da lista para confirmar a presença ou ausência de ciclo.  
- **Space Complexity:**
  - `Worst Case: O(1)`  
    - Só utiliza dois ponteiros (`slow` e `fast`), independentemente do tamanho da lista.  
    - Não há alocação extra proporcional a `n`.  
  - `Best Case: O(1)`  
    - Mesmo nos casos imediatos (lista vazia ou curta), apenas variáveis constantes são usadas.  
  - `Average Case: O(1)`  
    - Em todos os cenários, o espaço extra não cresce com o tamanho da entrada.  



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
