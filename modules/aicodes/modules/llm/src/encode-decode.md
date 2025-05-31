



























































---

<div id="intro-to-encode"></div>

## encode()

> Um **encode()** é um método (ou função) fornecido por tokenizers de modelos pré-treinados (como os da biblioteca 🤗 transformers) para converter uma string de texto em IDs numéricos de tokens.

O método (ou função) `.encode()` realiza duas etapas principais:

 - **Tokenização:**
   - Divide o texto em unidades menores chamadas tokens (subpalavras, palavras ou pedaços).
 - **Mapeamento para IDs:**
   - Converte cada token em um número inteiro com base no vocabulário do modelo.

![img](images/encode-01.png)  

Vamos ver como implementar isso na prática:

<!--- ( Transformers (Hugging Face) ) --->
<details>

<summary>Transformers (Hugging Face)</summary>

</br>

A biblioteca **🤗 Transformers** já possui `.encode()` pronto. Ela fornece tokenizers otimizados, que:

 - Tokenizam o texto (tokenize);
 - Criam vocabulário (vocab);
 - Fazem mapeamento de tokens para IDs (convert_tokens_to_ids);
 - E até fazem o encode automático com padding, truncamento e máscara de atenção, se necessário.

[transformers_encode_decode.py](src/transformers_encode_decode.py)
```python
from transformers import AutoTokenizer

from utils import read_txt


# load the BERT tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Load the and read the text
file_path = "../datasets/the-verdict.txt"
text = read_txt(file_path)

# encode = Here we tokenize + convert to IDs
encoding = tokenizer.encode_plus(
    text,
    add_special_tokens=True,  # Add [CLS], [SEP]
    return_tensors=None,      # "pt" for Pytorch, "tf" for TensorFlow or None
    truncation=True,          # Truncates if too long
    padding=False             # Do not add padding
)
```

No código acima nós já tokenizamos o texto e convertemos para IDs.

> **Mas qual o tipo eo que tem dentro de "encoding"?**

```python
print("Return type:", type(encoding))
print("\nencoding:\n", encoding)
```

**OUTPUT:**
```bash
Return type: <class 'transformers.tokenization_utils_base.BatchEncoding'>

encoding:
 {'input_ids': [101, 1045, 2018, 2467, 2245, 2990, 21025, 19022, 14287, 2738, 1037, 10036, 11067, 1011, 1011, 2295, 1037, 2204, 3507, 2438, 1011, 1011, 2061, 2009, 2001, 2053, 2307, 4474, 2000, 2033, 2000, 2963
, 2008, 1010, 1999, 1996, 4578, 1997, 2010, 8294, 1010, 2002, 2018, 3333, 2010, 4169, 1010, 2496, 1037, 4138, 7794, 1010, 1998, 2511, 2370, 1999, 1037, 6992, 2006, 1996, 15544, 14356, 2050, 1012, 1006, 2295, 10
45, 2738, 2245, 2009, 2052, 2031, 2042, 4199, 2030, 7701, 1012, 1007, 1000, 1996, 4578, 1997, 2010, 8294, 1000, 1011, 1011, 2008, 2001, 2054, 1996, 2308, 2170, 2009, 1012, 1045, 2064, 2963, 3680, 1012, 12137, 1
6215, 9328, 1011, 1011, 2010, 2197, 3190, 4133, 3334, 1011, 1011, 2139, 24759, 28741, 2290, 2010, 14477, 21408, 16671, 3085, 19935, 21261, 1012, 1000, 1997, 2607, 2009, 1005, 1055, 2183, 2000, 4604, 1996, 3643,
 1997, 2026, 3861, 1005, 2126, 2039, 1025, 2021, 1045, 2123, 1005, 1056, 2228, 1997, 2008, 1010, 2720, 1012, 6174, 3511, 1011, 1011, 1996, 3279, 2000, 12098, 5339, 2003, 2035, 1045, 2228, 1997, 1012, 1000, 1996
, 2773, 1010, 2006, 3680, 1012, 16215, 9328, 1005, 1055, 2970, 1010, 28608, 2049, 1035, 12667, 1035, 2004, 2295, 2027, 2020, 7686, 1999, 2019, 10866, 13005, 1997, 13536, 1012, 1998, 2009, 2001, 2025, 2069, 1996
, 3680, 1012, 16215, 9328, 2015, 2040, 9587, 21737, 2094, 1012, 2018, 2025, 1996, 19401, 2014, 10092, 28983, 1010, 2012, 1996, 2197, 28680, 3916, 2265, 1010, 3030, 2033, 2077, 21025, 19022, 14287, 1005, 1055, 1
000, 4231, 1011, 10487, 1000, 2000, 2360, 1010, 2007, 4000, 1999, 2014, 2159, 1024, 1000, 2057, 4618, 2025, 2298, 2588, 2049, 2066, 2153, 1000, 1029, 2092, 999, 1011, 1011, 2130, 2083, 1996, 26113, 1997, 2014,
10092, 1005, 1055, 4000, 1045, 2371, 2583, 2000, 2227, 1996, 2755, 2007, 1041, 16211, 3490, 16383, 1012, 3532, 2990, 21025, 19022, 14287, 999, 1996, 2308, 2018, 2081, 2032, 1011, 1011, 2009, 2001, 11414, 2008,
2027, 2323, 9587, 14287, 2032, 1012, 2426, 2010, 2219, 3348, 8491, 23161, 2020, 2657, 1010, 1998, 1999, 2010, 2219, 3119, 6684, 1037, 20227, 1012, 2658, 14225, 1029, 3383, 1012, 2065, 2009, 2020, 1010, 1996, 62
25, 1997, 1996, 7477, 2001, 19354, 26022, 2011, 2210, 8149, 17490, 3051, 1010, 2040, 1010, 1999, 2035, 2204, 4752, 1010, 2716, 2041, 1999, 1996, 15552, 1037, 2200, 8502, 1000, 20815, 1000, 2006, 2990, 1011, 101
1, 2028, 1997, 2216, 2265, 2100, 4790, 24802, 2007, 6721, 4087, 6447, 2008, 1045, 2031, 2657, 1006, 1045, 2180, 1005, 1056, 2360, 2011, 3183, 1007, 4102, 2000, 21025, 19022, 14287, 1005, 1055, 4169, 1012, 1998,
 2061, 1011, 1011, 2010, 10663, 2108, 4593, 20868, 2890, 6767, 21170, 1011, 1011, 1996, 6594, 6360, 2351, 2041, 1010, 1998, 1010, 2004, 3680, 1012, 16215, 9328, 2018, 10173, 1010, 1996, 3976, 1997, 1000, 21025,
 19022, 14287, 2015, 1000, 2253, 2039, 1012, 2009, 2001, 2025, 6229, 2093, 2086, 2101, 2008, 1010, 1999, 1996, 2607, 1997, 1037, 2261, 3134, 1005, 8909, 2989, 2006, 1996, 15544, 14356, 2050, 1010, 2009, 3402, 4
158, 2000, 2033, 2000, 4687, 2339, 21025, 19022, 14287, 2018, 2445, 2039, 2010, 4169, 1012, 2006, 9185, 1010, 2009, 2428, 2001, 1037, 23421, 3291, 1012, 2000, 26960, 2010, 2564, 2052, 2031, 2042, 2205, 3733, 10
2], 'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}
```

Vejam que nós temos:

 - Um objeto `transformers.tokenization_utils_base.BatchEncoding`;
 - Em `encoding` temos um dicionário:
   - Com as chaves: `input_ids`, `token_type_ids` e `attention_mask`.
   - E os valores temos *listas* para cada chave.

> **Mas o que são `input_ids`, `token_type_ids` e `attention_mask`?**

 - `input_ids`
   - IDs dos tokens, incluindo tokens especiais ([CLS], [SEP], [PAD]).
 - `token_type_ids`
   - Informa a qual sentença cada token pertence.
 - `attention_mask`
   - 	Informa quais tokens devem ser processados (1) ou ignorados (0).

**OBSERVAÇÃO:**  
Sabendo que nós temos um dicionário com essas chaves (`input_ids`, `token_type_ids` e `attention_mask`), podemos acessar seus valores usando a lógica de dicionários em Python:

```python
token_ids = encoding["input_ids"]
token_type_ids = encoding["token_type_ids"]
attention_mask = encoding["attention_mask"]
```

> **E os vocabulários?**  
> Eles ainda estão disposíveis utilizando `tokenizer.get_vocab()`, lembre-se que **"tokenizer"** é um objeto transformers.

```python
vocabulary = tokenizer.get_vocab()
for vocab in list(vocabulary.items())[:10]:
    print(vocab)
```

**OUTPUT:**
```bash
('titan', 16537)
('##vu', 19722)
('ascended', 19644)
('coats', 15695)
('persist', 29486)
('squeak', 29552)
('₍', 1558)
('##erine', 24226)
('##irus', 26013)
('##valent', 24879)
```

> **OBSERVAÇÃO:**  
> Com isso nós temos o básico de um `encode()`.

</details>




















---



<div id="intro-to-decode"></div>

## decode()

> Um **decode()** é um método (ou função) que transforma uma sequência de IDs de tokens de volta em texto legível (strings).

Por exemplo:

![img](images/decode-01.png)  

Vamos ver como implementar isso na prática:

<!--- ( Transformers (Hugging Face) ) --->
<details>

<summary>Transformers (Hugging Face)</summary>

</br>

Da mesma maneira que a biblioteca tem um mecanismo de `encode()`, ela tem um mecanismo de `decode()`:

[transformers_encode_decode.py](src/transformers_encode_decode.py)
```python
# decode process = here we convert IDs back to text
token_ids = encoding["input_ids"]
decoded_text = tokenizer.decode(token_ids)

print("\nDecoded text (first 353 chars):\n", decoded_text[:353])
```

**OUTPUT:**
```bash
Decoded text (first 353 chars):
 [CLS] i had always thought jack gisburn rather a cheap genius - - though a good fellow enough - - so it was no great surprise to me to hear that, in the height of his glory, he had dropped his painting, marrie
d a rich widow, and established himself in a villa on the riviera. ( though i rather thought it would have been rome or florence. ) " the height
```

</details>
