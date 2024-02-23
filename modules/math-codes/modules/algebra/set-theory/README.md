# Set Theory

## Contents

 - **Fundamentals of Set Theory:**
   - [Set Theory Symbols](#set-theory-symbols)
 - **Types of Set:**




<!--- ( Fundamentals of Set Theory ) --->

---

<div id="set-theory-symbols"></div>

## Set Theory Symbols

**Relational symbols in Set Theory:**

| Symbol            | Name                     | Meaning/Definition       | Example                                                   |
|-------------------|--------------------------|--------------------------|-----------------------------------------------------------|
| **x ∈ A**         | x is an element of set A | Element is member of set | If A={12, 17, 18, 27}, then 27 ∈ A.                       |
| **x ∉ A**         | x is not an element of set A | Element not in set   | If B={c, d, g, h, 32, 54, 59}, then 18 ∉ B.               |
| **A = B**         | Equality Relation | Sets are equivalent           | If P={16, 22, a} and Q={16, 22, a}, then P = Q.           |
| **A ⊆ B**         | Subset           | A is subset of B              | If A={31, b} and B={a, b, 31, 54}, then A ⊆ B.           |
| **A ⊂ B**         | Proper Subset    | A is proper subset of B       | If A={24, c} and B={a, c, 24, 50}, then A ⊂ B.           |
| **A ⊄ B**         | Not a Subset     | A is not subset of B          | If A={67,52} and B={42,34,12}, then A ⊄ B.               |
| **A ⊇ B**         | Superset         | A is superset of B            | If A={14, 18, 26} and B={14, 18, 26}, then A ⊇ B.         |
| **A ⊃ B**         | Proper Superset  | A is proper superset of B     | If A={14, 18, 26, 42} and B={18, 26}, then A ⊃ B.        |
| **A ⊅ B**         | Not a Superset   | A is not superset of B        | If A={11, 12, 16} and B={11, 19}, then A ⊅ B.            |
| **∅ or Φ**        | Empty Set        | Set with no elements          | If {22, y} ∩ {33, a} = Ø.                                |
| **U**             | Universal Set    | Set containing all elements   | If A={a,b,c} and B={1,2,3,b,c}, then U={1,2,3,a,b,c}.    |
| **\|A\|, n(A), n{A}** | Cardinality of a Set | Number of elements in set | If A={17, 31, 45, 59, 62}, then \|A\|=5 (5 elements). |
| **P(X)**          | Power Set        | Set of all subsets of X       | If X={12, 16, 19}, then P(X)={{}, {12}, {16}, {19}, {12, 16}, {16, 19}, {12, 19}, {12, 16, 19}}. |

**Operator-based Symbols in Set Theory:**

| Symbol | Name                        | Meaning/Definition                                     | Example                                                                                                  |
|--------|-----------------------------|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| **A ∪ B** | Union of Sets               | Combines all components from provided sets             | If A={p, q, u, v, w} and B={r, s, x, y}, then A ∪ B = {p, q, u, v, w, r, s, x, y}                        |
| **A ∩ B**  | Intersection of Sets       | Includes common components of both sets               | If A={4, 8, a, b} and B={3, 8, c, b}, then A ∩ B = {8, b}                                                 |
| **X<sup>c</sup> or X<sup>’</sup>** | Complement of a set      | All elements not in the provided set                  | If A is universal set and A={3, 6, 8, 13, 15, 17, 18, 19, 22, 24} and B={13, 15, 17, 18, 19}, then X′ = A - B ⇒ X′ = {3, 6, 8, 22, 24}    |
| **A − B**  | Set Difference             | Contains items from one set not in another            | If A={12, 13, 15, 19} and B={13, 14, 15, 16, 17}, then A − B = {12, 19}                                   |
| **A × B**  | Cartesian Product of Sets  | Product of ordered components of sets                 | If A={4, 5, 6} and B={r}, then A × B = {(4, r), (5, r), (6, r)}                                            |
| **A ∆ B**  | Symmetric Difference       | (A − B) U (B − A) denotes symmetric difference       | If A={13, 19, 25, 28, 37} and B={13, 25, 55, 31}, then A ∆ B = {19, 28, 37, 55, 31}                       |

**Another useful set theory symbols are:**

| Symbol | Name                | Meaning/Definition                                 | Example                |
|--------|---------------------|----------------------------------------------------|------------------------|
| **{}** | Set                 | Brackets containing elements/numbers/alphabets     | {15, 22, c, d}         |
| **\|** | Such that (tal que) | Specifies what is contained within a set           | { q \| q > 6}          |
| **:**  | Such that (tal que) | Alternative symbol for "Such that"                 | {q : q > 6}            |
| **∃ or ∄** | **There exist** or **there doesn’t exist** | If set exists or does not exist | {q ∃ q > 6}    |
































 - **Types of Set:**



<!--- ( types of set ) --->


---

<div id=""></div>

## x

















































































































































<!--- ( Settings ) --->

---

<div id="settings"></div>

## Settings

**CREATE VIRTUAL ENVIRONMENT:**  
```bash
python -m venv math-environment
```

**ACTIVATE THE VIRTUAL ENVIRONMENT (LINUX):**  
```bash
source math-environment/bin/activate
```

**ACTIVATE THE VIRTUAL ENVIRONMENT (WINDOWS):**  
```bash
source math-environment/Scripts/activate
```

**UPDATE PIP:**
```bash
python -m pip install --upgrade pip
```

**INSTALL PYTHON DEPENDENCIES:**  
```bash
pip install -U -v --require-virtualenv -r requirements.txt
```

**Now, Be Happy!!!** 😬





<!--- ( REFERENCES ) --->

---

<div id="ref"></div>

## REFERENCES

 - **General:**
   - [ChatGPT](https://chat.openai.com/chat)
   - [Gemini](https://gemini.google.com/app)
   - [ELEMENTS OF SET THEORY](https://docs.ufpr.br/~hoefel/ensino/CM304_CompleMat_PE3/livros/Enderton_Elements%20of%20set%20theory_%281977%29.pdf)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**

$\mathbf{\exists B \ \forall x \ x \notin B}$  
$\mathbf{\forall A \ \forall B[\forall x(x  \in A \leftrightarrow x \in B) \Rightarrow A = B]}$  
$\mathbf{\forall u \ \forall v \ \exists B \ \forall x(x \in B \leftrightarrow x = u \vee x = v)}$  
