# Docker Container

## Contents

 - [01 - Parâmetros de inicialização de um Container](#01)

---

<div id="01"></div>

## 01 - Parâmetros de inicialização de um Container

Supondo que você já tem uma *Docker Imagem* baixada agora chegou a hora de você inicializar um container a partir desta *Imagem*.

Mas antes disso vamos ver quais parâmetros nós podemos adicionar na hora da criação de um container e para que serve cada um:

| Parâmetro |                          Explicação                                       |
|-----------|---------------------------------------------------------------------------|
|    -d     | Executa o container em background                                         |
|    -i     | Modo interativo. Mantém o STDIN aberto mesmo sem console anexado          |
|    -t     | Aloca uma pseudo TTY                                                      |
|   --rm    | Automaticamente remove o container após finalização (Não funciona com -d) |
|   --name  | Nomea o container                                                         |
|    -v     |	Mapea (mapeamento) de volume                                              |
|    -p     | Mapea (mapeamento) de porta                                               |
|    -m     | Limita o uso de memória RAM                                               |
|    -c     | Balancea o uso de CPU                                                     |


Segue um exemplo simples de como aplicar isso na prática com o comando abaixo:

```
docker container run -it --rm --name my_python python bash
```

De acordo com o comando acima, será iniciado um container com o nome **my_python**, criado a partir da imagem *python* e o processo executado nesse container será o *bash*.

**NOTE:**  
Vale lembrar que, caso o *CMD* não seja especificado no comando **docker container run**, é utilizado o valor padrão definido no Dockerfile da imagem utilizada. No nosso caso é python e seu comando padrão executa o binário python, ou seja, se não fosse especificado o bash, no final do comando de exemplo acima, ao invés de um shell bash do GNU/Linux, seria exibido um shell do python.

---

**REFERENCES:**  
[Comandos básicos](https://stack.desenvolvedor.expert/appendix/docker/comandos.html)
