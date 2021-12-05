# O que é Docker?

## Contents

 - [01 - Definição não formal de Docker](#01)
 - [02 - Docker e o modelo de isolamento](#02)

---

<div id="01"></div>

## 01 - Definição não formal de Docker

De forma bem resumida, podemos dizer que o Docker é uma plataforma aberta, criada com o objetivo de **facilitar o desenvolvimento**, **a implantação e a execução de aplicações em ambientes isolados (lembre dessa parte)**. Foi desenhada especialmente para disponibilizar uma aplicação da forma mais rápida possível.

---

<div id="02"></div>

## 02 - Docker e o modelo de isolamento

> Essa talvez seja a parte mais crucial do Docker que deixa ele tão diferente de tudo.

O **modelo de isolamento** utilizado no Docker é a **virtualização a nível do sistema operacional**:

> Um método de virtualização onde o kernel do sistema operacional permite que múltiplos processos sejam executados isoladamente no mesmo host.

**NOTE:**  
Esses processos isolados em execução são denominados no Docker de **container**.

Veja a imagem abaixo:

![img](images/docker2.png)  

Para criar o isolamento necessário do processo, o Docker usa a funcionalidade do kernel, denominada de **[namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html) (Isso mesmo, igual nas linguagens de programação como C++)**, que cria ambientes isolados entre containers:

> os processos de uma aplicação em execução não terão acesso aos recursos de outra. A menos que seja expressamente liberado na configuração de cada ambiente.

**NOTE:**  
Para evitar a exaustão dos recursos da máquina por apenas um ambiente isolado, o Docker usa a funcionalidade **[cgroups](https://en.wikipedia.org/wiki/Cgroups)** do kernel, responsável por criar limites de uso do hardware a disposição. Com isso é possível coexistir no mesmo host diferentes containers sem que um afete diretamente o outro por uso exagerado dos recursos compartilhados.

---

**REFERENCES:**  
[O que é Docker?](https://stack.desenvolvedor.expert/appendix/docker/oquee.html)
