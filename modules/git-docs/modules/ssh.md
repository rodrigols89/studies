### SSH  
  
__Generating Your SSH Public Key__  
  
As chaves SSH ficam armazenadas em um diretório oculto chamado <strong>.ssh</strong>. Para saber quais as chaves SSH existem no seu computador basta digitar o seguinte no terminal:  
  
```  
ls ~/.ssh  
```  
  
Se nenhum arquivo for listado isso significa que não existe nenhuma chave SSH na sua máquina. Mas para resolver isso é bem simples, basta digitar o comando <strong>ssh-keygen -C "comentário..."</strong>:  
  
```  
ssh-keygen -C "comentário..."  
```  
  
É interessante que esse comentário seja algo que lhe ajuda a lembrar sobre o motivo desta chave. Continuando, depois que você pede para gerar a chave você vai ter uma mensagem parecida com a seguinte:  
  
```
Generating public/private rsa key pair.
Enter file in which to save the key (/home/drigols/.ssh/id_rsa):  
```  
  
Está pedindo para você digitar o arquivo no qual vocÊ deseja salva a chave. Basta você aperta enter para essa chave ser salva no arquivo padrão <strong>id_rsa.pub</strong>. Agora ele vai pedir para você digitar sua senha para a chave privada SSH, por favor, coloque uma senha que você não esqueça, porque não tem como altera essa senha novamente.  
  
Agora se você novamente lista os arquivos do diretório oculto SSH( ls ~/.ssh ) terá o seguinte resultado:  
  
```  
drigols@Debian-drigols:~$ ls ~/.ssh
id_rsa  id_rsa.pub  
```  
  
<strong>Arquivo "id_rsa":</strong>  
Este arquivo é responsável pelo armazenamento da nossa <strong>chave privada</strong>.  
  
<strong>Arquivo "id_rsa.pub":</strong>  
Este arquivo é responsável pelo armazenamento da nossa <strong>chave pública</strong>.  
  
Por exemplo, se quisermos trabalhar em conjunto com o GitHub, basta adicionar nossa <strong>chave pública(id_rsa.pub)</strong> nas configurações do GitHub. Lembre que <strong>id_rsa.pub</strong> é apenas um arquivo, a chave pública está armazenada dentro do mesmo, para ver a chave basta digitar:  
  
```  
drigols@Debian-drigols:~$ cat ~/.ssh/id_rsa.pub  
```  
  
E agora como eu posso testar se está tudo ok entre a comunicação entre minha máquina e o servidor do GitHub. Basta digitar <strong>ssh -T git@github.com</strong>:  
  
```  
drigols@Debian-drigols:~$ ssh -T git@github.com  
```  
  
Agora se a gente digitar o seguinte comando do Git, <strong>git remote -v</strong>, se ele não retornar nada que dizer que nõs não estamos em nenhum remoto do Git.  
  
Agora o que precisamos fazer é simplesmente adicionar um remoto na nossa máquina para trabalhar nele:  
  
```  
root@Debian-drigols:/home/drigols/workspace# git remote add test git@github.com:drigols/test.git  
```  
  
Agora basta rodar novamente o comando <strong>git remote -v</strong> para ver o resultado do nosso remoto:  
  
```  
root@Debian-drigols:/home/drigols/workspace# git remote -v  
test	git@github.com:drigols/test.git (fetch)  
test	git@github.com:drigols/test.git (push)  
```  
  
Agora é só trabalhar com os comandos <strong>git pull</strong> e <strong>git push</strong> para enviar e receber arquivos do proejto.  
  
__Note__  
  
Veja que quando nós criamos o remote a palavra <strong>test</strong> foi apenas um "apelido" parao remoto. Se você por exemplo clonar um repositório por padrão o remoto vai se chamar <strong>origin</strong>.  

---

**REFERENCES:**  
https://git-scm.com/book/pt-br/v1/  
https://git-scm.com/book/en/v2/  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
