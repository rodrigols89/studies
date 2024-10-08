# Python Internals (Theory and Practice)

## Contents

 - **Requirements:**
   - [**Regular Expressions (Abbreviated as "Regex"):**](#intro-to-regex)
     - [Finding a Word/Text + Understanding slicing (start:end)](#regex-start-end)
     - **Metacharacters:**
       - [`^`](#regex-metacharacters-circumflexaccent)
       - [`$`](#regex-metacharacters-dollarsign)
       - [`\t`](#regex-metacharacters-tab)
       - [`\n`](#regex-metacharacters-newline)
       - [`\r`](#regex-metacharacters-carriagereturn)
       - [`\s and \S`](#regex-metacharacters-checkspaces)
       - [`\d and \D`](#regex-metacharacters-checkdigits)
       - [`\w and \W`](#regex-metacharacters-checkcharacters)
     - **Useful Methods:**
       - **Python:**
         - [`re.search(regex, string) + Match.attributes`](#re-search)
   - [**Extended Backus–Naur Form (EBNF):**](#intro-to-ebnf)
 - **Concepts:**
   - [Intermediate Language (IL) vs. Machine Language (Assembly)](#il-ml)
 - [**Python Precompilation Process:**](#ppp)
     - [**Tokenizer (Tokenizes the program statements)**](#intro-to-tokenizer)
       - [`python -m tokenize <module.py>`](#mtokenize)
     - [**Parser (Analyzes the tokens and makes sense of operations)**](#intro-to-parser)
       - [Lexical Analysis](#intro-to-lexical-analysis)
       - [Understanding the "SyntaxError"](#syntaxerror)
     - [**Abstract Syntax Tree/AST ()**](#intro-to-ast)
       - [`python -m ast <module.py>`](#mast)
 - [**Python Compilation Process:**](#pcp)
   - [Bytecode == Intermediate Language (IL)](#bytecode-equal-il)
   - [`python -m compileall <module.py> (Compiles the code)`](#mcompileall)
   - [`python -m dis <module.py> (Generates IL)`](#mdis)
 - [**Python Virtual Machine:**](#pvm)
 - [**CPython Runtime Project:**](#cpython)
   - [Directory structure (Link)](https://devguide.python.org/getting-started/setup-building/#directory-structure)
   - **/Programs (Source code for the python executable and other binaries):**
     - [`python.c (Python interpreter entry point)`](#programs-python)
   - **/Python (The CPython interpreter source code):**
     - [`pyarena.c (Memory Management)`](#python-pyarena)
 - [**Python Enhancement Proposals (PEPs | Link):**](https://github.com/python/peps)
   - [**PEP 8 – Style Guide for Python Code (Link):**](https://peps.python.org/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds)
     - [Indentation](#pep08-indentation)
     - [Tabs or Spaces?](#pep08-tabs-or-spaces)
     - [Maximum Line Length](#pep08-maximum-line-length)
     - [Should a Line Break Before or After a Binary Operator?](#pep08-line-break-before-or-after-binary-operator)
     - [Blank Lines](#pep08-blank-lines)
     - [Package and Module Names](#pep8-package-and-module-names)
     - [Class Names](#pep8-class-names)
     - [Function and Variable Names](#pep8-function-and-variable-names)
     - [Constants](#pep8-constants)
 - [**The Python Language Reference (Portuguese Brazilian notes):**](#tplr)
 - **Python Developer’s Guide References:**
   - **Contributing - Tips and Tricks:**
     - [Setup and building (Add/Configure upstream | Link)](https://devguide.python.org/getting-started/setup-building/)
     - [Python Development Cycle (Link)](https://devguide.python.org/developer-workflow/development-cycle/)
     - [P.R Lifecycle (Making good PRs/Commits, Reviewing | Link)](https://devguide.python.org/getting-started/pull-request-lifecycle/)
     - [Issue tracker (How to create an "Issue" | Link)](https://devguide.python.org/triage/issue-tracker/)
     - [GitHub labels (CPython Labels | Link)](https://devguide.python.org/triage/labels/)
   - **Issues:**
     - [Easy](https://github.com/python/cpython/issues?q=is%3Aissue+is%3Aopen+label%3Aeasy)
     - [Docs](https://github.com/python/cpython/labels/docs)
   - **Core Developers:**
     - [How to become a core developer (Link)](https://devguide.python.org/core-developers/become-core-developer/)
     - [Experts index (Maintainers | Link)](https://devguide.python.org/core-developers/experts/)
     - [CODEOWNERS (P.R Reviewers | Link)](https://github.com/python/cpython/blob/main/.github/CODEOWNERS)
 - **Settings:**
   - [Creating venv environment](#venv-environment)
   - [Install Python From Source](#python-from-source)
   - [Contribute Process](#contribute-process)
 - **Useful Links:**
   - [**Status of Python versions (Releases, Supported/Unsupported versions, Status key | Link)**](https://devguide.python.org/versions/)
   - **Documentation:**
     - [Python Brazilian Portuguese Documentation (Link)](https://docs.python.org/pt-br)
     - [Python Official Documentation (Link)](https://docs.python.org)
     - [Building the documentation (Link)](https://devguide.python.org/documentation/start-documenting/#building-the-)
     - [reStructuredText markup (Link)](https://devguide.python.org/documentation/markup/)
 - [**REFERENCES**](#ref)
<!--- 
[WHITESPACE RULES]
- Same topic = "10" Whitespace character.
- Different topic = "50" Whitespace character.
--->




















































<!--- ( Requirements/Regular Expressions ) --->

---

<div id="intro-to-regex"></div>

## Regular Expressions (Abbreviated as "Regex")

 - Regular Expressions was initially a term borrowed from **"Automata Theory"** in theoretical computer science. Broadly, it refers to patterns to which a substring needs to be matched.
 - Many *"programming languages"*, *"text processing tools"*, *"data validation tools"* and *"search engines"* make extensive use of them.

The key idea is that a regular expression is a pattern which matches a set of target strings. For example:

```bash
\w+@\w+\.(com|org|net|in)
```

The Regex above matches a most email addresses that end with a `.com`, `.net`, `.org` or a `.in`.

---

<div id="regex-start-end"></div>

## Finding a Word/Text + Understanding slicing (start:end)

> We can use the **Regex** to find a word/text in a string.

For example, let's use the **re.search()** function to find the first ocorrence of the word **"dri"** in the string **"Rodrigo Leite da Silva"**:

```python
import re

regex = r"dri"
string = "Rodrigo Leite da Silva"

match = re.search(regex, string)

if match:
    print("Match found:", match.group())
    print("Start:", match.start())
    print("End:", match.end())
    print("Span:", match.span())
else:
    print("No match found!")
```

**OUTPUT:**
```bash
Match found: dri
Start: 2
End: 5
Span: (2, 5)
```

Now, let's see an abstraction to the string **"Rodrigo Leite da Silva"** on the memory:

```bash
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
| R | o | d | r | i | g | o |   | L | e | i | t | e |   | d | a |   | S | i | l | v | a |
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
  0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21
          |           |
          |           |
        +---+---+---+---+
        | d | r | i | g |
        +---+---+---+---+ 
```

> **What?**
> Why the return was **"dri"** and not **"drig"** as shown in the memory abstraction above?

**NOTE:**  
This is because we must treat the **"start()"** and **"end()"** of the Match object as columns. For example, see the other abstraction below of text in columns rather (em vez de) than in memory:

```bash
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
| R | o | d | r | i | g | o |   | L | e | i | t | e |   | d | a |   | S | i | l | v | a |
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22
        |           |
        |           |
        +---+---+---+
        | d | r | i |
        +---+---+---+
```

Great, now we understand how to:

 - `re.search(regex, string)`
   - How to use the **re.search()** method to find the first occurrence of a word/text in a string.
 - `match.start() and match.end()`
   - How the **"start()"** and **"end()"** methods work:
     - By columns, not indices.

> **But what are the coordinate points of the *start() *and *end()* methods for since they cannot be treated as indexes in memory?**

### Slicing

> We can use these coordinate points to slice the string.

For example:

```python
import re

regex = r"dri"
string = "Rodrigo Leite da Silva"

match = re.search(regex, string)
start = match.start()
end = match.end()
print("Sliced ​​string:", string[start:end])
```

**OUTPUT:**
```bash
Sliced ​​string: dri
```

This is equivalent to:

```python
import re

regex = r"dri"
string = "Rodrigo Leite da Silva"
print(string[2:5])
```

**OUTPUT:**
```bash
dri
```

---

<div id="regex-metacharacters-circumflexaccent"></div>

## `^`

| Metacharacter | Meaning                                         |
|---------------|-------------------------------------------------|
| `^`           | Used to test (match) if the beginning of the string starts with the selected string/word. |

**EXAMPLE:**
```python
import re

regex = r"^Hello"
string = "Hello, world!"

match = re.search(regex, string)

if match:
    print("Match found:", match.group())
    print("Start:", match.start())
    print("End:", match.end())
    print("Span:", match.span())
else:
    print("No match found!")
```

**OUTPUT:**
```bash
Match found: Hello
Start: 0
End: 5
Span: (0, 5)
```

See that:

 - We use the **Metacharacter** `^` to test (match) if the beginning of the string starts with the selected string/word.
 - **NOTE:** The *Regex* is **"case-sensitive"**.

---

<div id="regex-metacharacters-dollarsign"></div>

## `$`

| Metacharacter | Meaning                                         |
|---------------|-------------------------------------------------|
| `$`           | Used to test (match) if the end of the string ends with the selected string/word. |

**EXAMPLE:**
```python
import re

regex = r"!$"
string = "Hello, world!"

match = re.search(regex, string)

if match:
    print("Match found:", match.group())
    print("Start:", match.start())
    print("End:", match.end())
    print("Span:", match.span())
else:
    print("No match found!")
```

**OUTPUT:**
```bash
Match found: !
Start: 12
End: 13
Span: (12, 13)
```

See that:

 - The **Metacharacter** `$` is used at the end of the selected string/word to test (match).

---

<div id="regex-metacharacters-tab"></div>

## `\t`

**EXAMPLE:**
| Metacharacter | Meaning                                                     |
|---------------|-------------------------------------------------------------|
| `\t`          |	Used to test (match) if the selected string/word has a tab. |

```python
import re

regex = r"\t"
string = "1... \t2... \t3..."

match = re.search(regex, string)

if match:
    print("Match found:", match.group())
    print("Start:", match.start())
    print("End:", match.end())
    print("Span:", match.span())
else:
    print("No match found!")
```

**OUTPUT:**
```bash
Match found: 
Start: 5
End: 6
Span: (5, 6)
```

See that:

 - **First:**
   - The **match.group()** function doesn't display anything because the `\t` character is a tab character (a special whitespace character) that is not visible as text when printed.
 - **Continuing...**
   - Regardless of the location of the tab in the text, Regex will tell you whether (tem/exist) or not there is a tab.
   - **NOTE:** Another observation is that this approach only catches the first occurrence of the Regular Expression.

---

<div id="regex-metacharacters-newline"></div>

## `\n`

| Metacharacter | Meaning                                                         |
|---------------|-----------------------------------------------------------------|
| `\n`          |	Used to test (match) if the selected string/word has a newline. |

**EXAMPLE:**
```python
import re

regex = r"\n"
string = "1... \n2... \n3..."

match = re.search(regex, string)

if match:
    print("Match found:", match.group())
    print("Start:", match.start())
    print("End:", match.end())
    print("Span:", match.span())
else:
    print("No match found!")
```

**OUTPUT:**
```bash
Match found: 

Start: 5
End: 6
Span: (5, 6)
```

 - `Match found:`
   - The match.group() returns the found character, which is `\n`.
   - However, `\n` is a control character that does not appear visually in the output as text; it simply causes the cursor to move to the next line:
     - **NOTE:** So it appears that nothing is displayed after "Match found:", but it is actually the newline character.

---

<div id="regex-metacharacters-carriagereturn"></div>

## `\r`

**NOTE:**  
Before we see how `Carriage Return \r` works in *Regex*, let's understand what it is.

 - **1st:**
   - The `Carriage Return \r` moves the cursor to the beginning of the line.
 - **2nd:**
   - Now, the subsequent characters **"overwrite"** the first characters of the original string. 

For example:

```bash
# Original String.
"Hello, World\r..."

# Move the cursor to the beginning of the line.
"Hello, World ..."
             ^
             | Cursor here...

# The subsequent characters "overwrite" the first characters of the original string.
"Hello, World ..."
"...lo, World ..." # The subsequent characters were "overwritten".
```

| Metacharacter | Meaning                                                                 |
|---------------|-------------------------------------------------------------------------|
| `\r`          |	Used to test (match) if the selected string/word has a carriage return. |

**EXAMPLE:**
```python
import re

regex = r"\r"
string = "Hello... World\r..."

match = re.search(regex, string)

if match:
    print("Match found:", match.group())
    print("Start:", match.start())
    print("End:", match.end())
    print("Span:", match.span())
else:
    print("No match found!")
```

**OUTPUT:**
```bash
Match found: 
Start: 14
End: 15
Span: (14, 15)
```

See that:

 - Again, the `Carriage Return \r` is a special character that is not visible as text.

---

<div id="regex-metacharacters-checkspaces"></div>

## `\s and \S`

| Metacharacter | Meaning                                                     |
|---------------|-------------------------------------------------------------|
| `\s`          | Used to test (match) if the selected string/word has space. |
| `\S`          | Used to test (match) the first **"character (any character) that is not whitespace"**. This includes letters, numbers, symbols, etc. |

**EXAMPLE "\s":**
```python
import re

regex = r"\s"
string = "Hello, World..."

match = re.search(regex, string)

if match:
    print("Match found:", match.group())
    print("Start:", match.start())
    print("End:", match.end())
    print("Span:", match.span())
else:
    print("No match found!")
```

**OUTPUT:**
```bash
Match found:  
Start: 6
End: 7
Span: (6, 7)
```

**EXAMPLE "\S":** 
```python
import re

regex = r"\S"
string = "     Hello, World..."

match = re.search(regex, string)

if match:
    print("Match found:", match.group())
    print("Start:", match.start())
    print("End:", match.end())
    print("Span:", match.span())
else:
    print("No match found!")
```

**OUTPUT:**
```bash
Match found: H
Start: 5
End: 6
Span: (5, 6)
```

See that here:

 - `Match found: H`
   - The first match found is **"H"**, which is **the first character in the string that is not a whitespace character**.
   - **NOTE:** Note that before the **"H"** there were 5 whitespace characters, but the `\S` only considers the first occurrence of a character that **IS NOT A WHITESPACE**.

---

<div id="regex-metacharacters-checkdigits"></div>

## `\d and \D`

| Metacharacter | Meaning                                                                       |
|---------------|-------------------------------------------------------------------------------|
| `\d`          |	Used to test (match) *the first digit occurrence on a selected string*.         |
| `\D`          |	Used to test (match) *the first **non-digit** occurrence on a selected string*. |

**EXAMPLE "\d":**
```python
import re

regex = r"\d"
string = "Nine - 9"

match = re.search(regex, string)

if match:
    print("Match found:", match.group())
    print("Start:", match.start())
    print("End:", match.end())
    print("Span:", match.span())
else:
    print("No match found!")
```

**OUTPUT:**
```bash
Match found: 9
Start: 7
End: 8
Span: (7, 8)
```

**EXAMPLE "\D":**
```python
import re

regex = r"\D"
string = "Nine - 9"

match = re.search(regex, string)

if match:
    print("Match found:", match.group())
    print("Start:", match.start())
    print("End:", match.end())
    print("Span:", match.span())
else:
    print("No match found!")
```

**OUTPUT:**
```bash
Match found: N
Start: 0
End: 1
Span: (0, 1)
```

---

<div id="regex-metacharacters-checkcharacters"></div>

## `\w and \W`

| Metacharacter | Meaning                                                                                  |
|---------------|------------------------------------------------------------------------------------------|
| `\w`          |	Used to test (match) *the first word character occurrence on selected string*.           |
| `\W`          |	Used to test (match) *the first **non-word character** occurrence on a selected string*. |

**EXAMPLE "\w":**
```python
import re

regex = r"\w"
string = "Nine - 9"

match = re.search(regex, string)

if match:
    print("Match found:", match.group())
    print("Start:", match.start())
    print("End:", match.end())
    print("Span:", match.span())
else:
    print("No match found!")
```

**OUTPUT:**
```bash
Match found: N
Start: 0
End: 1
Span: (0, 1)
```

**EXAMPLE "\W":**
```python
import re

regex = r"\W"
string = "Nine - 9"

match = re.search(regex, string)

if match:
    print("Match found:", match.group())
    print("Start:", match.start())
    print("End:", match.end())
    print("Span:", match.span())
else:
    print("No match found!")
```

**OUTPUT:**
```bash
Match found:  
Start: 4
End: 5
Span: (4, 5)
```

> **NOTE:**  
> In the above example with `\W` the first occurrence that was not a *Word Character* was a *"whitespace"*.

---

<div id="re-search"></div>

## `re.search(regex, string) + Match.attributes`

 - The **re.search()** function of the **"re"** module in Python is used to *search for a match of a pattern (regular expression) in a string*.
 - **Return:**
   - If a match is found, **re.search()** returns a match object, which contains information about the match (such as the position and the matched text).
   - If no match is found, it returns `None`.

For example:

```python
import re

regex = r"^Hello"
string = "Hello, world!"

match = re.search(regex, string)
print(match)
```

**OUTPUT:**
```bash
<match object; span=(0, 5), match='Hello'>
```

Where:

 - `<re.Match object>`
   - Indicates that the returned object is a *Match object*.
 - `span=(0, 5)`
   - Shows the range (start and end position) of the match in the original string.
   - In this case, the match starts at index 0 and ends at index 5 (non-inclusive), indicating that the word *"Hello"* was found from the beginning of the string.
 - `match='Hello'`
   - Displays the text of the *match found* was *"Hello"*.

### Match.attributes

Also access *attributes* of a *Match object* returned by the **re.search()** function:

 - **match.group():**
   - Returns the string matching the found pattern.
 - **match.start():**
   - Returns the starting index of the match.
 - **match.end():**
   - Returns the ending index of the match.
 - **match.span():**
   - Returns a tuple containing the starting and ending indices of the match.

Let's look at another example:

```python
import re

regex = r"^Hello"
string = "Hello, world!"

match = re.search(regex, string)

if match:
    print("Match found:", match.group())
    print("Start:", match.start())
    print("End:", match.end())
    print("Span:", match.span())
else:
    print("No match found")
```

**OUTPUT:**
```bash
Match found: Hello
Start: 0
End: 5
Span: (0, 5)
```




















































<!--- ( Requirements/Extended Backus–Naur Form ) --->

---

<div id="intro-to-ebnf"></div>

## Extended Backus–Naur Form (EBNF)




















































<!--- ( Concepts ) --->

---

<div id="il-ml"></div>

## Intermediate Language (IL) vs. Machine Language (Assembly)

To understand how Python is interpreted, first, let's see how a compilation works for a compiled language:

![img](images/il-vs-ml-01.png)  

See our **file.xx** passes by a *compiler* → next is generated a Machine Language (Assembly). However, the compiler has **Front-end** and **Backend** steps:

 - **Front-end:**
   - Receive the compiled language code: C/C++, Go, Rust.
   - Translates to an *Intermediate Language (IL)* → The compiler knows to work with this language (IL).
 - **Backend:**
   - The compiler backend translates the *Intermediate Language (IL)* to *Machine Language (Assembly)*:
     - The *Machine Language (Assembly)* is a language used/read by the *CPU*.
     - This *Machine Language (Assembly)* is:
       - *x83:* 32 architecture.
       - *x64:* 64 architecture.
       - *ARM:* Cellphone architecture.

> **NOTE:**  
> This is the traditional compilation, but how Python compiler works?

To understand how Python is interpreted, let's see another abstraction below:

![img](images/il-vs-ml-02.png)  

 - Looking at the image above we can see that the Python compilation has no **"backend step"**.
 - That's, the Python compilation doesn't generate a **Machine Language (Assembly)** for a specific CPU architecture.

> **Ok, but if the Python compiler doesn't compiler for a specific architecture where does he send the Intermediate Language (IL)?**

To understand this, let's see another abstraction:

![img](images/il-vs-ml-03.png)  

Looking at the image above we can see that:

 - **1st -** The compiler translates our code to an *Intermediate Language (IL)*.
 - **2nd -** This *Intermediate Language (IL)* is sended to a **Virtual Machine**.
 - **3rd -** The **Virtual Machine** communicates with the **computer (CPU)** and repeats this process until it finishes the tasks.

> **NOTE:**  
> See that here the Python compiler doesn't have a backend step to generate a *Machine Language*. **The *Virtual Machine* that communicates with the *computer (CPU)***.

Knowing this, we can say that:

 - Traditional compilers compile the code for **Real Machines (or CPU architecture)**.
 - The Python compiler compiles the code for a **Virtual Machine**.

























































<!--- ( PPP = Python Pre-Compilation Process ) --->

---

<div id="ppp"></div>

## Python Precompilation Process

The **Python Precompilation Process** has three steps before sending an *Intermediate Language (IL)* to the **Virtual Machine**:

 - Tokenizer.
 - Parser.
 - Abstract Syntax Tree (AST).

![img](images/ppp-01.png)  










<!--- ( PPP/Tokenizer ) --->

---

<div id="intro-to-tokenizer"></div>

## Tokenizer (Tokenizes the program statements)

> The first step before sending an *Intermediate Language (IL)* to the *Virtual Machine* is the ***"Tokenizer"***.

For example, see the **tokenizations** below:

![img](images/tokenizer-01.jpeg)  

See that:

 - **We have a Input (text):**
 - **Next, we tokenize the Input (text) by sentences:**
   - The *dot symbol "."* sometimes says that the sentence is ended.
 - **Finally, we to tokenize the sentences.**

> **OK, but why tokenize?**

 - **Do you remember in the high school the "Morphological Analysis"?**
   - That's, we get each word in the sentence and find your grammatical class.
 - **The Lexical Analysis (applied on the Parse stage) do the same thing:**
   - Take each tokenized word (or statement) and place it in the appropriate context.

> **NOTE:**  
> However, here the focus is not "Morphological Analysis" or "Words", but **Python statements**, **inputs**, **expressions**, etc.

For example:

![img](images/tokenizer-03.png)  

> If you pay attention you can see that the **"+"** is an operator. But, which operator?

Like **"Morphological Analysis"** here we also have **"subclass"**:

![img](images/tokenizer-04-v2.png)  

> **Okay, but how do I know what tokens Python has?**

**NOTE:**  
We can check the Python Tokens on the [CPython Repository](https://github.com/python/cpython) by clicking on the [Grammar/Tokens](https://github.com/python/cpython/blob/main/Grammar/Tokens).

**Current Python Tokens (02/07/2024):**
```py
ENDMARKER
NAME
NUMBER
STRING
NEWLINE
INDENT
DEDENT

LPAR                    '('
RPAR                    ')'
LSQB                    '['
RSQB                    ']'
COLON                   ':'
COMMA                   ','
SEMI                    ';'
PLUS                    '+'
MINUS                   '-'
STAR                    '*'
SLASH                   '/'
VBAR                    '|'
AMPER                   '&'
LESS                    '<'
GREATER                 '>'
EQUAL                   '='
DOT                     '.'
PERCENT                 '%'
LBRACE                  '{'
RBRACE                  '}'
EQEQUAL                 '=='
NOTEQUAL                '!='
LESSEQUAL               '<='
GREATEREQUAL            '>='
TILDE                   '~'
CIRCUMFLEX              '^'
LEFTSHIFT               '<<'
RIGHTSHIFT              '>>'
DOUBLESTAR              '**'
PLUSEQUAL               '+='
MINEQUAL                '-='
STAREQUAL               '*='
SLASHEQUAL              '/='
PERCENTEQUAL            '%='
AMPEREQUAL              '&='
VBAREQUAL               '|='
CIRCUMFLEXEQUAL         '^='
LEFTSHIFTEQUAL          '<<='
RIGHTSHIFTEQUAL         '>>='
DOUBLESTAREQUAL         '**='
DOUBLESLASH             '//'
DOUBLESLASHEQUAL        '//='
AT                      '@'
ATEQUAL                 '@='
RARROW                  '->'
ELLIPSIS                '...'
COLONEQUAL              ':='
EXCLAMATION             '!'

OP
AWAIT
ASYNC
TYPE_IGNORE
TYPE_COMMENT
SOFT_KEYWORD
FSTRING_START
FSTRING_MIDDLE
FSTRING_END
COMMENT
NL
ERRORTOKEN

# These aren't used by the C tokenizer but are needed for tokenize.py
ENCODING
```

---

<div id="mtokenize"></div>

## `python -m tokenize <module>`

To see the tokens of a program, we need to run the following command:

```bash
python -m tokenize <module.py>
```

For example, imagine we have the following program:

[tokenize-ex01.py](src/tokenize-ex01.py)
```python
1 + 2
```

**INTPUT:**
```bash
python -m tokenize tokenize-ex01.py
```

**OUTPUT:**
```bash
0,0-0,0:            ENCODING       'utf-8'        
1,0-1,1:            NUMBER         '1'            
1,2-1,3:            OP             '+'            
1,4-1,5:            NUMBER         '2'            
1,5-1,6:            NEWLINE        '\n'           
2,0-2,0:            ENDMARKER      ''
```

Analyzing the output above we have **three columns**:

 - **First column:**
   - **Token (Statement) mapping:** This mapping is separated into *two parts*.
     - "initial_row", "initial_col" - "final_row", "final_col"
     - For example, "1,2-1,3":
       - "initial_row" = 1
       - "initial_col" = 2
       - "final_row" = 1
       - "final_col" = 3
     - **NOTE:** The tokenize process ignores *"spaces"* and *"tabs"*. That is, **"1 + 2"** is equal to **"1+2"**.
 - **Second column:**
   - Token name in the grammar.
 - **Third column:**
   - Token value.

> **NOTE:**  
> We can also specific to the *"tokenize"* show *subclass* of tokens using **"-e"** flag:

**INTPUT:**
```bash
python -m tokenize -e tokenize-ex01.py
```

**OUTPUT:**
```bash
0,0-0,0:            ENCODING       'utf-8'        
1,0-1,1:            NUMBER         '1'            
1,2-1,3:            PLUS           '+'            
1,4-1,5:            NUMBER         '2'            
1,5-1,6:            NEWLINE        '\n'           
2,0-2,0:            ENDMARKER      ''
```

> **NOTE:**  
> See that now the **"+"** operator shows its subclass **"PLUS"** and not just **"OP"**.










<!--- ( PPP/Parser ) --->

---

<div id="intro-to-parser"></div>

## Parser (Analyzes the tokens and makes sense of operations)

> The **"Parser"** stage is where Python will **analyze the tokens** and **make sense of operations (dar sentido as operações)**.

 - To make sense of the operations, we first need to program the **grammatical rules** of the language.
 - To program the **grammatical rules** is common used the [Extended Backus-Naur Form (EBNF)](https://plantuml.com/ebnf#:~:text=Extended%20Backus%E2%80%93Naur%20Form%20(EBNF)%20is%20a%20type%20of,of%20the%20Algol%20programming%20language.) notation, also know as the [Context-Free Grammars](https://brilliant.org/wiki/context-free-grammars/):
   - [Extended Backus–Naur Form (EBNF)](https://plantuml.com/ebnf#:~:text=Extended%20Backus%E2%80%93Naur%20Form%20(EBNF)%20is%20a%20type%20of,of%20the%20Algol%20programming%20language.) is a type of formal syntax used to specify the structure of a programming language or other formal language. 

**NOTE:**  
We can check the Python grammar implementations on the [CPython Repository](https://github.com/python/cpython) by clicking on the [Grammar/python.gram](https://github.com/python/cpython/blob/main/Grammar/python.gram).

---

<div id="intro-to-lexical-analysis"></div>

## Lexical Analysis

The process of **analyzing the tokens** and **making sense of operations** is called **"Lexical Analysis"**:

![img](images/lexical-analysis-01.png)  

See that:

 - **First, we take the tokens:**
   - Generated by the **"Tokenizer"** stage.
 - **Next, the *Parser* stage will check the language Grammar:**
   - This step is known as the **"Lexical Analysis"**.
 - **Finally, the *Parser* generates the *"Abstract Syntax Tree (AST)"*.**

---

<div id="syntaxerror"></div>

## Understanding the "SyntaxError"

To understand the **"SyntaxError"** imagine we have the following program:

[syntax_error.py](src/syntax_error.py)
```python
1000 +* 2
```

Now, let's tokenize this program:

**INPUT:**
```bash
python -m tokenize -e syntax_error.py
```

**OUTPUT:**
```bash
0,0-0,0:            ENCODING       'utf-8'        
1,0-1,4:            NUMBER         '1000'         
1,5-1,6:            PLUS           '+'            
1,6-1,7:            STAR           '*'            
1,8-1,9:            NUMBER         '2'            
1,9-1,10:           NEWLINE        '\n'           
2,0-2,0:            ENDMARKER      ''
```

**NOTE:**  
See that the `*` and `+` are considered operators (*"PLUS"* and *"STAR"* respectively).

> **Now... What happens if we try to run this program?**

**INPUT:**
```bash
python -m syntax_error.py
```

**OUTPUT:**
```bash
  File "syntax_error.py", line 1
    1000 +* 2
          ^
SyntaxError: invalid syntax
```

**Why SyntaxError?**  
Do you remember **"Lexical Analysis"** in the *Parser* stage?

![img](images/lexical-analysis-01.png)  

Yes, the **Lexical Analysis (Parser)** checks the rule `+*` on the [Grammar/python.gram](https://github.com/python/cpython/blob/main/Grammar/python.gram) and sees that **the rule doesn't exist**.

> **NOTE:**  
> Whenever (sempre) a rule is not in the grammar it will generate a **"SyntaxError"**.










<!--- ( PPP/Abstract Syntax Tree/AST ) --->

---

<div id="intro-to-ast"></div>

## Abstract Syntax Tree/AST ()



---

<div id="mast"></div>

## `python -m ast <module.py>`

To check the **"Abstract Syntax Tree (AST)"** of our program we need to run the following command:

**INPUT:**
```bash
python -m ast tokenize-ex01.py
```

**OUTPUT:**
```bash
Module(
   body=[
      Expr(
         value=BinOp(
            left=Constant(value=1),
            op=Add(),
            right=Constant(value=2)))],
   type_ignores=[])
```

> **NOTE:**  
> See that the output is a Data Structure. That is, we can access it.

The **Abstract Syntax Tree (AST)** of the example above will look like this:

![img](images/m-ast-01.png)  





















































<!--- ( PCP = Python Compilation Process ) --->

---

<div id="pcp"></div>

## Python Compilation Process

After Python goes through the *Precompilation stages (Tokenizer, Parser, AST)* we start the **Compilation** process:

![img](images/pcp-01.png)

Python compilation looks something like this:

![img](images/pcp-02.png)  

See that:

 - First, we take the *Abstract Syntax Tree (AST)* stage result.
 - Next, the compiler run **Operation codes (written in .c)** on the *Abstract Syntax Tree (AST)*.
 - Finally is generates **"Bytecode"**:
   - The generated *Bytecode* are files with the `.pyc` extension.

**NOTE:**  
We can see the **Operation codes (written in .c)** on the [CPython Repository](https://github.com/python/cpython) by clicking on the [Python/compile.c](https://github.com/python/cpython/blob/main/Python/compile.c).

---

<div id="bytecode-equal-il"></div>

## Bytecode == Intermediate Language (IL)

I don't know if you remember, but **Bytecode** and **Intermediate Language (IL)** are the same thing:

![img](images/il-vs-ml-03.png)  

---

<div id="mcompileall"></div>

## `python -m compileall <module.py> (Compiles the code)`

To compiler a Python module manually we can run the following command:

**INPUT:**
```bash
python -m compileall tokenize-ex01.py
```

Going back to our examples, the compiled code will be something like this:

![img](images/m-compileall-01.png)  

> **NOTE:**  
> These files are generally saved in `__pycache__` folder.

---

<div id="mdis"></div>

## `python -m dis <module.py> (Generates IL)`

After the *Compilation process*, we have a crazy code to be interpreted:

![img](images/m-compileall-01.png)  

**The *Virtual Machine* can't interpret this code!**  
To solve that we first need to *"disassemble"* it (the Virtual Machine does it automatically).

For example:

[disassemble.py](src/disassemble.py)
```python
a = 10000
b = 2
a + b
```

**INPUT:**
```bash
python -m dis disassemble.py
```

> **NOTE:**  
> **"dis"** is the abbreviation of **"disassemble"**.

**OUTPUT:**
```bash
  0           0 RESUME                   0

  1           2 LOAD_CONST               0 (10000)
              4 STORE_NAME               0 (a)

  2           6 LOAD_CONST               1 (2)
              8 STORE_NAME               1 (b)

  3          10 LOAD_NAME                0 (a)
             12 LOAD_NAME                1 (b)
             14 BINARY_OP                0 (+)
             18 POP_TOP
             20 RETURN_CONST             2 (None)
```

**NOTE:**  
This is what the **Virtual Machine** *"understands"* and will *"interpret"*.





















































<!--- ( CPython Runtime Project ) --->

---

<div id="cpython"></div>

## CPython

> [CPython](https://github.com/python/cpython) is one of the many **Python runtimes**, maintained and written by different teams of developers.

 - [CPython](https://github.com/python/cpython) is the “official” or reference implementation of Python:
   - Some other runtimes you may have heard are [PyPy](https://github.com/pypy/pypy), [Cython](https://github.com/cython/cython), and [Jython](https://github.com/jython/jython).










<!--- ( CPython/Programs ) --->

---

<div id="programs-python"></div>

## `python.c (Python interpreter entry point)`

 - When you type **"python"** into the terminal, you run the Python binary, compiled from source files like [CPython/Programs/python.c](https://github.com/python/cpython/blob/main/Programs/python.c).
 - **NOTE:** So, although you are not directly calling [CPython/Programs/python.c](https://github.com/python/cpython/blob/main/Programs/python.c), you are using the result of compiling that file.










<!--- ( CPython/Python ) --->

---

<div id="python-pyarena"></div>

## `pyarena.c (Memory Management)`

> The **"PyArena"** is one of CPython’s Memory Management Structures.

 - The code is within [Python/pyarena.c](https://github.com/python/cpython/blob/main/Python/pyarena.c) and contains a *wrapper* around C’s *Memory Allocation* and *Deallocation* functions:
   - In a traditionally written C program, the developer should allocate memory for data structures before writing into that data.

Python takes that responsibility away from the programmer and uses two algorithms:

 - A Reference Counter.
 - A Garbage Collector.





















































<!--- ( PEP 8 – Style Guide for Python Code ) --->

---

<div id="pep08-indentation"></div>

## Indentation

Use **"4 spaces"** per *indentation* level:

```python
# Correct:

# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```

```python
# Wrong:

# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
```

---

<div id="pep08-tabs-or-spaces"></div>

## Tabs or Spaces?

> **Spaces are the preferred indentation method.**

---

<div id="pep08-maximum-line-length"></div>

### Maximum Line Length

 - Limit all lines to a maximum of 79 characters.
 - **NOTE:** When you write *explanatory* **"docstrings"** and **"comments"**, **"limiting lines to 72 characters"**:
   - This ensures that notes are easily visible and readable (legíveis).

**NOTE:**  
The preferred way of wrapping long lines is by using Python’s implied line continuation inside *parentheses*, *brackets* and *braces*.

For example:

**Function Calls with Many Arguments:**
```python
# Instead of using backslashes:
result = my_function(first_argument, second_argument, third_argument, 
                     fourth_argument, fifth_argument)

# Use parentheses:
result = my_function(
    first_argument,
    second_argument,
    third_argument,
    fourth_argument,
    fifth_argument
)
```

**Long Lists, Dictionaries, and Sets:**
```python
# Long list using backslashes:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, \
           13, 14, 15, 16, 17, 18, 19, 20]

# Long list using brackets:
my_list = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20
]
```

**Long Logical Expressions:**
```python
# Using backslashes:
if (condition1 and condition2 and condition3 and condition4 and \
    condition5 and condition6):
    perform_action()

# Using parentheses:
if (condition1 and condition2 and condition3 and condition4 and
    condition5 and condition6):
    perform_action()
```

---

<div id="pep08-line-break-before-or-after-binary-operator"></div>

## Should a Line Break Before or After a Binary Operator?

```python
# Wrong:
# operators sit far away from their operands
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
```

```python
# Correct:
# easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

---

<div id="pep08-blank-lines"></div>

## Blank Lines

**Top-Level function and class definitions:**  
Surrounding top-level function and class definitions with two blank lines helps visually separate different parts of the code, making it easier to navigate.

```python
# Top-level function definition
def my_function1():
    pass


# Another top-level function definition
def my_function2():
    pass


# Top-level class definition
class MyClass:
    pass
```

**Methods inside a class:**  
Surrounding method definitions inside a class with a single blank line helps visually separate the methods, improving readability.

```python
class MyClass:
    def method1(self):
        pass

    def method2(self):
        pass
```

**Blank lines to separate related functions:**  
Using blank lines to separate groups of related functions can improve code organization. However, this should be done sparingly.

```python
def related_function1():
    pass

def related_function2():
    pass


def another_function():
    pass
```

**Blank lines in functions to indicate logical sections:**  
Within functions, using blank lines to indicate logical sections can help make the code more comprehensible.

```python
def calculate_total(prices):
    total = 0.0

    # Calculate the total of the prices.
    for price in prices:
        total += price

    # Return the calculated total.
    return total
```

---

<div id="pep8-package-and-module-names"></div>

## Package and Module Names

**Naming modules with Short, all-lowercase names:**  
Choosing short, all-lowercase names for modules makes importing and using them easier, avoiding confusion and typographical errors.

```python
# Appropriate module name.
import utilities

# Inappropriate module name.
import GeneralUtilities
```

**Using underscores to improve readability of modules:**  
When a module has a compound name, using underscores can improve readability.

```python
# Module name with underscore for readability
import data_processing

# Module name without underscore, less readable
import dataprocessing
```

**Naming packages with short, all-Lowercase names:**  
Keeping package names short and lowercase, without underscores, helps maintain a clean and navigable project structure.

```python
# Appropriate package structure
my_project/
    setup.py
    my_module/
        __init__.py
        processing.py

# Inappropriate package structure
MyProject/
    setup.py
    MyModule/
        __init__.py
        DataProcessing.py
```

---

<div id="pep8-class-names"></div>

## Class names

**Using the CapWords convention for class names:**  
Using the CapWords (or PascalCase) convention for naming classes makes it easier to identify classes in the code and follows common practice in the Python community.

```python
# Class name using CapWords
class MyExampleClass:
    pass

# Inappropriate class name
class my_example_class:
    pass
```

**Using function naming convention for callable interfaces:**  
In cases where the interface of a class is documented and used primarily as a callable, the function naming convention can be used.

```python
# Class used as a callable with function name
class process_data:
    def __call__(self, data):
        pass

# Using the class as a callable
processor = process_data()
processor(data)
```

**Builtin Exceptions and Constants:**  
For builtin exceptions and constants, the CapWords convention is also used, distinguishing them from other keywords and builtin functions.

```python
# Exception name using CapWords
class MyException(Exception):
    pass

# Builtin constant name using CapWords
MAX_SIZE = 100
```

---

<div id="pep8-function-and-variable-names"></div>

## Function and Variable Names

**Naming functions with lowercase letters and underscores:**  
Functions should be named using lowercase letters and underscores to separate words, which improves readability.

```python
# Appropriate function name
def calculate_total():
    pass

# Inappropriate function name
def CalculateTotal():
    pass
```

**Naming variables with the same convention as functions:**  
Variables should follow the same naming convention as functions, using lowercase letters and underscores to separate words.

```python
# Appropriate variable name
total_items = 10

# Inappropriate variable name
TotalItems = 10
```

---

<div id="pep8-constants"></div>

## Constants

**Defining constants at the module level:**  
Constants are usually defined at the module level, where they are visible and accessible throughout the module.

```python
# Defining constants at the module level
MAX_OVERFLOW = 100
TOTAL_USERS = 500
```

**Using all capital letters with underscores to separate words:**
Writing constants in all capital letters with underscores separating words helps to distinguish them from regular variables.

```python
# Well-defined constants
MAX_TIME = 3600
ATTEMPT_LIMIT = 5
```

**Defining constants for global settings:**  
Constants are often used to define global settings that should not be changed during the program execution.

```python
# Global settings using constants
BUFFER_SIZE = 1024
SERVER_PORT = 8080
```




















































<!--- ( The Python Language Reference (Portuguese Brazilian notes) ) --->

---

<div id="tplr"></div>

## The Python Language Reference (Portuguese Brazilian notes)

 - Este manual de referência descreve a **"Sintaxe"** e a **“Semântica Central”** da linguagem.
 - É *conciso (reduzido ao essencial; em poucas palavras (diz-se de escritos, ideias, discurso etc.); preciso, sucinto, resumido)*, mas tenta ser exato e completo.
 - Ele abrange tópicos como análise léxica, modelo de dados, modelo de execução, sistema de importação, expressões, instruções simples e compostas, entre outros aspectos fundamentais da linguagem.




















































<!--- ( Settings ) --->

---

<div id="venv-environment"></div>

## Creating venv environment

**CREATE VIRTUAL ENVIRONMENT:**  
```bash
python -m venv python-environment
```

**ACTIVATE THE VIRTUAL ENVIRONMENT (LINUX):**  
```bash
source python-environment/bin/activate
```

**ACTIVATE THE VIRTUAL ENVIRONMENT (WINDOWS):**  
```bash
source python-environment/Scripts/activate
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

---

<div id="python-from-source"></div>

## Install Python From Source

To install Python from source, first we need some requirements (like C Compiler):

For Debian, Ubuntu, or other apt-based systems:

```bash
sudo apt install build-essential
```

```bash
sudo apt install libssl-dev zlib1g-dev libncurses5-dev \
  libncursesw5-dev libreadline-dev libsqlite3-dev libgdbm-dev \
  libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev libffi-dev \
  tk-dev \
  uuid-dev
```


Now, let's clone the repository:

```bash
git clone https://github.com/python/cpython
```

Enter the CPython directory:

```bash
cd cpython
```

Checkout to the specific branch:

```bash
git branch -a
```

```bash
* main
  remotes/origin/3.10
  remotes/origin/3.11
  remotes/origin/3.12
  remotes/origin/3.13
  remotes/origin/3.8
  remotes/origin/3.9
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
```

For example, let's checkout to the **"3.13 branch"**:

```bash
git checkout 3.13
```

Now let's prepare the system for compilation, configuring options and checking dependencies:

```bash
./configure --with-pydebug
```

 - `./configure`
   - This script is used to prepare the build environment, checking dependencies and configuring specific build options. It is the first step in the building process for many software packages that use the autotools build system.
 - `--with-pydebug`
   - This is an argument passed to the configure script that specifies that the Python build should include debug symbols and other settings that make debugging the Python interpreter easier.
   - This includes, for example, additional error checks, extra assertions, memory allocation tracking, among others.

To compile the CPython code run the following command:

```bash
make -j
```

 - `make`
   - Invokes the *make* utility, which reads the *Makefile* to determine how to build the project.
 - `-j`
   - Specifies that *make* should run multiple jobs in parallel.
   - **NOTE:** When a number is not provided (e.g. -j2), make will attempt to run as many jobs in parallel as possible, depending on the resources available on the system.

**OUTPUT:**
```bash
Checked 112 modules (33 built-in, 78 shared, 1 n/a on linux-x86_64, 0 disabled, 0 missing, 0 failed on import)
```

This indicates that during compilation, 112 modules were checked:

 - 33 modules are integrated (built-in).
 - 78 modules are shared.
 - 1 module does not apply (n/a) to the linux-x86_64 platform.
 - No modules were disabled.
 - No modules are missing.
 - No module failed on import.

Now, let's run the tests:

```bash
./python -m test -j3
```

 - The command `./python -m test -j3` is used to run the Python test suite.
 - The suite tests are located in the `Lib/test` directory within the Python source code. This directory contains a series of test files that are used to verify the *integrity* and *functionality* of the Python implementation.

Finally, let's install the compiled Python on the system:

```bash
sudo make altinstall
```










---

<div id="contribute-process"></div>

## Contribute Process

**STEP-x:** Fork the project.  
To contribute to [CPython](https://github.com/python/cpython)the first step is to Fork the repository.

**STEP-x:** Clone the forked repository.  
Now, we need clone the forked repository on our local machine:

```bash
git clone https://github.com/your-username/cpython
```

**STEP-x:** Add a remote.  
Now, we need to define a new remote pointing to the original project:

```bash
git remote add upstream https://github.com/python/cpython
```

 - **Now you have two remotes for this project:**
 - **origin:**
   - The *"origin"* that points to your fork of the project on GitHub:
     - You have *"read"* and *"write"* access to this remote.
 - **upstream:**
   - The *"upstream"* that points to the main repository of the project on GitHub:
     - You only have *"read"* access to this remote.

> **NOTE:**  
> You can view these remotes with the command **git remote -v**:

```bash
git remote -v
```

**OUTPUT:**  
```bash
origin  https://github.com/rodrigols89/cpython (fetch)
origin  https://github.com/rodrigols89/cpython (push)
upstream        https://github.com/python/cpython (fetch)
upstream        https://github.com/python/cpython (push)
```

**STEP-x:** Install Python.  
Now, we need to install Python on our local machine. You can follow the ["Install Python From Source"](#python-from-source) process.


**STEP-x:** Get updates.  
Before working in the project, we need to get updates from the **upstream repository (Main repository)** to **origin repository (Your fork)**.

```bash
git remote update origin upstream --prune
```

 - `git remote update`
   - Updates all the configured remote repositories in your local repository.
   - It fetches all the changes from the remotes but does not merge them into your local branches.
 - `origin upstream`
   - Specifies the remotes to be updated.
   - In this case, it updates both the **"origin"** and **"upstream"** remotes.
 - `--prune`
   - Removes any local references to remote branches that have been deleted on the remote server.
   - This helps keep your local repository clean and in sync with the remote repositories.

```bash
git checkout <branch> # where <branch> is the branch you want to get updates.
git pull upstream <branch>
git push origin <branch>
```

 - `git checkout <branch>`
   - We ensured that we were on the `<branch>` we want to work in.
 - `git pull upstream <branch>`
   - The command **"git pull upstream"** fetches the data from the *upstream remote (Main repository)*.
 - `git push origin <branch>`
   - The command **"git push origin"** sends the data fetched from the original project (upstream) to my GitHub (origin).

**STEP-x:** Create a new branch.  
Next, we must create a new branch from the branch we want to work in. For example, let's create a new branch from the `3.13` branch:

```bash
git checkout -b fix-issue-12345 3.13
```

 - `fix-issue-12345` The `name` of the *new branch*.
   - `fix-issue` means fixing an issue.
   - `12345` is the issue number.
 - `3.13`
   - The `branch` we want to work in.
   - It could be main or anything else (Poderia ser a main ou qualquer outra).

**STEP-x:** Make changes/implementations.  
Now, we can do some **changes** or **implementations**.

**STEP-x:** Run the tests and the patchcheck.  
After *changes* or *implementations*, we need to run the **"tests"** and the **"patchcheck"**:

```bash
./python -m test -j3
```

```bash
make patchcheck
```

**STEP-x:** Commit changes.  
Now, we need to **commit** the changes.

```bash
git add .
```

```bash
git commit -S -m "fix issue 12345"
```

**STEP-x:** Merge changes.  
Now, we need to merge the changes to the `3.13` branch:

```bash
git checkout 3.13
```

```bash
git -S merge fix-issue-12345
```

**STEP-x:** "Get updates" and "tests/patchcheck" (again).  
Before doing a P.R we need to check for **updates** and run the **"tests"** and the **"patchcheck"** again.

**STEP-x:** Push changes.  
Now, we need to **push** the changes to our local repository.

```bash
git push origin 3.13
```

**STEP-x:** Create Pull Request.  
To create a P.R, we need to follow the following syntax:

```bash
gh-NNNN
```

> **NOTE:**  
> If you are fixing *"issue"* number *"12345"*, you should include **gh-12345** in the pull request description.

**EXAMPLE:**
```bash
gh-12345: Fix some bug in spam module
```




















































<!--- ( References ) --->

---

<div id="ref"></div>

## REFERENCES

 - **Books:**
   - [CPython Internals: Your Guide to the Python 3 Interpreter](https://www.amazon.com/CPython-Internals-Guide-Python-Interpreter/dp/1775093344)
   - [Inside The Python Virtual Machine](https://leanpub.com/insidethepythonvirtualmachine)
 - **Videos:**
   - [Como o interpretador do Python funciona? | Live de Python #218](https://www.youtube.com/watch?v=pxfZTAJDipY)
 - **Tutorials:**
   - [Your Guide to the CPython Source Code](https://realpython.com/cpython-source-code-guide/)
 - **Requirements:**
   - **Regular Expressions (Abbreviated as "Regex"):**
     - [Regular Expressions (Brilliant)](https://brilliant.org/wiki/regular-expressions/)
   - **Extended Backus–Naur form (EBNF):**
     - [Extended Backus–Naur form (Wikipedia)](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form)
     - [Extended Backus–Naur Form (EBNF)](https://plantuml.com/ebnf#:~:text=Extended%20Backus%E2%80%93Naur%20Form%20(EBNF)%20is%20a%20type%20of,of%20the%20Algol%20programming%20language.)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
