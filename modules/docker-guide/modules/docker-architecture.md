# Arquitetura Docker (+Componentes)

## Contents

 - [01 - Introdução a Arquitetura Docker](#01)
 - [02 - The Docker daemon](#02)
 - [03 - The Docker client](#03)
 - [04 - Docker Desktop](#04)
 - [05 - Docker registries](#05)
 - [06 - Docker objects](#06)
 - [07 - Images](#07)
 - [08 - Containers](#08)

---

<div id="01"></div>

## 01 - Introdução a Arquitetura Docker

> Docker usa uma arquitetura **cliente-servidor**.

 - O **cliente Docker** se comunica com o **Docker daemon**, que faz o trabalho pesado de construção, execução e distribuição de seus contêineres Docker.
 - O cliente Docker e o daemon podem ser executados no mesmo sistema ou você pode conectar um cliente Docker a um daemon remoto do Docker.
 - O cliente Docker e o daemon se comunicam usando uma **API REST**, por sockets UNIX ou uma interface de rede.
 - Outro cliente Docker é o **Docker Compose**, que permite trabalhar com aplicativos que consistem em um conjunto de contêineres.

Veja uma abstração desses componentes abaixo:

![img](images/docker-components.png)  

---

<div id="02"></div>

## 02 - The Docker daemon

O **Docker daemon (dockerd)** escuta as solicitações da **API Docker** e gerencia objetos Docker, como **imagens**, **contêineres**, **redes** e **volumes**.

**NOTE:**  
Um daemon também pode se comunicar com outros daemons para gerenciar serviços Docker.

---

<div id="03"></div>

## 03 - The Docker client

O **Cliente Docker (docker)** é a principal maneira pela qual muitos usuários do Docker interagem com o Docker. Quando você usa comandos como docker **run**, o cliente envia esses comandos para `dockerd`, que os executa.

> O comando `docker` usa a API Docker.

**NOTE:**  
O **Cliente Docker** pode se comunicar com *mais de um daemon*.

---

<div id="04"></div>

## 04 - Docker Desktop

O **Docker Desktop** é um aplicativo fácil de instalar para seu ambiente **Mac** ou **Windows** que permite criar e compartilhar aplicativos e microsserviços em contêineres. O Docker Desktop inclui:

 - O Docker daemon (dockerd);
 - O cliente Docker ( docker);
 - Docker Compose;
 - Docker Content Trust;
 - Kubernetes;
 - E credencial Helper.

Para obter mais informações, consulte [Docker Desktop](https://docs.docker.com/desktop/).

---

<div id="05"></div>

## 05 - Docker registries

> O **Docker registry** *armazena* imagens *Docker*.

**NOTE:**  
O Docker Hub é um registro público que qualquer pessoa pode usar e o Docker está configurado para procurar imagens no Docker Hub por padrão. Você pode até executar seu próprio registro privado.

 - Quando você usa os comandos **docker pull** ou **docker run**, as imagens necessárias são retiradas do registro configurado.
 - Quando você usa o comando **docker push**, sua imagem é enviada para o registro configurado.

---

<div id="06"></div>

## 06 - Docker objects

Ao usar o Docker, você está **criando** e **usando**:

 - Imagens;
 - Contêineres;
 - Redes;
 - Volumes
 - Plug-ins e outros objetos...

---

<div id="07"></div>

## 07 - Images

> Uma imagem é um modelo de somente leitura com instruções para criar um contêiner do Docker.

**NOTE:**  
Frequentemente, uma imagem é baseada em outra imagem, com alguma personalização adicional. Por exemplo, você pode construir uma imagem que é baseada na imagem **ubuntu**, mas instala o servidor web Apache e seu aplicativo, bem como os detalhes de configuração necessários para fazer seu aplicativo funcionar.

Você pode criar suas próprias imagens ou usar apenas aquelas criadas por terceiros e publicadas em um registro. Para construir sua própria imagem, você cria um **Dockerfile** com uma sintaxe simples para definir as etapas necessárias para criar a imagem e executá-la. Cada instrução em um **Dockerfile** cria uma camada na imagem. Quando você altera o **Dockerfile** e reconstrói a imagem, apenas as camadas que foram alteradas são reconstruídas. Isso é parte do que torna as imagens tão leves, pequenas e rápidas, quando comparadas a outras tecnologias de virtualização.

---

<div id="08"></div>

## 08 - Containers

> Um contêiner é uma instância executável de uma imagem.

Você pode **criar**, **iniciar**, **parar**, **mover** ou **excluir** um contêiner usando a API Docker ou CLI. Você pode conectar um contêiner a uma ou mais redes, anexar armazenamento a ele ou até mesmo criar uma nova imagem com base em seu estado atual.

Por padrão, um contêiner está relativamente bem isolado de outros contêineres e de sua máquina host. Você pode controlar o quão isolados estão a rede, o armazenamento ou outros subsistemas subjacentes de um contêiner de outros contêineres ou da máquina host.

Um contêiner é definido por sua imagem, bem como por quaisquer opções de configuração fornecidas a ele ao criá-lo ou iniciá-lo. Quando um contêiner é removido, todas as alterações em seu estado que não são armazenadas no armazenamento persistente desaparecem.


---

**REFERENCES:**  
[Docker overview](https://docs.docker.com/get-started/overview/)
