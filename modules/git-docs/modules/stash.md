# Stash  

## Contents

 - [Introdução ao git stash](#intro)
 - [Fazendo stash do seu trabalho](#create-stash)
 - [Listando suas stashes](#list)
 - [Usando uma stash](#using-stash)
 - [Removendo uma stash](#drop)
 - [Criando uma branch ("temp" por exmeplo) a partir de uma stash](#stash-to-branch)

---

<div id="intro"></div>

## Introdução ao git stash

Muitas vezes, quando você está trabalhando em uma parte do seu projeto, as coisas estão em um estado confuso e você quer mudar de branch por um tempo para trabalhar em outra coisa. O problema é, você não quer fazer o commit de um trabalho incompleto somente para voltar a ele mais tarde. A resposta para esse problema é o comando <strong>git stash</strong>.

Fazer <strong>Stash (esconder, juntar, acumular)</strong> é tirar o estado sujo do seu diretório de trabalho — isto é, seus arquivos modificados que estão sendo rastreados e mudanças na área de seleção — e o salva em uma pilha de modificações inacabadas que você pode voltar a qualquer momento.

---

<div id="create-stash"></div>

## Fazendo stash do seu trabalho

Para começar imagine que você entra no seu projeto e começa a trabalhar em alguns arquivos e adiciona alguma modificação na área de seleção. Se você executar <strong>git status</strong>, você pode ver seu estado sujo:

```
$ git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#      modified:   index.html
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   lib/simplegit.rb
#  
```

Agora você quer mudar de branch, mas não quer fazer o commit do que você ainda está trabalhando; você irá fazer o **stash** das modificações. Para fazer um novo **stash** na sua pilha, execute <strong>git stash</strong>:  

```
$ git stash
Saved working directory and index state \
  "WIP on master: 049d078 added the index file"
HEAD is now at 049d078 added the index file
(To restore them type "git stash apply")  
```

Seu diretório de trabalho está limpo novamente agora:

```
$ git status
# On branch master
nothing to commit, working directory clean
```

**NOTE:**  
Neste momento, você pode facilmente mudar de branch e trabalhar em outra coisa; suas alterações estão armazenadas na sua pilha.

---

<div id="list"></div>

## Listando suas stashes

Para ver as stashes que você guardou, você pode usar o comando <strong>git stash list</strong>:

```  
git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051... Revert "added file_size"
stash@{2}: WIP on master: 21d80a5... added number to log 
```

**NOTE:**  
Nesse caso, duas stashes tinham sido feitas anteriormente, então você tem acesso a três trabalhos stashed diferentes.

---

<div id="using-stash"></div>

## Usando uma stash

> Você pode aplicar para qualquer uma das stashes listadas no comando **git stash list** com o comando **git stash apply**.

 - Se você quer aplicar para um dos stashes mais antigos, você pode especificá-lo, assim <strong>git stash apply stash@{2}</strong>.
 - Se você não especificar um stash, Git assume que é o stash mais recente e tenta aplicá-lo.

```
$ git stash apply
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   index.html
#      modified:   lib/simplegit.rb
#  
```

---

<div id="drop"></div>

## Removendo uma stash

> A opção **apply** somente tenta aplicar o stash armazenado — ele continua na sua pilha. Para removê-lo, você deve executar o comando <strong>git stash drop</strong> com o nome do stash que quer remover.

**CONSOLE:**
```
git stash list
```

**OUTPUT:**
```
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051... Revert "added file_size"
stash@{2}: WIP on master: 21d80a5... added number to log
```

**CONSOLE:**
```
git stash drop stash@{0}
```

**OUTPUT:**
```
Dropped stash@{0} (364e91f3f268f0900bc3ee613f9f733e82aaed43)  
```

**NOTE:**  
Você também pode executar <strong>git stash pop</strong> para aplicar o stash e logo em seguida apagá-lo da sua pilha:  

**CONSOLE:**
```  
git stash pop stash@{0}
```

**OUTPUT:**
``` 
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   aaaa.js

Dropped stash@{0} (a16e7ef845316efea62b9f2ea8e70c557e727222)  
```

---

<div id="stash-to-branch"></div>

## Criando uma branch ("temp" por exmeplo) a partir de uma stash

Se você criar um stash, deixá-lo lá por um tempo, e continuar no branch de onde criou o stash, você pode ter problemas em reaplicar o trabalho. Se o apply tentar modificar um arquivo que você alterou, você vai ter um conflito de merge e terá que tentar resolvê-lo.

Se você quer uma forma mais fácil de testar as modificações do stash novamente, você pode executar <strong>git stash branch</strong>, que cria um novo branch para você, faz o checkout do commit que você estava quando criou o stash, reaplica seu trabalho nele, e então apaga o stash se ele é aplicado com sucesso:

**CONSOLE:**
```
git stash branch testchanges
```

**OUTPUT:**
```
Switched to a new branch "testchanges"
# On branch testchanges
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#      modified:   index.html
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#
#      modified:   lib/simplegit.rb
#
Dropped refs/stash@{0} (f0dfc4d5dc332d1cee34a634182e168c4efc3359)
```

**NOTE:**  
Este é um bom atalho para recuperar facilmente as modificações em um stash e trabalhar nele em um novo branch.

---

**REFERENCES:**  
https://git-scm.com/book/pt-br/v1/  
https://git-scm.com/book/en/v2/  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
