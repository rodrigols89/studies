# Git - Guide  
  
# Topics  
  
__01 - Getting Started__  
[1.0 - Introduction](#introduction)  
[1.1 - States](#states)  
[1.2 - Initial setting](#setting)  
  
__02 - Git Basic__  
[2.0 - Commit StyleGuide](#commit)  
[2.1 - Git log](#log)  
[2.2 - Working with Remotes](#remotes)  
  
__03 - Git Branching__  
[3.0 - Branching](#branching)  
[3.1 - Merging](#merging)  
[3.2 - Branch Management](#management)  
[3.3 - Branching Workflows](#workflows)   
[3.4 - Remote Branches + git fetch](#rb)  
[3.5 - Rebasing](#rebasing)  
  
__04 - Git Tools__  
[4.0 - Revision Selection(git show)](#revision)  
[4.1 - Interactive Staging](#interactive)  
[4.2 - Stash](#stash)  
  
__05 - Git Internals__  
[Plumbing and Porcelain](#pp)  
  
__06 Generating Your SSH Public Key__  
[Generating Your SSH Public Key](#ssh)


__Reference__  
[Reference](#reference)  
  
  
### Introduction  
  
__Comandos e conceitos básicos__  
  
* **clone:** Este comando serve para <strong>criar um repositório na sua máquina local</strong> mesmo que seja uma cópia de um repositório em um servidor, no caso o github. Em outras palavras, o comando **clone** faz download do código que está no servidor, <strong>mas ao mesmo tempo cria um repositório na sua máquina local</strong>.  
  
  
* **branch:** Uma é um ramo do projeto, uma divisão do projeto se baseando na principal porém que esteja seguindo linhas de pensamento diferentes Ex:  
  - Correção de bugs de uma versão que está online estaria em uma Branch.  
  - A atualização ou criação de um outro layout estaria em outra Branch.  
  - A criação de alguma nova funcionalidade poderia estar em outra Branch diferente das anteriores.  
  
  
* **checkout:** Este comando serve para você escolher em qual **branch** você está agindo agora. Ou seja, você configura qual a **branch vigente** no **repositório local**.  
  
  
* **add:** Este comando adiciona um arquivo ou diretório no **repositório local**, na **branch vigente** do mesmo, é como você dissesse pro repositório:  
  
```  
"Hey repositório, eu tenho um arquivo/diretório novo aqui e quero que você  
guarde ele para mim, segura ele, mas não guarda ainda não tá?".  
```  
  
Repare que o repositório não terá ainda teu arquivo, ele apenas saberá que ele existe.  
  
    - adiciona um arquivo/diretório no repositório local;  
    - Na branch vigente;  
    - Segura um arquivo/diretório mas não guarda no repositório ainda.  
  
  
* **commit:** Agora sim, você está entregando o arquivo/diretório para que o repositório guarde-o. Mas novamente, vale notar que este arquivo só está **versionado** (guardado), no **repositório local**, na **branch vigente**.  
  - No **repositório local**  
  - Na **branch vigente**  
  
  
* **pull:** Este comando baixa os documentos mais atuais do servidor(ex: GitHub), para o **repositório local** e **branch vigente**.  
  
  
* **push:** E agora, não menos importante, o grande comando **push**. Este comando é semelhante ao comando **commit**, mas agora ele envia tudo que está no seu **repositório local** e **branch vigente** para o repositório do servidor(Ex: github). Ou seja, só após você executar este comando é que as pessoas do projeto conseguirá ver o que você fez até então!  
  - Primeiro, o comando **add** pede para guardar um arquivo/diretório;  
  - Segundo, o comando **commit -m "msg"** guarda o/os arquivo/diretório no **repositório local** e **branch vigente**;  
  - Terceiro, o comando **push** envia tudo que está no seu **repositório local** e **branch vigente** para o repositório do servidor(Ex: github).  
  
  
E esses são os principais comandos e conceitos do GIT. Agora que sabemos o que cada um significa, temos que ver como que eles funcionam na prática, certo?  
  
<strong>Fluxos de trabalho Centralizado</strong>  
  
O fluxo de trabalho centralizado é o mais familiar para aqueles que vieram de outras ferramentas de versionamento mais antigas, como o CVS ou SVN. Nele você tem apenas um único servidor, e diversas pessoas trabalhando em seus repositórios locais e enfim subindo os documentos para o repositório principal(servidor).  
  
Explicando detalhadamente desde o inicio da vida de um repositório com **Fluxo de trabalho centralizado**, ele funcionaria desta forma:  

<table>
  <tr>
    <td>
      <strong>Step:01</strong>
    </td>
    <td>
      É criado um repositório novo no servidor para o projeto <strong>X</strong>.
    </td>
  </tr>
  <tr>
    <td>
      <strong>Step:02</strong>
    </td>
    <td>
      Cada membro da equipe <strong>clona</strong> o repositório em sua máquina local.
    </td>
  </tr>
  <tr>
    <td>
      <strong>Step:03</strong>
    </td>
    <td>
      Para cada <strong>tarefa</strong> ou <strong>subtarefa</strong> que for feita, cada membro da equipe cria uma nova <strong>branch</strong> em seu repositório local e logo em seguida efetua um <strong>checkout</strong> para a nova branch criada.
    </td>
  </tr>  
  <tr>
    <td>
      <strong>Step:04</strong>
    </td>
    <td>
      Então cada um segue com sua atividade e a medida que desejar, a pessoa <strong>adiciona(add)</strong> e realiza <strong>commit</strong> de suas alterações, para que o repositório local guarde o histórico do que foi feito. Este passo é executado até que a tarefa ou subtarefa esteja concluida.
    </td>
  </tr>
  <tr>
    <td>
      <strong>Step:05</strong>
    </td>
    <td>
      Após a tarefa estar concluido e feito o <strong>commit</strong> no repositório local, o membro da equipe faz <strong>checkout</strong> para a branch principal, no caso, a </strong>branch master</strong> e realiza o comando <strong>pull</strong> para atualizar seu repositório local com os documentos mais novos feitos pela equipe.
    </td>
  </tr>
  <tr>
    <td>
      <strong>Step:06</strong>
    </td>
    <td>
      Feito o <strong>pull</strong>, deve-se então realizar o <strong>merge</strong> da branch criada no <strong>3º passo</strong> com a branch <strong>master</strong>, juntando assim os documentos em seu repositório local.
    </td>
  </tr>
  <tr>
    <td>
      <strong>Step:07</strong>
    </td>
    <td>
      Por fim, é realizado o comando <strong>push</strong> para que suas alterações sejam enviadas ao repositório central(servidor).
    </td>
  </tr>
  <tr>
    <td>
      <strong>Step:08</strong>
    </td>
    <td>
      Após feito o <strong>push</strong>, a pessoa pode apagar a branch criada (se desejar) e então deve escolher uma nova <strong>tarefa</strong> ou <strong>subtarefa</strong> e voltar ao <strong>3º passo</strong>. E isso continua até que o projeto esteja concluído.
    </td>
  </tr>  
</table>  
  
Este fluxo se chama **Fluxo de Trabalho Centralizado**, pois temos um único repositório servidor servindo como centralizador do código entre as equipes de desenvolvimento. É um fluxo bastante utilizado em mundo corporativo onde temos uma equipe pequena trabalhando. Porém mostra-se inviável em grandes projetos Open-Source, como por exemplo o projeto do kernel do GNU Linux.  
  
### States  
  
Agora preste atenção. Essa é a coisa mais importante pra se lembrar sobre <strong>Git</strong> se você quiser que o resto do seu aprendizado seja tranquilo. Git faz com que seus arquivos sempre estejam em um dos três estados fundamentais:  
  
 - consolidado <strong>(committed)</strong>;  
 - modificado <strong>(modified)</strong>;  
 - preparado <strong>(staged)</strong>.  
  
<strong>Consolidado(comitted):</strong>  
Dados são ditos consolidados quando estão seguramente armazenados em sua base de dados local.  
  
<strong>Modificado(modified):</strong>  
Modificado trata de um arquivo que sofreu mudanças mas que ainda não foi consolidado na base de dados.  
  
<strong>preparado(staged):</strong>  
Um arquivo é tido como preparado quando você marca um arquivo modificado em sua versão corrente para que ele faça parte do snapshot do próximo commit (consolidação).  
  
Isso nos traz para as três seções principais de um projeto do Git:  
  
 - O diretório do Git <strong>(git directory, repository)</strong>  
 - O diretório de trabalho <strong>(working directory)</strong>  
 - A área de preparação <strong>(staging area)</strong>  
  
![Git - Guide](res/picture01.png)  
  
<strong>git directory(repository):</strong>  
É o diretório do Git <strong>local</strong> onde o Git armazena os metadados e o banco de objetos de seu projeto. Esta é a parte mais importante do Git, e é a parte copiada quando você clona um repositório de outro computador.
  
<strong>Working Directory:</strong>  
O diretório de trabalho é um único checkout de uma versão do projeto. Estes arquivos são obtidos a partir da base de dados comprimida no diretório do Git e colocados em disco para que você possa utilizar ou modificar.  
  
<strong>Staging Area:</strong>  
A área de preparação é um simples arquivo, geralmente contido no seu diretório Git, que armazena informações sobre o que irá em seu próximo commit. É bastante conhecido como índice (index), mas está se tornando padrão chamá-lo de área de preparação(Staging Area).  
  
### Setting  
  
<strong>Sua Identidade</strong>  
  
A primeira coisa que você deve fazer quando instalar o Git é definir o seu <strong>nome de usuário</strong> e <strong>endereço de e-mail</strong>. Isso é importante porque todos os commits no Git utilizam essas informações, e está imutavelmente anexado nos commits que você realiza:  
  
```  
$ git config --global user.name "drigols"  
$ git config --global user.email drigols.creative@gmail.com  
```  
  
Relembrando, você só precisará fazer isso uma vez caso passe a opção <strong>--global</strong>, pois o Git sempre usará essa informação para qualquer coisa que você faça nesse sistema. Caso você queira sobrepor estas com um nome ou endereço de e-mail diferentes para projetos específicos, você pode executar o comando <strong>sem a opção --global</strong> quando estiver no próprio projeto.  
  
<strong>Verificando Suas Configurações</strong>  
  
Caso você queira verificar suas configurações, você pode utilizar o comando <strong>git config --list</strong> para listar todas as configurações que o Git encontrar naquele momento:  
  
```  
user.name=drigols  
user.email=drigols.creative@gmail.com  
core.editor=emacs  
core.repositoryformatversion=0  
core.filemode=true  
core.bare=false  
core.logallrefupdates=true  
```  
  
Você também pode verificar qual o valor que uma determinada chave tem para o Git digitando <strong>git config {key}</strong>:  
  
```  
$ git config user.name  
drigols  
```  
  
### Commit  
  
Uma coisa muito importante que a maioria dos desenvolvedores esquecem é a parte dos <strong>emoji</strong>. Isso deixa o seu commit bem mais legível visto que de cara já da para notar o que aconteceu com aquele commit.  
  
<strong>Examples:</strong>  
  
Emoji | Code | Commit Type
------------ | ------------- | -------------
:tada: | `:tada:` | initial commit
:art: | `:art:` | quando melhorar a estrutura/formato do código
:racehorse: | `:racehorse:` | quando melhorar a performance
:memo: | `:memo:` | quando escrever alguma documentação
:bug: | `:bug:` | quando corrigir um bug
:fire: | `:fire:` | quando remover códigos ou arquivos
:green_heart: | `:green_heart:` | quando corrigir uma build no CI
:white_check_mark: | `:white_check_mark:` | quando adicionar testes
:lock: | `:lock:` | quando melhorar a segurança
:arrow_up: | `:arrow_up:` | quando der upgrade em dependências
:arrow_down: | `:arrow_down:` | quando der downgrade em dependências
:poop: | `:poop:` | deprecated
:construction: | `:construction:` | em construção
:rocket: | `:rocket:` | nova feature
:see_no_evil: | `:see_no_evil:` | gambiarra
:gift: | `:gift:` | nova versão
  
# Três coisas importantes em um commit  
  
 - Tag(quando necessário);  
 - Linha de resumo(máximo de 72 caracteres);  
 - Descrição do commit.  
  
__TAGS PERMITIDAS__  
  
* [tag] : Criação de uma tag.  
* [-tag] : Remoção de uma tag.  
* [branch] : Criação de um branch.  
* [-branch] : Remoção de um branch.  
* [merge] : Junção de códigos, ponto crítico.  
  
__Linha de Resumo__  
  
A primeira linha do commit deve ser um resumo do commit e tem 2 pontos importantes:  
  
 - Deve ter no máximo 72 caracteres;  
 - Não termina a linha de resumo com pontuação.  
  
Escreva a linha de resumo e a descrição de modo <strong>imperativo</strong>, como se estivesse comandando alguém. Exemplo:  
  
 - Adiciona  
 - Remove  
 - Atualiza  
  
O contrário seria: "adicionado", "removido", "atualizado"(Não faça isso).  
  
<strong>Exemplo:</strong>  
  
```bash
git commit -m ":tada: Initial commit  
>  
> Esse é meu primeiro commit...  
> ...essa nova linha é para não deixar o seu commit muito longo na horizontal."  
```   
  
<strong>Output:</strong>  
  
```  
[master dde03e0] :tada: Initial commit  
 1 file changed, 0 insertions(+), 0 deletions(-)  
 create mode 100644 index.html  
```  
  
Agora você acabou de criar o seu primeiro commit! Você pode ver que o commit te mostrou uma saída sobre ele mesmo:  
  
 - Qual o branch que recebeu o commit <strong>(master)</strong>;  
 - Qual o checksum SHA-1 que o commit teve <strong>(dde03e0)</strong>;  
 - Quantos arquivos foram alterados <strong>(1 file changed, 0 insertions(+), 0 deletions(-))</strong>;  
 - Estatísticas a respeito das linhas adicionadas e removidas no commit.  
  
<strong>Modificando Seu Último Commit</strong>  
  
Uma das situações mais comuns para desfazer algo, acontece quando você faz o commit muito cedo e possivelmente esqueceu de adicionar alguns arquivos, ou você bagunçou sua mensagem de commit. Se você quiser tentar fazer novamente esse commit, você pode executá-lo com a opção <strong>--amend</strong>:  
  
```  
$ git commit --amend  
```  
  
Esse comando pega sua área de seleção e a utiliza no commit. Se você não fez nenhuma modificação desde seu último commit (por exemplo, você rodou esse comando imediatamente após seu commit anterior), seu snapshot será exatamente o mesmo e tudo que você mudou foi sua mensagem de commit.  
  
### Log  
  
<strong>Visualizando o Histórico de Commits</strong>  
  
Depois que você tiver criado vários commits, ou se clonou um repositório com um histórico de commits existente, você provavelmente vai querer ver o que aconteceu. A ferramente mais básica e poderosa para fazer isso é o comando <strong>git log</strong>.  
  
<strong>Exemplo:</strong>  
  
```  
git clone git://github.com/schacon/simplegit-progit.git  
```  
  
Quando você executar git log neste projeto, você deve ter uma saída como esta:  
  
```  
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
  
Por padrão, sem argumentos, <strong>git log</strong> lista os commits feitos naquele repositório em ordem cronológica reversa. Isto é, os commits mais recentes primeiro. Como você pode ver, este comando lista:  
  
 - Cada commit;  
 - Seu checksum SHA-1;  
 - O nome e e-mail do autor;  
 - A data;  
 - A mensagem do commit.  
  
### Remotes  
  
<strong>Exibindo Seus Remotos</strong>  
  
Para ver quais servidores remotos você configurou, você pode executar o comando <strong>git remote</strong>. Ele lista o nome de cada remoto que você especificou. Se você tiver clonado seu repositório, você deve pelo menos ver um chamado <strong>origin</strong> — esse é o nome padrão que o Git dá ao servidor de onde você fez o clone.  
  
```  
$ cd test  
$ git remote  
origin  
```  
  
Você também pode especificar <strong>-v</strong>, que mostra a URL que o Git armazenou para o nome do remoto:  
  
```  
$ git remote -v
origin  git://github.com/schacon/ticgit.git (fetch)  
origin  git://github.com/schacon/ticgit.git (push)  
```  
Se você tem mais de um remoto, o comando lista todos. Por exemplo, meu repositório Grit se parece com isso.  
  
```  
$ cd grit  
$ git remote -v  
bakkdoor  git://github.com/bakkdoor/grit.git  
cho45     git://github.com/cho45/grit.git  
defunkt   git://github.com/defunkt/grit.git  
koke      git://github.com/koke/grit.git  
origin    git@github.com:mojombo/grit.git  
```  
  
Isso significa que podemos puxar contribuições de qualquer um desses usuários muito facilmente. Mas note que somente o <strong>remoto origin</strong> é uma URL SSH, sendo o único pra onde eu posso fazer o push.  
  
__Adicionando Repositórios Remotos__  
  
Para adicionar um novo repositório remoto no Git com um nome curto, para que você possa fazer referência facilmente, execute <strong>git remote add [nomecurto] [url]</strong>:  
  
```  
$ git remote
origin
$ git remote add pb git://github.com/paulboone/ticgit.git
$ git remote -v
origin    git://github.com/schacon/ticgit.git
pb    git://github.com/paulboone/ticgit.git
```  
  
Agora você pode usar a string <strong>pb</strong> na linha de comando em lugar da URL completa. Por exemplo, se você quer fazer o fetch de todos os dados de Paul que você ainda não tem no seu repositório, você pode executar <strong>git fetch pb</strong>:  
  
```  
$ git fetch pb
remote: Counting objects: 58, done.
remote: Compressing objects: 100% (41/41), done.
remote: Total 44 (delta 24), reused 1 (delta 0)
Unpacking objects: 100% (44/44), done.
From git://github.com/paulboone/ticgit
 * [new branch]      master     -> pb/master
 * [new branch]      ticgit     -> pb/ticgit
 ```  
  
O branch master de Paul é localmente acessível como pb/master — você pode fazer o merge dele em um de seus branches, ou fazer o check out de um branch local a partir deste ponto se você quiser inspecioná-lo.  
  
__Fazendo o Fetch e Pull de Seus Remotos__  
  
Como você acabou de ver, para pegar dados dos seus projetos remotos, você pode executar:  
  
```  
$ git fetch [nome-remoto]  
```  
  
Esse comando <strong>vai até o projeto remoto e pega todos os dados que você ainda não tem</strong>. Depois de fazer isso, você deve ter referências para todos os branches desse remoto, onde você pode fazer o <strong>merge</strong> ou <strong>inspecionar</strong> a qualquer momento.  
  
Se você clonar um repositório, o comando automaticamente adiciona o remoto com o nome origin. Então, <strong>git fetch origin</strong> busca qualquer novo trabalho que foi enviado para esse servidor desde que você o clonou (ou fez a última busca).  
  
<strong>OBSERVAÇÃO:</strong>  
É importante notar que o comando <strong>fetch</strong> traz os dados para o seu <strong>repositório local</strong> — ele não faz o merge automaticamente com o seus dados ou modifica o que você está trabalhando atualmente. Você terá que fazer o merge manualmente no seu trabalho quando estiver pronto.  
  
__git pull__  
  
Se você tem um branch configurado para acompanhar um branch remoto, você pode usar o comando <strong>git pull</strong> para automaticamente fazer o <strong>fetch</strong> e o <strong>merge</strong> de um branch remoto no seu <strong>branch atual</strong>.  
  
Executar <strong>git pull</strong> geralmente busca os dados do servidor de onde você fez o clone originalmente e automaticamente tenta fazer o merge dele no código que você está trabalhando atualmente.  
  
<strong>Pushing para seus remotos</strong>  
  
Quando o seu projeto estiver pronto para ser compartilhado, você tem que enviá-lo para a fonte. O comando para isso é simples:  
  
```  
git push [nome-remoto] [branch]  
```  
  
Se você quer enviar o seu branch master para o servidor origin, então você pode rodar o comando abaixo para enviar o seu trabalho para o sevidor:  
  
```  
$ git push origin master  
```  
  
Este comando funciona apenas se você clonou de um servidor que você têm permissão para escrita, e se mais ninguém enviou dados no meio tempo. Se você e mais alguém clonarem ao mesmo tempo, e você enviar suas modificações após a pessoa ter enviado as dela, o seu push será rejeitado. Antes, você terá que fazer um pull das modificações deste outro alguém, e incorporá-las às suas para que você tenha permissão para enviá-las.  
  
__Removendo e renomeando remotos__  
  
Se você quiser renomear uma referência, em versões novas do Git você pode rodar <strong>git remote rename</strong> para modificar um apelido de um remoto. Por exemplo, se você quiser renomear pb para paul, você pode com <strong>git remote rename</strong>:  
  
```  
$ git remote rename pb paul
$ git remote
origin
paul
```  
  
É válido mencionar que isso modifica também os nomes dos branches no servidor remoto. O que costumava ser referenciado como <strong>pb/master</strong> agora é <strong>paul/master</strong>.  
  
Se você quiser remover uma referência por qualquer razão — você moveu o servidor ou não está mais usando um mirror específico, ou talvez um contribuidor não está mais contribuindo — você usa <strong>git remote rm</strong>:  
  
```  
$ git remote rm paul
$ git remote
origin  
```  
  
### Branching  
  
Quando você faz um commit no Git, o Git guarda um objeto commit que contém:  
  
 - Um ponteiro para o snapshot do conteúdo que você colocou na área de seleção;  
 - O autor;  
 - Os metadados da mensagem;  
 - Zero ou mais ponteiros para o commit ou commits que são pais deste commit.  
  
Para visualizar isso, vamos supor que você tenha um diretório contendo três arquivos, e colocou todos eles na área de seleção e fez o commit. Colocar na área de seleção cria o <strong>checksum</strong> de cada arquivo, armazena esta versão do arquivo no repositório Git (o Git se refere a eles como blobs), e acrescenta este checksum à área de seleção:  
  
```  
$ git add README test.rb LICENSE  
$ git commit -m 'commit inicial do meu projeto'  
```  
  
Quando você cria um commit executando <strong>git commit</strong>, o Git calcula o checksum de cada subdiretório e armazena os objetos de árvore no repositório Git. O Git em seguida, <strong>cria um objeto commit</strong> que tem os metadados e <strong>um ponteiro para a árvore do projeto raiz</strong>, então ele pode recriar este snapshot quando necessário.  
  
Seu repositório Git agora contém cinco objetos:  
  
 - 1º Um blob para o conteúdo de cada um dos três arquivos;  
 - 2º Uma árvore que lista o conteúdo do diretório e especifica quais nomes de arquivos são armazenados em quais blobs;  
 - 3º Um commit com o ponteiro para a raiz dessa árvore com todos os metadados do commit.  
  
Conceitualmente, os dados em seu repositório Git se parecem como na figura abaixo:  
  
![Git - Guide](res/picture02.png)  
<strong>Dados de um repositório com um único commit.</strong>  
  
Se você modificar algumas coisas e fizer um commit novamente, o próximo commit armazenará um ponteiro para o commit imediatamente anterior. Depois de mais dois commits, seu histórico poderia ser algo como a figura abaixo:  
  
![Git - Guide](res/picture03.png)  
  
__Branching__  
  
Um <strong>branch</strong> no Git é simplesmente um leve ponteiro móvel para um desses commits. O nome do branch padrão no Git é master. Como você inicialmente fez commits, você tem um branch principal (master branch) que aponta para o último commit que você fez. Cada vez que você faz um commit ele avança automaticamente.  
  
![Git - Guide](res/picture04.png)  
<strong>Branch apontando para o histórico de commits.</strong>  
  
__NOTE__  
  
Lembram que quando utilizamos o comando <strong>git log</strong> ele retorna a lista de commits da branch vigente? Lembram que ele retorna os commits da ordem mais recente, ou seja, do mais recente até os mais antigos. Então, a imagem acima demonstrar isso na prática onde a <strong>master</strong> está apontando para o último commit(mais recente).  
  
__Nova Branching__  
  
O que acontece se você criar um novo branch? Bem, isso cria um novo ponteiro para que você possa se mover. Vamos dizer que você crie um novo branch chamado <strong>testing</strong>. Você faz isso com o comando <strong>git branch</strong>:  
  
```  
$ git branch testing  
```  
  
Isso cria um novo ponteiro para o mesmo commit em que você está no momento, veja na figura abaixo:  
  
![Git - Guide](res/picture05.png)  
  
Como o Git sabe o branch em que você está atualmente? Ou seja, como ele sabe se eu estou na branch <strong>master</strong> ou <strong>testing</strong>? Ele mantém um ponteiro especial chamado <strong>HEAD</strong>.  
  
![Git Guide](res/picture06.png)  
<strong>HEAD apontando para o branch em que você está.</strong>  
  
No Git, este é um ponteiro para o <strong>branch local</strong> em que você está no momento. Neste caso, você ainda está no master. O comando git branch só criou um novo branch — ele não mudou para esse branch.  
  
__Mudando de Branching__  
  
Para mudar para um branch existente, você executa o comando <strong>git checkout</strong>. Vamos mudar para o novo branch <strong>testing</strong>:  
  
```  
$ git checkout testing  
```  
  
Isto move o <strong>HEAD</strong> para apontar para o branch testing, veja a figura abaixo:  
  
![Git - Guide](res/picture07.png)  
<strong>O HEAD aponta para outro branch quando você troca de branches.</strong>  
  
Qual é o significado disso? Bem, vamos fazer um outro commit:  
  
```  
$ touch test-02.rb  
$ git commit -a -m 'fiz uma alteração'  
```  
  
A figura abaixo ilustra o nosso resultado:  
  
![Git - Guide](res/picture08.png)  
<strong>O branch para o qual HEAD aponta avança com cada commit(Lembra que uma branch no Git é simplesmente um leve ponteiro móvel para um desses commits, então, o que acontece é que a cada commit essa branching vai avançando.).</strong>  
  
Isso é interessante, porque agora o seu branch testing avançou, mas o seu branch master ainda aponta para o commit em que estava quando você executou <strong>git checkout</strong> para trocar de branch. Vamos voltar para o branch master:  
  
```  
$ git checkout master  
```  
  
Veja a figura abaixo o resultado:  
  
![Git - Guide](res/picture09.png)  
<strong>O HEAD se move para outro branch com um checkout.</strong>  
  
Esse comando fez duas coisas:  
  
 - Ele alterou o ponteiro HEAD para apontar novamente para o branch master;  
 - E reverteu os arquivos em seu diretório de trabalho para o estado em que estavam no snapshot para o qual o master apontava.  
  
Isto significa também que as mudanças feitas a partir deste ponto em diante, irão divergir de uma versão anterior do projeto. Ele essencialmente "volta" o trabalho que você fez no seu <strong>branch testing</strong>, temporariamente, de modo que você possa ir em uma direção diferente.  
  
Vamos fazer algumas mudanças e fazer o commit novamente:  
  
```  
$ vim test.rb  
$ git commit -a -m 'fiz outra alteração'  
```  
  
Agora o histórico do seu projeto divergiu. Você criou e trocou para um branch, trabalhou nele, e então voltou para o seu branch principal(master) e trabalhou mais. Ambas as mudanças são isoladas em branches distintos: você pode alternar entre os branches e fundi-los (merge) quando estiver pronto. E você fez tudo isso simplesmente com os comandos <strong>branch</strong> e <strong>checkout</strong>.  
  
Veja na figura abaixo como fica essas divergências(fluxos diferentes de trabalho):  
  
![Git - Guide](res/picture10.png)  
<strong>O histórico dos branches diverge.</strong>  
  
__NOTE__  
Um branch em Git é na verdade um arquivo simples que contém os 40 caracteres do checksum SHA-1 do commit para o qual ele aponta, os branches são baratos para criar e destruir. Criar um novo branch é tão rápido e simples como escrever 41 bytes em um arquivo (40 caracteres e uma quebra de linha).  
  
  
### Merging  
  
Vamos ver um exemplo simples de uso de <strong>branch</strong> e <strong>merge</strong> com um fluxo de trabalho que você pode usar no mundo real. Você seguirá esses passos:  
  
1. Trabalhar em um web site.  
2. Criar um branch para uma nova história em que está trabalhando.  
3. Trabalhar nesse branch.  
  
Nesse etapa, você receberá um telefonema informando que outro problema crítico existe e precisa de correção. Você fará o seguinte:  
  
1. Voltar ao seu branch de produção.  
2. Criar um branch para adicionar a correção.  
3. Depois de testado, fazer o merge do branch da correção, e enviar para produção.  
4. Retornar à sua história anterior e continuar trabalhando.  
  
__Branch Básico__  
  
Primeiro, digamos que você esteja trabalhando no seu projeto e já tem alguns commits. Veja na figura abaixo:  
  
![Git - Guide](res/picture11.png)  
<strong>Um histórico de commits pequeno e simples(Lembre que esses commit apontam em sequência do mais recente para o mais antigo).</strong>  
  
Você decidiu que irá trabalhar na tarefa <strong>(issue) #53</strong> do gerenciador de bugs ou tarefas que sua empresa usa. Para deixar claro, Git não é amarrado a nenhum gerenciador de tarefas em particular; mas já que a tarefa <strong>#53</strong> tem um foco diferente, você criará um branch novo para trabalhar nele.  
  
Para criar um branch e mudar para ele ao mesmo tempo, você pode executar o comando <strong>git checkout</strong> com a opção <strong>-b</strong>:  
  
```  
$ git checkout -b iss53  
Switched to a new branch "iss53"  
```  
  
Isso é um atalho para:  
  
```  
$ git branch iss53  
$ git checkout iss53  
```  
  
Veja a figura abaixo para ficar melhor com uma ilustração do fluxo:  
  
![Git - Guide](res/picture12.png)  
  
Você trabalha no seu web site e faz alguns commits:  
  
```  
$ touch index.html  
$ git commit -a -m 'adicionei um novo rodapé [issue 53]'  
```  
  
Ao fazer isso o branch <strong>iss53</strong> avançará, pois você fez o checkout dele (isto é, seu HEAD está apontando para ele), veja na figura abaixo:  
  
![Git - Guide](res/picture13.png)  
  
Nesse momento você recebe uma ligação dizendo que existe um problema com o web site e você deve resolvê-lo imediatamente. Com Git, você não precisa fazer o deploy de sua correção junto com as modificações que você fez no <strong>iss53</strong>, e você não precisa se esforçar muito para reverter essas modificações antes que você possa aplicar sua correção em produção. Tudo que você tem a fazer é voltar ao seu <strong>branch master</strong>.  
  
No entanto, antes de fazer isso, note que seu <strong>diretório de trabalho(Working Directory)</strong> ou <strong>área de seleção</strong> tem modificações que não entraram em commits e que estão gerando conflitos com o branch que você está fazendo o checkout, Git não deixará você mudar de branch.  
  
Existem maneiras de contornar esta situação (isto é, incluir e fazer o commit). Por enquanto, você fez o commit de todas as suas modificações, então você pode mudar para o seu branch master:  
  
```  
$ git checkout master  
Switched to branch "master"  
```  
  
Nesse ponto, o diretório do seu projeto está exatamente do jeito que estava antes de você começar a trabalhar na tarefa #53, e você se concentra na correção do erro.  
  
Em seguida, você tem uma correção para fazer. Vamos criar um branch para a correção <strong>(hotfix)</strong> para trabalhar até a conclusão:  
  
```  
$ git checkout -b 'hotfix'
Switched to a new branch "hotfix"
$ touch index.html
$ git commit -a -m 'consertei o endereço de email'
[hotfix]: created 3a0874c: "consertei o endereço de email"
 1 files changed, 0 insertions(+), 1 deletions(-)
```  
  
Veja o resultado na figura abaixo:  
  
![Git - Guide](res/picture14.png)  
<strong>branch de correção (hotfix) baseado num ponto de seu branch master.</strong>  
  
Você pode rodar seus testes, tenha certeza que a correção é o que você quer, e faça o merge no seu branch master para fazer o deploy em produção. Você faz isso com o comando <strong>git merge</strong>:  
  
```  
$ git checkout master
$ git merge hotfix
Updating f42c576..3a0874c
Fast forward
 README |    1 -
 1 files changed, 0 insertions(+), 1 deletions(-)  
```  
  
Você irá notar a frase <strong>"Fast forward"</strong> no merge. Em razão do branch que você fez o merge <strong>apontar para o commit que está diretamente acima do commit que você se encontra</strong>, Git avança o ponteiro adiante. Em outras palavras, quando você tenta fazer o merge de um commit com outro que pode ser alcançado seguindo o histórico do primeiro, Git simplifica as coisas movendo o ponteiro adiante porque não existe modificações divergente para fazer o merge — isso é chamado de <strong>"fast forward"</strong>.  
  
Sua modificação está agora no snapshot do commit apontado pelo <strong>branch master</strong>, e você pode fazer o deploy, veja na figura abaixo:  
  
![Git - Guide](res/picture15.png)  
  
<strong>Depois do merge seu branch master aponta para o mesmo local que o branch hotfix(Isso porque os commits da branche master e hotfix são adjacentes).</strong>  
  
Depois que a sua correção super importante foi enviada, você está pronto para voltar ao trabalho que estava fazendo antes de ser interrompido. No entanto, primeiro você <strong>apagará o branch hotfix</strong>, pois você não precisa mais dele — o branch master aponta para o mesmo local. Você pode excluí-lo com a opção <strong>-d</strong> em <strong>git branch</strong>:  
  
```  
$ git branch -d hotfix  
Deleted branch hotfix (3a0874c).  
```  
  
Agora você pode voltar para o trabalho incompleto no branch da tafera <strong>#53</strong> e continuar a trabalhar nele:  
  
```  
$ git checkout iss53
Switched to branch "iss53"
$ vim index.html
$ git commit -a -m 'novo rodapé terminado [issue 53]'
[iss53]: created ad82d7a: "novo rodapé terminado [issue 53]"
 1 files changed, 1 insertions(+), 0 deletions(-)
```  
  
Veja a figura abaixo para entender melhor como serie esse fluxo de trabalho:  
  
![Git - Guide](res/picture16.png)  
<strong>Seu branch iss53 pode avançar de forma independente.</strong>  
  
Vale a pena lembrar aqui que o trabalho feito no seu branch <strong>hotfix</strong> não existe nos arquivos do seu branch <strong>iss53</strong>. Se você precisa incluí-lo, você pode fazer o merge do seu branch <strong>master</strong> no seu branch <strong>iss53</strong> executando o comando <strong>git merge master</strong>, ou você pode esperar para integrar essas mudanças até você decidir fazer o pull do branch <strong>iss53</strong> no <strong>master</strong> mais tarde.  
  
__Merge Básico__  
  
Suponha que você decidiu que o trabalho na <strong>tarefa #53(branching)</strong> está completo e pronto para ser feito o merge no branch <strong></strong>. Para fazer isso, você fará o merge do seu branch <strong>iss53</strong>, bem como o merge do branch <strong>hotfix</strong> de antes. Tudo que você tem a fazer é executar o checkout do branch para onde deseja fazer o merge e então rodar o comando <strong>git merge</strong>:  
  
```  
$ git checkout master
$ git merge iss53
Merge made by recursive.
 README | 1 +
 1 files changed, 1 insertions(+), 0 deletions(-)  
```  
  
Isso parece um pouco diferente do merge de <strong>hotfix</strong> que você fez antes. Neste caso, o histórico do seu desenvolvimento divergiu em algum ponto anterior. Pelo fato do commit no branch em que você está não ser um ancestral direto do branch que você está fazendo o merge, Git tem um trabalho adicional. Neste caso, Git faz um merge simples de três vias, usando os dois snapshots apontados pelas pontas dos branches e o ancestral comum dos dois. A figura abaixo destaca os três snapshots que Git usa para fazer o merge nesse caso.  
  
![Git - Guide](res/picture17.png)  
<strong>Git identifica automaticamente a melhor base ancestral comum para o merge do branch.</strong>  
  
Em vez de simplesmente avançar o ponteiro do branch adiante, Git cria um novo snapshot que resulta do <strong>merge de três vias</strong> e automaticamente cria um <strong>novo commit</strong> que aponta para as vias. Isso é conhecido como um merge de commits e é especial pois tem mais de um pai.  
  
Veja na figura abaixo como isso funciona:  
  
![Git - Guide](res/picture18.png)  
<strong>Git cria automaticamente um novo objeto commit que contém as modificações do merge.</strong>  
  
Vale a pena destacar que o Git determina o melhor ancestral comum para usar como base para o merge; isso é diferente no CVS ou Subversion (antes da versão 1.5), onde o desenvolvedor que está fazendo o merge tem que descobrir a melhor base para o merge por si próprio. Isso faz o merge muito mais fácil no Git do que nesses outros sistemas.  
  
Agora que foi feito o merge no seu trabalho, você não precisa mais do branch <strong>iss53</strong>. Você pode apagá-lo e fechar manualmente o chamado no seu gerenciador de chamados:  
  
```  
$ git branch -d iss53  
```  
  
__Conflitos de Merge Básico__  
  
Às vezes, esse processo não funciona sem problemas. Se você alterou a mesma parte do mesmo arquivo de forma diferente nos dois branches que está fazendo o merge, Git não será capaz de executar o merge de forma clara. Se sua correção para o erro <strong>#53</strong> alterou a mesma parte de um arquivo que <strong>hotfix</strong>, você terá um conflito de merge parecido com isso:  
  
```  
$ git merge iss53
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.  
```  
  
Git não criou automaticamente um novo commit para o merge. Ele fez uma pausa no processo enquanto você resolve o conflito. Se você quer ver em quais arquivos não foi feito o merge, em qualquer momento depois do conflito, você pode executar <strong>git status</strong>:  
  
```  
[master*]$ git status
index.html: needs merge
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#    unmerged:   index.html  
```  
  
Qualquer coisa que tem conflito no merge e não foi resolvido é listado como "unmerged". Git adiciona marcadores padrão de resolução de conflitos nos arquivos que têm conflitos, para que você possa abri-los manualmente e resolver esses conflitos. Seu arquivo terá uma seção parecida com isso:  
  
```  
<<<<<<< HEAD:index.html
<div id="footer">contato : email.support@github.com</div>
=======
<div id="footer">
  por favor nos contate em support@github.com
</div>
>>>>>>> iss53:index.html  
```  
  
Isso significa que a versão em <strong>HEAD</strong> (seu branch master, pois era isso que você tinha quando executou o comando merge) é a parte superior desse bloco (tudo acima de =======), enquanto a versão no seu branch <strong>iss53</strong> é toda a parte inferior. Para resolver esse conflito, você tem que optar entre um lado ou outro, ou fazer o merge do conteúdo você mesmo. Por exemplo, você pode resolver esse conflito através da substituição do bloco inteiro por isso:  
  
```  
<div id="footer">
por favor nos contate em email.support@github.com
</div>
```  
  
Esta solução tem um pouco de cada seção, e eu removi completamente as linhas <<<<<<<, =======, e >>>>>>>. Depois que você resolveu cada uma dessas seções em cada arquivo com conflito, rode git add em cada arquivo para marcá-lo como resolvido. Colocar o arquivo na área de seleção o marcar como resolvido no Git. Se você quer usar uma ferramenta gráfica para resolver esses problemas, você pode executar git mergetool, que abre uma ferramenta visual de merge adequada e percorre os conflitos:  
```  
$ git mergetool
merge tool candidates: kdiff3 tkdiff xxdiff meld gvimdiff opendiff emerge vimdiff
Merging the files: index.html

Normal merge conflict for 'index.html':
  {local}: modified
  {remote}: modified
Hit return to start merge resolution tool (opendiff):  
```  
  
### Management  
  
__Branch Management__  
  

Agora que você criou, fez merge e apagou alguns branches, vamos ver algumas ferramentas de gerenciamento de branches que serão úteis quando você começar a usá-los o tempo todo.  
  
O comando <strong>git branch</strong> faz mais do que criar e apagar branches. Se você executá-lo sem argumentos, você verá uma lista simples dos seus branches atuais:  
  
```  
$ git branch
  iss53
* master
  testing  
```  
  
Note o caractere <strong>*</strong> que vem antes do branch <strong>master</strong>: ele indica o branch que você está atualmente (fez o checkout). Isso significa que se você fizer um commit nesse momento, o branch <strong>master</strong> irá se mover adiante com seu novo trabalho. Para ver o último commit em cada branch, você pode executar o comando <strong>git branch -v</strong>:  
  
```  
$ git branch -v
  iss53   93b412c consertar problema em javascript
* master  7a98805 Merge branch 'iss53'
  testing 782fd34 adicionar drigols para a lista de autores nos readmes  
```  
  
Outra opção útil para saber em que estado estão seus branches é filtrar na lista somente branches que você já fez ou não o merge no branch que você está atualmente. As opções <strong>--merged</strong> e <strong>--no-merged</strong> estão disponíveis no Git desde a versão 1.5.6 para esse propósito. Para ver quais branches já foram mesclados no branch que você está, você pode executar <strong>git branch --merged</strong>:  
  
```  
$ git branch --merged
  iss53
* master  
```  
  
Por você já ter feito o merge do branch <strong>iss53</strong> antes, você o verá na sua lista. Os branches nesta lista sem o <strong>*</strong> na frente em geral podem ser apagados com <strong>git branch -d</strong>; você já incorporou o trabalho que existia neles em outro branch, sendo assim você não perderá nada.  
  
Para ver todos os branches que contém trabalho que você ainda não fez o merge, você pode executar </strong>git branch --no-merged</strong>:  
  
```  
$ git branch --no-merged
  testing  
```  
  
Isso mostra seu outro branch. Por ele conter trabalho que ainda não foi feito o merge, tentar apagá-lo com <strong>git branch -d</strong> irá falhar:  
  
```  
$ git branch -d testing
error: The branch 'testing' is not an ancestor of your current HEAD.
If you are sure you want to delete it, run `git branch -D testing`.  
```  
  
Se você quer realmente apagar o branch e perder o trabalho que existe nele, você pode forçar com </strong>-D</strong>, como a útil mensagem aponta.  
  
### Workflows  
  
__Branching Workflows__  
  
Devido ao Git usar um merge de três vias, fazer o merge de um branch em outro várias vezes em um período longo é geralmente fácil de fazer. Isto significa que você pode ter vários branches que ficam sempre abertos e que são usados em diferentes estágios do seu ciclo de desenvolvimento; você pode regularmente fazer o merge de alguns deles em outros.  
  
Muitos desenvolvedores Git tem um fluxo de trabalho que adotam essa abordagem, como ter somente código completamente estável em seus branches <strong>master</strong> — possivelmente somente código que já foi ou será liberado. Eles têm outro branch paralelo chamado <strong>develop</strong> ou algo parecido em que eles trabalham ou usam para testar estabilidade — ele não é necessariamente sempre estável, mas quando ele chega a tal estágio, pode ser feito o merge com o branch master. Ele é usado para puxar (pull) branches tópicos <strong>(topic, branches de curta duração, como o seu branch iss53 anteriormente)</strong> quando eles estão prontos, para ter certeza que eles passam em todos os testes e não acrescentam erros.  
  
Na realidade, nós estamos falando de <strong>ponteiros avançando na linha de commits</strong> que você está fazendo. Os branches estáveis estão muito atrás na linha histórica de commits, e os branches de ponta (que estão sendo trabalhados) estão a frente no histórico, veja a figura abaixo:  
  
![Git - Guide](res/picture19.png)  
<strong>Branches mais estáveis geralmente ficam atrás no histórico de commits.</strong>  
  
Normalmente é mais fácil pensar neles como um contêiner de trabalho, onde conjuntos de commits são promovidos a um contêiner mais estável quando eles são completamente testados, veja a ilustração abaixo:  
  
![Git - Guide](res/picture20.png)  
  
A ideia é que seus branches estejam em vários níveis de estabilidade; quando eles atingem um nível mais estável, é feito o merge no branch acima deles. Repetindo, ter muitos branches de longa duração não é necessário, mas geralmente é útil, especialmente quando você está lidando com projetos muito grandes ou complexos.  
  
__Branches Tópicos (topic)__  
  
Branches tópicos, entretanto, são úteis em projetos de qualquer tamanho. Um branch tópico é um branch de curta duração que você cria e usa para uma funcionalidade ou trabalho relacionado. Isso é algo que você provavelmente nunca fez com um controle de versão antes porque é geralmente muito custoso criar e fazer merge de branches. Mas no Git é comum criar, trabalhar, mesclar e apagar branches muitas vezes ao dia.  
  
Você viu isso na seção anterior com os branches <strong>iss53</strong> e <strong>hotfix</strong> que você criou. Você fez commits neles e os apagou depois que fez o merge com seu branch principal. Tecnicamente, isso lhe permite mudar completamente e rapidamente o contexto — em razão de seu trabalho estar separado em contêineres onde todas as modificações naquele branch estarem relacionadas ao tópico, é fácil ver o que aconteceu durante a revisão de código. Você pode manter as mudanças lá por minutos, dias, ou meses, e mesclá-las quando estivem prontas, não importando a ordem que foram criadas ou trabalhadas.  
  
__Exemplo__  
  
Considere um exemplo onde:  
  
1. Você está fazendo um trabalho (no <strong>master</strong>);
2. Cria um branch para um erro <strong>(iss91)</strong>, trabalha nele um pouco;  
3. Cria um segundo branch para testar uma nova maneira de resolver o mesmo problema <strong>(iss91v2)</strong>;  
4. Volta ao seu branch principal(<strong>master</strong>) e trabalha nele por um tempo;  
5. Cria um novo branch para trabalhar em algo que você não tem certeza se é uma boa ideia <strong>(dumbidea)</strong>.  
  
Seu histórico de commits irá se parecer com a figura abaixo:  
  
![Git - Guide](res/picture21.png)  
<strong>Seu histórico de commits com multiplos branches tópicos.</strong>  
  
Agora, vamos dizer que você decidiu que sua segunda solução é a melhor para resolver o erro <strong></strong>; e você mostrou seu branch <strong>dumbidea</strong> para seus colegas de trabalho, e ele é genial. Agora você pode jogar fora o branch original <strong>iss91</strong> (perdendo os commits <strong>C5</strong> e <strong>C6</strong>) e fazer o <strong>merge</strong> dos dois restantes. Seu histórico irá se parecer com a figura abaixo:  
  
![Git - Guide](res/picture22.png)  
<strong>Seu histórico depois de fazer o merge de dumbidea e iss91v2.</strong>  
  
É importante lembrar que você esta fazendo tudo isso com seus branches localmente. Quando você cria e faz o merge de branches, tudo está sendo feito somente no seu repositório Git — nenhuma comunicação com o servidor esta sendo feita.  
  
### RB  
  
__Remote Branches__  
  
Branches remotos são <strong>referências ao estado</strong> de seus branches no seu <strong>repositório remoto</strong>. São branches locais que você não pode mover, <strong>eles se movem automaticamente sempre que você faz alguma comunicação via rede</strong>. Branches remotos agem como marcadores para lembrá-lo onde estavam seus branches no seu repositório remoto na última vez que você se conectou a eles.  
  
Eles seguem o padrão <strong>(remote)/(branch)</strong>. Por exemplo, se você quer ver como o branch <strong>master</strong> estava no seu repositório remoto <strong>origin</strong> na última vez que você se comunicou com ele, você deve ver o branch <strong>origin/master</strong>.  
  
Se você estivesse trabalhando em um problema com alguns colegas e eles colocassem o branch <strong>iss53</strong> no repositório, você poderia ter seu próprio branch <strong>iss53</strong>; mas o branch no servidor iria fazer referência ao commit em <strong>origin/iss53</strong>.  
  
Isso pode parecer um pouco confuso, então vamos ver um exemplo. Digamos que você tem um servidor Git na sua rede em <strong>git.ourcompany.com</strong>:  
  
1. Se você cloná-lo, Git automaticamente dá o nome origin para ele;  
2. Baixa todo o seu conteúdo;  
3. Cria uma referência para onde o branch <strong>master</strong> dele está, e dá o nome <strong>origin/master</strong> para ele localmente, e você não pode movê-lo.  
  
O Git também dá seu próprio branch <strong>master</strong> como ponto de partida no mesmo local onde o branch <strong>master</strong> remoto está, a partir de onde você pode trabalhar, veja figura abaixo:  
  
![Git - Guide](res/picture23.png)  
<strong>Um comando clone do Git dá a você seu próprio branch master e origin/master faz referência ao branch master original.</strong>  
  
Se você estiver trabalhando no seu branch master local, e, ao mesmo tempo, alguém envia algo para <strong>git.ourcompany.com</strong> atualizando o branch master, seu histórico avançará de forma diferente. <strong>Além disso, enquanto você não fizer contado com seu servidor original, seu origin/master não se moverá</strong>, veja a figura abaixo:  
  
![Git - Guide](res/picture24.png)  
<strong>Veja que a branch master avançou no servidor(alguém enviou algo para servidor remoto), e sua branch origin/master continua de onde você clonou. Isso, porque você não fez contato com o servidor ainda.</strong>  
  
<strong>   </strong>  
  
__git fetch origin__  
  
Para sincronizar suas coisas, você executa o comando <strong>git fetch origin</strong>. Esse comando:  
  
 - Verifica qual servidor "origin" representa (nesse caso, é git.ourcompany.com);  
 - Obtém todos os dados que você ainda não tem;  
 - Atualiza o seu banco de dados local, movendo o seu origin/master para a posição mais recente e atualizada.  
  
Veja a figura abaixo:  
  
![Git - Guide](res/picture25.png)  
<strong>O comando git fetch atualiza suas referências remotas.</strong>  
  
__Múltiplos Servidores__  
  
Para demostrar o uso de múltiplos servidores remotos e como os branches remotos desses projetos remotos parecem, vamos assumir que você tem outro servidor Git interno que é usado somente para desenvolvimento por um de seus times. Este servidor está em:  
  
```  
git.team1.ourcompany.com  
```  
  
Você pode adicioná-lo como uma nova referência remota ao projeto que você está atualmente trabalhando executando o comando <strong>git remote add</strong>.  
  
Dê o nome de <strong>teamone</strong>, que será o apelido para aquela URL, veja a figura abaixo:  
  
![Git - Guide](res/picture26.png)  
<strong>Adicionando um novo servidor.</strong>  
  
Agora, você pode executar o comando <strong>git fetch teamone</strong> para obter tudo que o servidor <strong>teamone</strong> tem e você ainda não, veja a figura abaixo:  
  
![Git - Guide](res/picture27.png)  
  
Por esse servidor ter um subconjunto dos dados que seu servidor <strong>origin</strong> tem, Git não obtém nenhum dado, somente cria um branch chamado <strong>teamone/master</strong> que faz referência ao commit que teamone tem no master dele.  
  
### Rebasing  
  
No Git, existem duas maneiras principais de integrar mudanças de um branch em outro: o <strong>merge</strong> e o <strong>rebase</strong>. Nessa seção você aprenderá o que é rebase, como fazê-lo, por que é uma ferramenta sensacional, e em quais casos você não deve usá-la.  
  
__O Rebase Básico__  
  
Se você olhar para o exemplo abaixo(figura), você pode ver que você criou uma divergência no seu trabalho e fez commits em dois branches diferentes.  
  
![Git - Guide](res/picture28.png)  
  
A maneira mais fácil de integrar os branches, como já falamos, é o comando <strong>merge</strong>. Ele executa um merge de <strong>três vias</strong> entre os dois últimos snapshots (cópias em um determinado ponto no tempo) dos branches </strong>(C3 e C4)</strong> e o mais recente ancestral comum aos dois <strong>(C2)</strong>, criando um novo snapshot (e um commit), como é mostrado na figura abaixo:  
  
![Git - Guide](res/picture29.png)  
  
Porém, existe outro modo: você pode pegar o trecho da mudança que foi introduzido em <strong>C3</strong> e reaplicá-lo em cima do <strong>C4</strong>. No Git, isso é chamado de <strong>rebasing</strong>. Com o comando rebase, você pode pegar todas as mudanças que foram commitadas em um branch e replicá-las em outro.  
  
Nesse exemplo, se você executar o seguinte:  
  
```  
$ git checkout experiment
$ git rebase master
First, rewinding head to replay your work on top of it...
Applying: added staged command  
```  
  
Ele vai ao ancestral comum dos dois branches (no que você está e no qual será feito o rebase), pega a diferença (diff) de cada commit do branch que você está, salva elas em um arquivo temporário, restaura o branch atual para o mesmo commit do branch que está sendo feito o rebase e, finalmente, aplica uma mudança de cada vez. A figura abaixo ilustra esse processo:  
  
![Git - Guide](res/picture30.png)  
<strong>Fazendo o rebase em C4 de mudanças feitas em C3.</strong>  
  
Nesse ponto, você pode ir ao branch master e fazer um merge fast-forward, como na figura abaixo:  
  
![Git - Guide](res/picture31.png)  
  
Agora, o snapshot apontado por <strong>C3'</strong> é exatamente o mesmo apontado por <strong>C5</strong> no exemplo do merge. Não há diferença no produto final dessas integrações, mas o rebase monta um histórico mais limpo. Se você examinar um log de um branch com rebase, ele parece um histórico linear: como se todo o trabalho tivesse sido feito em série, mesmo que originalmente tenha sido feito em paralelo.  
  
Constantemente você fará isso para garantir que seus commits sejam feitos de forma limpa em um branch remoto — talvez em um projeto em que você está tentando contribuir mas não mantém. Nesse caso, você faz seu trabalho em um branch e então faz o rebase em <strong>origin/master</strong> quando está pronto pra enviar suas correções para o projeto principal. Desta maneira, o mantenedor não precisa fazer nenhum trabalho de integração — somente um merge ou uma inserção limpa.  
  
__Os Perigos do Rebase__  
  
Apesar dos benefícios do rebase existem os inconvenientes, que podem ser resumidos em um linha:  
  
<strong>Não faça rebase de commits que você enviou para um repositório público.</strong>  
  
Se você seguir essa regra você ficará bem. Se não seguir, as pessoas te odiarão e você será desprezado por amigos e familiares.  
  
Quando você faz o rebase, você está abandonando commits existentes e criando novos que são similares, mas diferentes. Se fizer o push de commits em algum lugar e outros pegarem e fizerem trabalhos baseado neles e você reescrever esses commits com <strong>git rebase</strong> e fizer o push novamente, seus colaboradores terão que fazer o merge de seus trabalhos novamente e as coisas ficarão bagunçadas quando você tentar trazer o trabalho deles de volta para o seu.  
  
### Revision  
  
__SHA Curto__  
  
Git é inteligente o suficiente para descobrir qual commit você quis digitar se você fornecer os primeiros caracteres, desde que o SHA-1 parcial tenha pelo menos quatro caracteres e não seja ambíguo — ou seja, somente um objeto no repositório atual começe com esse código SHA-1 parcial.  
  
Por exemplo, para ver um commit específico, digamos que você execute um comando <strong>git log</strong> e identifique o commit que adicionou uma certa funcionalidade:  
  
```  
$ git log
commit 734713bc047d87bf7eac9674765ae793478c50d3
Author: Scott Chacon <schacon@gmail.com>
Date:   Fri Jan 2 18:32:33 2009 -0800

    fixed refs handling, added gc auto, updated tests

commit d921970aadf03b3cf0e71becdaab3147ba71cdef
Merge: 1c002dd... 35cfb2b...
Author: Scott Chacon <schacon@gmail.com>
Date:   Thu Dec 11 15:08:43 2008 -0800

    Merge commit 'phedders/rdocs'

commit 1c002dd4b536e7479fe34593e72e6c6c1819e53b
Author: Scott Chacon <schacon@gmail.com>
Date:   Thu Dec 11 14:58:32 2008 -0800

    added some blame and merge stuff  
```  
  
Neste caso, escolho <strong>1c002dd....</strong> Se você executar <strong>git show</strong> nesse commit, os seguintes comandos são equivalentes (assumindo que as versões curtas não são ambíguas):  
  
```  
$ git show 1c002dd4b536e7479fe34593e72e6c6c1819e53b
$ git show 1c002dd4b536e7479f
$ git show 1c002d  
```  
  
__Referências de Branch__  
  
A maneira mais simples de especificar um commit requer que ele tenha uma referência de um branch apontando para ele. Então, você pode usar um nome de branch em qualquer comando no Git que espera um objeto commit ou valor SHA-1.  
  
Por exemplo, se você quer mostrar o último objeto commit em um branch, os seguintes comandos são equivalentes, assumindo que o branch <strong>topic1</strong> aponta para <strong>ca82a6d</strong>:  
  
```  
$ git show ca82a6dff817ec66f44342007202690a93763949
$ git show topic1  
```  
  
__Abreviações do RefLog__  
  
Uma das coisas que o Git faz em segundo plano enquanto você está fora é manter um reflog — um log de onde suas referências de HEAD e branches estiveram nos últimos meses.  
  
Você poder ver o reflog usando <strong>git reflog</strong>:  
  
```  
$ git reflog
734713b... HEAD@{0}: commit: fixed refs handling, added gc auto, updated
d921970... HEAD@{1}: merge phedders/rdocs: Merge made by recursive.
1c002dd... HEAD@{2}: commit: added some blame and merge stuff
1c36188... HEAD@{3}: rebase -i (squash): updating HEAD
95df984... HEAD@{4}: commit: # This is a combination of two commits.
1c36188... HEAD@{5}: rebase -i (squash): updating HEAD
7e05da5... HEAD@{6}: rebase -i (pick): updating HEAD  
```  
  
### Interactive  
  
__Interactive Staging__  
  
Git vem com alguns scripts que facilitam algumas tarefas de linha de comando. Aqui, você verá alguns comandos interativos que podem ajudar você a facilmente escolher combinações ou partes de arquivos para incorporar em um commit.  
  
Essas ferramentas são muito úteis se você modificou vários arquivos e decidiu que quer essas modificações em commits separados em vez de um grande e bagunçado commit. Desta maneira, você pode ter certeza que seus commits estão logicamente separados e podem ser facilmente revisados pelos outros desenvolvedores trabalhando com você. Se você executar git add com a opção <strong>-i</strong> ou <strong>--interactive</strong>, Git entra em um modo interativo de shell, exibindo algo desse tipo:  
  
```  
$ git add -i
           staged     unstaged path
  1:    unchanged        +0/-1 TODO
  2:    unchanged        +1/-1 index.html
  3:    unchanged        +5/-1 lib/simplegit.rb

*** Commands ***
  1: status     2: update      3: revert     4: add untracked
  5: patch      6: diff        7: quit       8: help
What now>  
```  
  
Você pode ver que esse comando lhe mostra uma visão muito diferente da sua área de seleção — basicamente a mesma informação que você recebe com <strong>git status</strong> mas um pouco mais sucinto e informativo. Ele lista as modificações que você colocou na área de seleção à esquerda e as modificações que estão fora à direita.  
  
Agora você só precisa digitar os números<strong>(ou letra/)</strong> referentes a cada opção. Por exemplo, 4  é referente a opção para adicionar um novo arquivo/diretório, depois selecionar no próximo menu interativo o número<strong>(ou letra/s)</strong> de cada arquivo que você deseja adicionar e continua o mesmo processo novamente.  
  
### Stash  
  
__Fazendo Stash__  
  
Muitas vezes, quando você está trabalhando em uma parte do seu projeto, as coisas estão em um estado confuso e você quer mudar de branch por um tempo para trabalhar em outra coisa. O problema é, você não quer fazer o commit de um trabalho incompleto somente para voltar a ele mais tarde. A resposta para esse problema é o comando <strong>git stash</strong>.  
  
Fazer <strong>Stash(esconder, juntar, acumular)</strong> é tirar o estado sujo do seu diretório de trabalho — isto é, seus arquivos modificados que estão sendo rastreados e mudanças na área de seleção — e o salva em uma pilha de modificações inacabadas que você pode voltar a qualquer momento.  
  
__Fazendo Stash do Seu Trabalho__  
  
Para demonstrar, você entra no seu projeto e começa a trabalhar em alguns arquivos e adiciona alguma modificação na área de seleção. Se você executar <strong>git status</strong>, você pode ver seu estado sujo:  
  
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
  
Agora você quer mudar de branch, mas não quer fazer o commit do que você ainda está trabalhando; você irá fazer o stash das modificações. Para fazer um novo stash na sua pilha, execute <strong>git stash</strong>:  
  
```  
$ git stash
Saved working directory and index state \
  "WIP on master: 049d078 added the index file"
HEAD is now at 049d078 added the index file
(To restore them type "git stash apply")  
```  
  
Seu diretório de trabalho está limpo:  
  
```  
$ git status
# On branch master
nothing to commit, working directory clean  
```  
  
Neste momento, você pode facilmente mudar de branch e trabalhar em outra coisa; suas alterações estão armazenadas na sua pilha. Para ver as stashes que você guardou, você pode usar <strong>git stash list</strong>:  
  
```  
$ git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051... Revert "added file_size"
stash@{2}: WIP on master: 21d80a5... added number to log  
```  
<strong>Nesse caso, duas stashes tinham sido feitas anteriormente, então você tem acesso a três trabalhos stashed diferentes.</strong>  
  
Você pode aplicar aquele que acabou de fazer o stash com o comando mostrado na saída de ajuda do comando stash original: <strong>git stash apply</strong>.  
  
Se você quer aplicar um dos stashes mais antigos, você pode especificá-lo, assim: <strong>git stash apply stash@{2}</strong>. Se você não especificar um stash, Git assume que é o stash mais recente e tenta aplicá-lo:  
  
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
  
Você pode ver que o Git altera novamente os arquivos que você reverteu quando salvou o stash. Neste caso, você tinha um diretório de trabalho limpo quando tentou aplicar o stash, e você tentou aplicá-lo no mesmo branch de onde tinha guardado; mas ter um diretório de trabalho limpo e aplicá-lo no mesmo branch não é necessario para usar um stash com sucesso.  
  
Você pode salvar um stash em um branch, depois mudar para outro branch, e tentar reaplicar as alterações. Você também pode ter arquivos alterados e sem commits no seu diretório de trabalho quando aplicar um stash — Git informa conflitos de merge se alguma coisa não aplicar de forma limpa.  
  
As alterações em seus arquivos foram reaplicadas, mas o arquivo que você colocou na área de seleção antes não foi adicionado novamente. Para fazer isso, você deve executar o comando <strong>git stash apply</strong> com a opção <strong>--index</strong> para informar ao comando para tentar reaplicar as modificações da área de seleção. Se você tivesse executado isso, você teria conseguido voltar à sua posição original:  
  
```  
$ git stash apply --index
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
  
A opção apply somente tenta aplicar o stash armazenado — ele continua na sua pilha. Para removê-lo, você pode executar <strong>git stash drop</strong> com o nome do stash que quer remover:  
  
```  
$ git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051... Revert "added file_size"
stash@{2}: WIP on master: 21d80a5... added number to log
$ git stash drop stash@{0}
Dropped stash@{0} (364e91f3f268f0900bc3ee613f9f733e82aaed43)  
```  
  
Você também pode executar <strong>git stash pop</strong> para aplicar o stash e logo em seguida apagá-lo da sua pilha:  
  
```  
$ git stash pop stash@{0}
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   aaaa.js

Dropped stash@{0} (a16e7ef845316efea62b9f2ea8e70c557e727222)  
```  
  
__Criando um Branch de um Stash__  
  
Se você criar um stash, deixá-lo lá por um tempo, e continuar no branch de onde criou o stash, você pode ter problemas em reaplicar o trabalho. Se o apply tentar modificar um arquivo que você alterou, você vai ter um conflito de merge e terá que tentar resolvê-lo.  
  
Se você quer uma forma mais fácil de testar as modificações do stash novamente, você pode executar <strong>git stash branch</strong>, que cria um novo branch para você, faz o checkout do commit que você estava quando criou o stash, reaplica seu trabalho nele, e então apaga o stash se ele é aplicado com sucesso:  
  
```  
$ git stash branch testchanges
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
  
Este é um bom atalho para recuperar facilmente as modificações em um stash e trabalhar nele em um novo branch.  
  
### PP  
  
__Encanamento (Plumbing) e Porcelana (Porcelain)__  
  
Quando você executa <strong>git init</strong> em um diretório novo ou existente, Git cria o diretório <strong>.git</strong>, que é onde quase tudo que o Git armazena e manipula está localizado. Se você deseja fazer o backup ou clonar seu repositório, copiar este diretório para outro lugar lhe dará quase tudo o que você precisa. Eis o que ele contém:  
  
```  
$ ls -a
HEAD
branches/
config
description
hooks/
index
info/
objects/
refs/  
```  
  
Você pode ver alguns outros arquivos lá, mas este é um novo repositório <strong>git init</strong> — é o que você vê por padrão.  
  
<strong>branches:</strong>  
O diretório <strong>branches</strong> não é usado por versões mais recentes do Git.  
  
<strong>description:</strong>  
O arquivo <strong>description</strong> só é usado pelo programa gitweb, então não se preocupe com eles.  
  
<strong>config:</strong>  
O arquivo <strong>config</strong> contém as opções de configuração específicas do projeto.  
  
<strong>info:</strong>  
O diretório <strong>info</strong> contém um arquivo de exclusão global com padrões ignorados que você não deseja rastrear em um arquivo .gitignore.  
  
<strong>hook:</strong>  
O diretório <strong>hooks</strong> contém os "hook scripts" de cliente ou servidor.  
  
Isso deixa quatro entradas importantes:  
  
<strong>Os arquivos:</strong>  
  
 - HEAD  
 - index  
  
<strong>Os diretórios:</strong>  
  
 - objects  
 - refs  
  
Estas são as peças centrais do Git.  
  
<strong>Diretório objects:</strong>  
O <strong>diretório objects</strong> armazena todo o conteúdo do seu banco de dados.  
  
<strong>Diretório refs:</strong>  
O <strong>diretório refs</strong> armazena os ponteiros para objetos de commit (branches).  
  
<strong>Arquivo HEAD:</strong>  
O <strong>arquivo HEAD</strong> aponta para o branch atual.  
  
<strong>Arquivo index:</strong>  
O <strong>arquivo index</strong> é onde Git armazena suas informações da área de preparação (staging area).  
  
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
  
**References:**  
https://git-scm.com/book/pt-br/v1/  
https://git-scm.com/book/en/v2/  
  
**Rodrigo Leite -** *Software Engineer*
