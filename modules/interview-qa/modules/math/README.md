# Mathematical Algorithms

## Contents

 - **Divisibility:**
   - [412. Fizz Buzz](#412-fizz-buzz)
<!---
[WHITESPACE RULES]
- Same topic = "10" Whitespace character.
- Different topic = "200" Whitespace character.
--->









































































































<!--- ( Divisibility ) --->

---

<div id="412-fizz-buzz"></div>

## 412. Fizz Buzz

> Given an integer **n**, return a string array **answer** (1-indexed) where:

 - `answer[i] == "FizzBuzz"` if i is divisible by 3 and 5.
 - `answer[i] == "Fizz"` if i is divisible by 3.
 - `answer[i] == "Buzz"` if i is divisible by 5.
 - `answer[i] == i` (as a string) if none of the above conditions are true.
 - **Constraints:**
   - `1 <= n <= 10^4`

**Example 1:**

```bash
Input: n = 3
Output: ["1","2","Fizz"]
```

**Example 2:**

```bash
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
```

**Example 3:**

```bash
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
```

<details>

<summary>RESPOSTA</summary>

<br/>

Para começar vamos identificar as entradas e as saídas:

 - **Entrada:**
   - um número inteiro `n`.
 - **Saída:**
   - Uma matriz de strings `answer` (1-indexed).
   - `1 <= n <= 10^4` para evitar overflow.

Vamos começar criando uma lista vazia `answer`:

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
```

Continuando, agora nós vamos iterar por todos os valores de 1 a `n`:

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for int i in range(1, n + 1):
```

> **Por que nós estamos percorrendo de `1` até `n + 1`?**

 - `range(inicio, fim)`
   - No Python, a função `range(inicio, fim)` gera números de `inicio` até `fim - 1`.
   - Ou seja, o valor final **(fim) não é incluído**.
 - `for i in range(1, n + 1):`
   - Isso significa que o loop vai percorrer os valores: 1, 2, 3, ..., n
   - **NOTE:** Incluindo o `n` na contagem.
 - **Se fosse apenas range(1, n)?**
   - O último valor seria `n - 1`, e o `n` ficaria de fora.
   - Portanto, usamos `n + 1` para garantir que o número `n` também seja considerado, já que o problema pede para ir de `1` até `n`.

Continuando, dentro do nosso loop primeiro nós vamos verificar se `i` é divisível por 3 e 5 (ao mesmo tempo, `and`):

```python
from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
        return answer
```

 - `if i % 3 == 0 and i % 5 == 0`
   - `if i % 3 == 0` - Para um número ser divisível por 3 o seu resto (mod, %) deve ser 0.
   - `if i % 5 == 0` - Para um número ser divisível por 5 o seu resto (mod, %) deve ser 0.
   - `and` - Para que ambas as condições sejam verdadeiras, eles devem ser verdadeiras ao mesmo tempo.
 - `answer.append("FizzBuzz")`
   - Se essa condição for verdadeira, vamos adicionar **"FizzBuzz"** na lista `answer`.

Continuando, agora vamos verificar se `i` é divisível por 3 (só por 3), se for vamos adicionar **"Fizz"** na lista `answer`:

```python
from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
        return answer
```

Continuando, agora vamos verificar se `i` é divisível por 5 (só por 5), se for vamos adicionar **"Buzz"** na lista `answer`:

```python
from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
        return answer
```

Para finalizar, se `n` não cair em nenhum dos casos vamos retornar uma string com o valor de `i`:

[412-FizzBuzz.py](src/412-FizzBuzz.py)
```python
from typing import List

class Solution:

    def fizzBuzz(self, n: int) -> List[str]:  # O(1)
        answer = []                           # O(1)
        for i in range(1, n + 1):             # O(n) × O(1) = O(n)
            if i % 3 == 0 and i % 5 == 0:     # O(1)
                answer.append("FizzBuzz")     # O(1)
            elif i % 3 == 0:                  # O(1)
                answer.append("Fizz")         # O(1)
            elif i % 5 == 0:                  # O(1)
                answer.append("Buzz")         # O(1)
            else:                             # O(1)
                answer.append(str(i))         # O(1)
        return answer                         # O(1)

if __name__ == '__main__':
    fb = Solution()
    answer = fb.fizzBuzz(15)
    print(answer)
```

**OUTPUT:**
```bash
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
```

 - **Time Complexity:**
   - `Worst Case: O(n)`
     - O loop sempre percorre todos os `n` elementos.
   - `Best Case: O(n)`
     - Mesmo se todos os elementos fossem “FizzBuzz”, ainda precisamos iterar até `n`.
   - `Average Case: O(n)`
     - Independente da mistura entre números e palavras, o loop percorre `n` elementos.
 - **Space Complexity:**
   - `Worst Case: O(n)`
     - No final, a lista *answer* sempre armazena `n` strings.
     - Cada string é de tamanho constante ou pequena em relação a `n`, então consideramos O(1) por item → total O(n).
   - `Best Case: O(n)`
     - Se todos forem "Fizz", "Buzz" ou "FizzBuzz", cada string tem tamanho fixo, mas ainda temos `n` elementos na lista.
   - `Average Case: O(n)`
     - Mesmo que algumas entradas sejam números (com tamanho proporcional a `log n`), em análise de complexidade padrão tratamos strings como O(1), logo o espaço continua proporcional ao número de elementos armazenados: `n`.

</details>

**REFERENCE:**  
[412. Fizz Buzz](https://leetcode.com/problems/fizz-buzz/description/)










































































































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
