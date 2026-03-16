# Two Pointers

## Contents

 - **Fundamentals:**
   - [`O que é, quanto (ou não) utilizar, vantagem e desvantagem da técnica "Two Pointers"?`](#oqvdt)
 - **Two Pointers (same direction):**
   - [`26. Remove Duplicates from Sorted Array`](#26-rdfsa)
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

<summary>ANSWER</summary>

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










































































































<!--- ( Two Pointers (same direction) ) --->

---

<div id="26-rdfsa"></div>

## `26. Remove Duplicates from Sorted Array`

> **NOTE:**  
> Read and understand the problem: [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

<details>

<summary>ANSWER</summary>

<br/>

De início vamos identificar as **entradas** e as **saídas** do nosso problema:

- **Entrada:**
  - `nums` → Lista de inteiros **ordenada não decrescente**.
- **Saída:**
  - Um número inteiro `k` → quantidade de elementos únicos.
  - Os primeiros `k` elementos do array `nums` devem conter os valores únicos, preservando a ordem.

Inicialmente o problema nos deu o seguinte código:

```python
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pass
```

Agora, vamos verificar se a lista `nums` é vazia, se estiver vamos parar a função retornando `0`:

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:                          # O(1)
            return 0                          # O(1)
```

Agora nós vamos criar o primeiro ponteiro, `write` que indica a posição onde o próximo número único será gravado.

> **NOTE:**  
> O primeiro elemento de `nums` sempre é único (visto que a lista está ordenada), então `write` começa em `1`. 

 - **O ponteiro write começa em 1 e não em 0 porque:**
   - O primeiro elemento do array (`nums[0]`) sempre será mantido, já que em um array ordenado o primeiro valor nunca pode ser duplicado em relação a algo anterior.
   - Portanto, não precisamos sobrescrever `nums[0]`. Ele já faz parte da solução.
   - O ponteiro `write` indicar a próxima posição disponível para escrever um valor único.
   - Como o índice 0 já está ocupado corretamente, a próxima posição disponível é o índice 1.

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:                          # O(1)
            return 0                          # O(1)
        write = 1                             # O(1)
```

Agora nós vamos percorrer nossa lista `nums` com um segundo ponteiro, `read` que vai percorrendo a lista a partir do índice 1:

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:                          # O(1)
            return 0                          # O(1)
        write = 1                             # O(1)
        for read in range(1, len(nums)):      # O(n)
            pass
```

> **E agora o que vamos fazer dentro desse loop?**

Primeiro, nós vamos comparar se o elemento atual (`nums[read]`) for diferente do anterior (`nums[read - 1]`), ou seja,  encontramos um número único:

 - Gravamos (salvamos) esse elemento na posição `write`:
   - Lembrando que `write` indica a primeira posição livre na lista `nums` que começou com `1`.
 - Incrementamos `write`.

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:                          # O(1)
            return 0                          # O(1)
        write = 1                             # O(1)
        for read in range(1, len(nums)):      # O(n)
            if nums[read] != nums[read - 1]:  # O(1)
                nums[write] = nums[read]      # O(1)
                write += 1                    # O(1)
```

Por fim, nós vamos retornar `write`, que indica a quantidade de números únicos na lista `nums`:

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:                          # O(1)
            return 0                          # O(1)
        write = 1                             # O(1)
        for read in range(1, len(nums)):      # O(n)
            if nums[read] != nums[read - 1]:  # O(1)
                nums[write] = nums[read]      # O(1)
                write += 1                    # O(1)
        return write                          # O(1)
```

**NOTE:**  
Partindo do presuposto que a lista `nums` não está vazia (nós testamos antes), mesmo que ela tenha apenas um elemento, a função retorna `1`, pois o primeiro elemento de `nums` sempre é único - `write = 1`.

O código completo para testes ficou assim:

[26-remove-duplicates-from-sorted-array.py](src/26-remove-duplicates-from-sorted-array.py)
```python
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:                          # O(1)
            return 0                          # O(1)
        write = 1                             # O(1)
        for read in range(1, len(nums)):      # O(n)
            if nums[read] != nums[read - 1]:  # O(1)
                nums[write] = nums[read]      # O(1)
                write += 1                    # O(1)
        return write                          # O(1)


if __name__ == '__main__':
    s = Solution()
    arr = [0,0,1,1,1,2,2,3,3,4, 9, 15]
    k = s.removeDuplicates(arr)
    print("Number of unique elements:", k)
    print("Modified array:", arr)
```

**OUTPUT:**
```bash
Number of unique elements: 7
Modified array: [0, 1, 2, 3, 4, 9, 15, 3, 3, 4, 9, 15]
```

> **What?**

 - Não deveriamos ter a lista modificada, sem elementos repetidos?
 - Por que nós retornarmos o valor de "k" e não a lista `nums` modificado?

#### in-place

 - **🔹 Em Python (e em quase todas as linguagens), listas são objetos mutáveis.**
   - Quando passamos `nums` para a função, não é feita uma cópia; a função recebe uma referência para o mesmo objeto em memória.
   - Portanto, qualquer modificação feita dentro da função (nums[write] = nums[read]) altera a lista original.
 - **🔹 O motivo de a função retornar apenas write (que é o k, o tamanho da parte útil do array) é que o problema do LeetCode define assim:**
   - Você precisa modificar o array original `in-place`.
   - *E retornar quantos elementos únicos (k) foram armazenados do índice 0 até k-1.*
   - A parte do array além de k pode ser ignorada.

Sendo assim, nós *não precisamos (devemos)* imprimir toda a lista porque o que nos importa é a quantidade `k (write)` retornada pelo a função:

```python
if __name__ == '__main__':
    s = Solution()
    arr = [0,0,1,1,1,2,2,3,3,4,9,15]
    k = s.removeDuplicates(arr)
    print("Number of unique elements:", k)
    print("Unique elements:", arr[:k])
```

**OUTPUT:**
```bash
Number of unique elements: 7
Unique elements: [0, 1, 2, 3, 4, 9, 15]
```

> **E por que se k=7 nós não ultrapassamos de 15 se o primeiro índice é 0?**  
> Não deveria ser [0, 1, 2, 3, 4, 9, 15, 3] do índice 0 ao 7?

 - `O Slicing ([start:end]) em Python funciona assim:`
   - start → índice inicial (*inclusivo*, ou seja, ele aparece na lista).
   - end → índice final (*exclusivo*, ou seja, ele não aparece na lista).
 - `O que significa nums[:k]?`
   - → “Pegue os elementos do índice 0 até k-1”.
   - Ele não inclui o índice k.

Para finalizar nós vamos ter as seguintes complexidades de tempo e espaço:

- **Time Complexity:**
  - Worst Case: `O(n)` → Percorremos todos os elementos uma vez.
  - Best Case: `O(n)` → Mesmo se todos forem iguais, ainda percorremos a lista inteira:
    - **NOTE:** Porém, se só tivermos 1 elemento na lista o *best case* seria `O(1)`.
  - Average Case: `O(n)` → Em média, percorremos a lista inteira.
- **Space Complexity:**
  - Worst Case: `O(1)` → Usamos apenas dois ponteiros (`read` e `write`).
  - Best Case: `O(1)` → Mesma lógica.
  - Average Case: `O(1)` → Sempre constante.

</details>










































































































<!--- ( Fast and Slow Pointers (Floyd's Tortoise and Hare) ) --->

---

<div id="141-llc"></div>

## `141. Linked List Cycle`

> **NOTE:**  
> Read and understand the problem: [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

<details>

<summary>ANSWER</summary>

<br/>

Para começar vamos identificar as **entradas** e as **saídas** do nosso problema:

 - **Entrada:**
   - `head` → Referência para o primeiro nó da lista encadeada.
 - **Saída:**
   - `true` → Se existir um ciclo.
   - `false` → se não existir ciclo.

Inicialmente o problema nos deu o seguinte código:

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
   - O loop while vai ser executado enquanto `fast` e `fast.next` não forem `None` (simultaneamente).
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

Para finalizar nós vamos ter as seguintes complexidades de tempo e espaço:

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

ANSWER

```bash

```

![img](images/)  

</details>
