# Bootcamp de Data Science do canal Stack (Outubro 2021)

> Meus códigos e exemplos do Bootcamp de Data Science do canal [Stack do Youtube](https://www.youtube.com/c/Stack_tecnologias/featured).

![img](images/logo.jpg)  

## Conteúdo

 - [Data Science Lifecycle](#ds-lifecycle)
 - [Qual problema (problem) vamos resolver?](#problem)
 - [Como criar um Overview da solução](#overview)
 - [Trabalhar com Docker](#docker)
 - [Trabalhando com Docker com MySQL no VSCode](#vscode)
 - [Instalação e Configuração do Data Lake com Minio Server](#data-like-minion-server)

---

<div id="ds-lifecycle"></div>

## Data Science Lifecycle

Bem, o **Data Science Lifecycle** nada mais é do que:

> **O Ciclo de Vida de um Projeto de Data Science.**

Veja como funciona esse ciclo abaixo:

![img](images/data-science-lifecycle.png)  

---

<div id="problem"></div>

## Qual problema (problem) vamos resolver?

Um problema que eu tinha até então *(estou tentando melhorar com isso)* é só estudar, estudar e estudar e não resolver nenhum tipo de problema.

> **Você tem que ter em mente que *Programadores*, *Cientistas de Dados*, *Engenheiros* `resolvem problemas` e não ficam só estudando!**

**Sabendo disso, qual tipo de problema nós vamos resolver nesse Bootcamp?**  
Bem, não sei se vocês já sabem, mas é muito **difícil (e caro)** uma empresa contratar um profissional que atenda aos requisitos da empresa. Por isso, é muito interessante que quando contratado o profissional permaneça o máximo de tempo possível na empresa.

> **Mas como impedir (ou tentar) que esses profissionais não saiam da empresa?**

**NOTE:**  
Esse é o problema que nós vamos tentar resolver.

Para resolver esse problema, nós vamos ter que responder várias questões como:

 - Quais fatores influenciam para um colaborador deixar a empresa?
 - Como reter esses colaboradores?
 - Podemos nos antecipar e saber se um determinado colaborador vai sair *(ou tentar)* da empresa?
 - Como diminuir o *turnover*?
   - **Turnover:** Turnover significa a taxa de rotatividade de colaboradores em uma empresa. Ou seja, o número de novos colaboradores comparado àqueles profissionais que deixam o ambiente de trabalho. Esse é um termo popular no setor de Recursos Humanos, relacionado com contratações e desligamentos de colaboradores.

---

<div id="overview"></div>

## Como criar um Overview técnico da nossa solução

Bem, como o nome já diz **Overview** é uma visão geral. Mas geral do que? No nosso caso, nosso problema. Ou seja, uma visão geral de como nós vamos resolver tecnicamente.

**Primeiro vamos começar vendo isso visualmente:**

![img](images/overview.png)  

---

<div id="docker"></div>

## Trabalhar com Docker

**NOTE:**  
Essa introdução inicial eu não aprendi no Bootcamp, porém, vou deixar aqui para que fique de exemplo para outras pessoas aprenderem mais sobre o assunto.

> O Docker é um software que nos permite *"conteinizar"* **recursos**, **softwares** e **outros recursos** em nossa máquina real.

Por exemplo:

 - Queremos testar uma versão x do Python;
 - Ou instalar uma versão específica do MySQL...

Estas instalações são salvas em nosso computador e muitas vezes quando não precisamos mais delas nós as removemos e ficamos com pacotes quebrados em nossa máquina e isso pode causar uma série de problemas.

Com o Docker nós criamos uma virtualização *(por exemplo, uma máquina virtual Linux)* para instalar esses recursos e quando não precisarmos mais deles, basta deletar o que foi instalado na virtualização. Isso é bastante interessante porque seguindo essa abordagem, o que foi instalado foi instalado apenas na máquina virtual e não na nossa máquina real.

### The Docker Toolbox

 - O [The Docker Toolbox](https://github.com/docker-archive/toolbox) é um projeto descontinuado do Docker que eu utilizei para poder simular o Docker atual.
 - Isso, porque minha versão do **Windows (Windows 10 Enterprise 2016 LTSB)** não permite instalar o Docker do site oficial.

**NOTE:**  
Se você também está passando por esse tipo de problema uma alternativa é baixar o Docker Toolbox, [aqui](https://github.com/docker-archive/toolbox/releases/tag/v19.03.1).

### Verificando a versão do Docker

Para verificar a versão atual do seu Docker é muito simples, basta digita **docker -v** no console do Docker.

**OUTPUT:**  
```
Docker version 19.03.1, build 74b1e89e8a
```

### Verificando/Testando se o Docker está instalado corretamente

Para verificar (ou testar) se o Docker está instalado corretamente uma maneira é baixar uma imagem de teste. Isso é muito simples, basta digitar o seguinte:

```
$ docker run -d -p 80:80 docker/getting-started
```

**NOTE:**  
Veja que nós estamos baixando a imagem **getting-started** que é uma imagem inicial do Docker. Agora como ver se essa imagem foi mesmo baixada?

```
docker images
```

**OUTPUT:**  
```
REPOSITORY               TAG                 IMAGE ID            CREATED             SIZE
docker/getting-started   latest              083d7564d904        4 months ago        28MB
```

**NOTE:**  
Veja que com o comando **docker images** nós conseguimos ver quantas máquinas (images) estão instalados no nosso docker. Outra alternativa é utilizar o comando **docker image ls**:

```
docker image ls
```

**OUTPUT:**  
```
REPOSITORY               TAG                 IMAGE ID            CREATED             SIZE
docker/getting-started   latest              083d7564d904        4 months ago        28MB
```

Vejam que o resultado é o mesmo.

### Instalando uma imagem Docker com MySQL

Ok, mas como eu posso criar uma imagem *(máquina virtual)* Docker com o **MySQL** já instalado? É muito simples, veja o exemplo abaixo:

```
docker run --rm --name mysqlbd1 -e MYSQL_ROOT_PASSWORD=bootcamp -p "3307:3306" -d mysql
```

Mas o que significa todos esse comandos?

 - **docker**
   - o docker é o principal, pois é a ferramenta para criação de containers *(o resto são parâmetros do docker)*.
 - **run**
   - O comando **run** é responsável por executar o container.
 - **--rm**
   - Significa que se estiver uma imagem com o mesmo nome que nós vamos nomear a que estamos criando, o docker vai remover a antiga e criar uma nova com esse nome.
 - **--name**
   - Esse é muito fácil, é o nome da imagem que estamos criando.
 - **-e**
   - Esse comando é utilizado quando queremos criar uma **variável de ambiente** = `MYSQL_ROOT_PASSWORD=bootcamp` no nosso caso
 - **-p**
   - O comando **-p** é utilizado (nesse exemplo) para mapear as portas entre o meu *container (image)* e a porta do meu *sistema operacional (máquina local)*. Por exemplo, quando nós colocamos **-p "3307:3306"**, significa que a porta 3307 do meu host (máquina local) vai se comunicar com a porta 3306 do meu container (image). Por que 3306? Porque é a porta padrão do serviço MySQL.
   - Por que eu mudei o da minha máquina host (local) para 3307? Porque nós podemos ter outros serviço MySQL trabalhando locamente nessa porta e pode dar conflito na hora do nosso container (image) tentar utilizar essa porta.
   - Por fim, você pode dizer que estamos mapeando a porta 3306 do container para a porta 3307 do host (máquina local).
 - **-d**
   - O comando **-d** executa o container em background *(como um daemon)*.
 - mysql
   - Significa que vamos ter o mysql instalado

### Verificando Containers em Execução

Agora como eu vejo os containers que estão em execução? Simples: **docker ps** ou **docker ps -a**

```
docker ps
```

**OUTPUT:**  
```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                               NAMES
23cb8a4bb7cd        mysql               "docker-entrypoint.s…"   8 hours ago         Up 8 hours          33060/tcp, 0.0.0.0:3307->3306/tcp   stack-image
```

**NOTE:**  
O comando **docker ps** mostra os containers que estão realmente em execução. Para ver todos os containers e seus status você pode utilizar o comando **docker ps -a**:

```
docker ps -a
```

**OUTPUT:**  
```
CONTAINER ID        IMAGE                    COMMAND                  CREATED             STATUS                   PORTS                               NAMES
a5e2d4d001fb        mysql                    "docker-entrypoint.s…"   7 hours ago         Created                                                      mysqlbd1
23cb8a4bb7cd        mysql                    "docker-entrypoint.s…"   8 hours ago         Up 8 hours               33060/tcp, 0.0.0.0:3307->3306/tcp   stack-image
53b4f89630a5        docker/getting-started   "/docker-entrypoint.…"   10 hours ago        Exited (0) 7 hours ago                                       admiring_elbakyan
```

### Executando e Parando Containers

Para executar e para os serviços de um container é muito simples, basta utilizar os comandos:

```
// Para startar.
docker start nome-do-container/id

// Para parar
docker stop nome-do-container/id
```

---

<div id="vscode"></div>

## Trabalhando com Docker com MySQL no VSCode

Os primeiros passos que você deve fazer se desejar trabalhar com MySQL que está no seu Docker e o VSCode é baixar as seguintes extensões do VSCode:

 - [Docker](https://github.com/microsoft/vscode-docker)
 - [Database Client](https://github.com/cweijan/vscode-database-client)

Com as extensões instaladas agora vamos criar no ícone **Database** no lado esquerdo do VSCode:

![img](images/database-client-01.png)  

Agora vamos clicar no mais (+) para configurar uma conexão com o Bando de Dados MySQL:

![img](images/database-client-02.png)  

**NOTE:**  
Veja que nós também podemos criar conexões com outros tipos de Banco de Dados e também serviços de *SSH* e *FTP*.

**NOTE:**  
Como eu não estou utilizado o Docker oficial, estou utilizando uma versão descontinuada eu não sei o motivo, mas o **IP** do host não é o meu sugerido, ao invés disso eu utilizei o do Docker Toolbox:

![img](images/docker-toolbox.png)  
![img](images/database-client-03.png)  

**NOTE:**  
Veja que a conexão foi bem-sucedida! Esses bancos de dados que foram listados do lado esquerdo são os bancos de dados padrãodo MySQL.

---

<div id="data-like-minion-server"></div>

## Instalação e Configuração do Data Lake com Minio Server

Vamos começar criando o diretório **datalake**:

```
mkdir datalake
```

Agora vamos criar outro container com o **MinIO Server**:

**NOTE:**  
Vale salientar que esse comando só vai funcionar se você estiver na pasta raiz, por exemplo, `C:\`.

```
docker run -d -p 9000:9000 -p 9001:9001 -v "$PWD/datalake:/data" minio/minio server /data --console-address ":9001"

docker run -d -p 9000:9000 -p 9001:9001 --name minio1 -v C:/stack-bootcamp-ds-2021-10/datalake:/data server /data --console-address ":9001"

docker run -d -p 9000:9000 -p 9001:9001 --name minio1 -v C:\data:/data server /data --console-address ":9001"

docker run \
  -p 9000:9000 \
  -p 9001:9001 \
  --name minio1 \
  -e "MINIO_ROOT_USER=AKIAIOSFODNN7EXAMPLE" \
  -e "MINIO_ROOT_PASSWORD=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY" \
  -v C:\stack-bootcamp-ds-2021-10\datalake:/data \
  quay.io/minio/minio server /data --console-address ":9001"
```

 - **docker**
   - o docker é o principal, pois é a ferramenta para criação de containers *(o resto são parâmetros do docker)*.
 - **run**
   - O comando **run** é responsável por executar o container.
 - **-d**
   - O comando **-d** executa o container em background *(como um daemon)*.
 - **-p**
   - Mais uma vez para fazer o mapeamento de portas
   - Como o MinIO trabalha nas porta 9000 e 9001 foi feito 2 mapeamentos das portas 9000 e 9001 entre host (máquina local) com o container (imagem).
 - **-v**
   - O comando **-v** consiste em criar um **volume de persistência**.
   - O que isso significa? Significa, que esse diretório do host (máquina local) será compartilhado com o meu container (imagem).

xSe tudo ocorrer bem você vai poder ir na Aplicação Web do MinIO:

```
Abra o browser e digite: [http://localhost:9001/login](http://localhost:9001/login)
username: minioadmin
password: minioadmin
```

x



---

**REFERÊNCIA:**  
[Stack - Youtube](https://www.youtube.com/c/Stack_tecnologias/featured)
[+Comandos básicos Docker](https://medium.com/xp-inc/principais-comandos-docker-f9b02e6944cd)
