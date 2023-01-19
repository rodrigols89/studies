# Setting

## Contents

 - [Configurando sua identidade (Username + Email)](#identity)
 - [Verificando suas configurações (git config --list)](#check)

---

<div id="identity"></div>

## Configurando sua identidade (Username + Email)

A primeira coisa que você deve fazer quando instalar o **Git** é definir o seu:

 - **Nome de usuário;**
 - **Endereço de e-mail.**

Isso é importante porque todos os commits no **Git** utilizam essas informações, e está imutavelmente anexado nos commits que você realizar:

```python
$ git config --global user.name "drigols"
$ git config --global user.email drigols.creative@gmail.com
```
  
Relembrando, você só precisará fazer isso uma vez caso passe a opção <strong>--global</strong>, pois o Git sempre usará essa informação para qualquer coisa que você faça nesse sistema.

> **NOTE:**  
> Caso você queira sobrepor estas com um nome ou endereço de e-mail diferentes para projetos específicos, você pode executar o comando <strong>sem a opção --global</strong> quando estiver no próprio projeto.

---

<div id="check"></div>

## Verificando suas configurações (git config --list)

Caso você queira verificar suas configurações, você pode utilizar o comando **git config --list** para listar todas as configurações que o Git encontrar naquele momento:

```python
user.name=drigols
user.email=drigols.creative@gmail.com
core.editor=emacs
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
```

**NOTE:**  
Você também pode verificar qual o valor que uma determinada **chave** tem para o **Git** digitando **git config {key}**:

**Check username:**  
```python
git config user.name
drigols
```

**Check email:**  
```python
git config user.email
drigols.creative@gmail.com
```

---

**REFERENCES:**  
https://git-scm.com/book/pt-br/v1/  
https://git-scm.com/book/en/v2/  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
