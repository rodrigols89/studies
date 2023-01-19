# Logs

## Contents

 - [Visualizando o histórico de commits](#history)

---

<div id="history"></div>

## Visualizando o histórico de commits

Depois que você tiver criado vários commits, ou se clonou um repositório com um histórico de commits existente, você provavelmente vai querer ver o que aconteceu. O comando mais básico e poderoso para fazer isso é o **git log**:

```
git clone git://github.com/schacon/simplegit-progit.git
```

Quando você executar **git log** neste projeto, você deve ter uma saída como esta:

```python
$ git log
commit ca82a6dff817ec66f44342007202690a93763949
Author: drigols <drigols.creative@gmail.com>
Date:   Mon Mar 17 21:52:11 2008 -0700

    changed the verison number

commit 085bb3bcb608e1e8451d4b2432f8ecbe6306e7e7
Author: drigols <drigols.creative@gmail.com>
Date:   Sat Mar 15 16:40:33 2008 -0700

    removed unnecessary test code

commit a11bef06a3f659402fe7563abf99ad00de2209e6
Author: drigols <drigols.creative@gmail.com>
Date:   Sat Mar 15 10:31:28 2008 -0700

    first commit
```

**NOTE:**  
Por padrão, sem argumentos, **git log** lista os commits feitos naquele repositório em ordem cronológica reversa. Isto é, os commits mais recentes primeiro. Como você pode ver, este comando lista:  

 - Cada commit;
 - Seu checksum SHA-1;
 - O nome e e-mail do autor;
 - A data;
 - A mensagem do commit.

---

**REFERENCES:**  
https://git-scm.com/book/pt-br/v1/  
https://git-scm.com/book/en/v2/  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
