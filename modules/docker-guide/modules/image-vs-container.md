# Docker Image vs Docker Container

## Contents

- [01 - Analogia baseada em Orientação a Objetos](#01)
- [02 - Diferenças cruciais entre Docker Image e Docker Container](#02)

---

<div id="01"></div>

## 01 - Analogia baseada em Orientação a Objetos

Uma boa *abordagem* para diferenciar **imagens** e **contêineres** é tentar pensar em uma **linguagem de programação orientada a objetos**. Em tal analogia:

 - A **classe** representa a **imagem**;
 - Enquanto sua **instância**, **o objeto**, é o **contêiner**.

```
+-----------------------------+-------+-----------+
|             Domain          | Meta  | Concrete  |
+-----------------------------+-------+-----------+
| Docker                      | Image | Container |
| Object oriented programming | Class | Object    |
+-----------------------------+-------+-----------+
```

**NOTE:**  
A mesma imagem pode criar mais contêineres, assim, como uma classe pode ser utilizada para criar vários objetos.

```
Você pode ver todas as suas imagens com docker imagesenquanto você pode ver seus contêineres em execução com docker ps(e você pode ver todos os contêineres com docker ps -a).
```

---

<div id="02"></div>

## 02 - Diferenças cruciais entre Docker Image e Docker Container

Embora seja mais simples pensar em um contêiner como uma imagem em execução, isso não é muito preciso.

> Uma imagem é, na verdade, um modelo que pode ser transformado em um contêiner.

Para transformar uma imagem em um contêiner, o mecanismo Docker pega a imagem, adiciona:

 - Um sistema de arquivos de leitura e gravação;
 - Inicializa várias configurações;
 - Inclui portas de rede;
 - Nome do contêiner
 - ID
 - Volume
 - Limites de recursos...

**NOTE:**  
Um contêiner em execução tem um processo em execução no momento, mas um contêiner também pode ser interrompido (ou encerrado na terminologia do Docker). Um contêiner encerrado não é o mesmo que uma imagem, pois pode ser reiniciado e manterá suas configurações e quaisquer alterações no sistema de arquivos.

**NOTE:**  
Outra observação crucial é que esse contêiner interrompido vai manter as configurações e alterações, mas a imagem nós utilizamos para criar nosso contêiner vai permanecer imutável - Ou seja, se nós quisermos mudar algo na Imagem não fazemos isso a partir do contêiner e sim do **Dockerfile**.

---

**REFERENCES:**  
[Which is the difference between a Docker image and a container? How to create a docker file](https://www.iperiusbackup.net/en/docker-image-container-howto-create-dockerfile/)
