# Docker Images

## Contents

 - [01 - Listando Imagens do seu Docket Host](#01)

---

<div id="01"></div>

## 01 - Listando Imagens do seu Docket Host

Para iniciar um **container** é necessário saber a partir de qual **imagem** será executado. Para listar as imagens que seu *Docker host* tem localmente nós podemos utilizar os comando **docker image list** ou **docker image ls**:

```
docker image list
docker image ls
```

**OUTPUT:**  
```
REPOSITORY               TAG       IMAGE ID       CREATED       SIZE
minio/minio              latest    01431999f934   10 days ago   393MB
mysql                    latest    b05128b000dd   2 weeks ago   516MB
docker/getting-started   latest    eb9194091564   3 weeks ago   28.5MB
```

**NOTE:**  
Outra alternativa seria você utilizar o comando **docker images** para lista todas as imagens que seu *Docker host* tem localmente:

```
docker images
```

**OUTPUT:**  
```
REPOSITORY               TAG       IMAGE ID       CREATED       SIZE
minio/minio              latest    01431999f934   10 days ago   393MB
mysql                    latest    b05128b000dd   2 weeks ago   516MB
docker/getting-started   latest    eb9194091564   3 weeks ago   28.5MB
```

---

**REFERENCES:**  
[Comandos básicos](https://stack.desenvolvedor.expert/appendix/docker/comandos.html)
