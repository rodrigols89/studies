# O que é Python

# 01 - Interpretador

- Você provavelmente já ouviu ou leu em algum lugar que Python é uma linguagem interpretada ou uma linguagem de script.
- Em certo sentido, também é verdade que Python é tanto uma linguagem interpretada quanto uma linguagem compilada.
- Um compilador traduz linguagem Python em linguagem de máquina - código Python é traduzido em um código intermediário que deve ser executado por uma máquina virtual conhecida como PVM (Python Virtual Machine).
-  É muito similar ao Java - há ainda um jeito de traduzir programas Python em bytecode Java para JVM (Java Virtual Machine) usando a implementação Jython.

#### Interpretador vs Compitador

- O **interpretador** faz esta **'tradução'** em tempo real para código de máquina, ou seja, em tempo de execução.
  - Interpretador interrompe a tradução quando encontra um primeiro erro.
- Já o **compilador** *traduz o programa inteiro em código de máquina de uma só* vez e então o executa, criando um arquivo que pode ser rodado (executável).
  - O compilador gera um relatório de erros (casos eles existam).

Mas devemos compilar script Python? Como compilar? Normalmente, não precisamos fazer nada disso porque o Python está fazendo isso para nós, ou seja, ele faz este passo automaticamente. Na verdade, é o interpretador Pyhton, o **CPython**. A diferença é que em Java é mais clara essa separação, o programador compila e depois executa o código.
