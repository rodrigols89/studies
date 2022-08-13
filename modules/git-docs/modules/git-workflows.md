# Git Workflows

## Contents

 - [Fluxo de trabalho Centralizado](#ftc)

---

<div id="ftc"></div>

## Fluxo de trabalho Centralizado

O fluxo de trabalho centralizado é o mais familiar para aqueles que vieram de outras ferramentas de versionamento mais antigas, como o **CVS** ou **SVN**. Nele você tem apenas um único servidor, e diversas pessoas trabalhando em seus repositórios locais, subindo os documentos para o repositório principal (servidor).

Explicando detalhadamente desde o inicio da vida de um repositório com **Fluxo de trabalho centralizado**, ele funcionaria da seguinte forma:  

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
      Então cada um segue com sua atividade e a medida que desejar, a pessoa <strong>adiciona (add)</strong> e realiza <strong>commit</strong> de suas alterações, para que o repositório local guarde o histórico do que foi feito. Este passo é executado até que a tarefa ou subtarefa esteja concluida.
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
      Por fim, é realizado o comando <strong>push</strong> para que suas alterações sejam enviadas ao repositório central (servidor).
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

**NOTE:**  
Este fluxo se chama **Fluxo de Trabalho Centralizado**, pois temos um único repositório servidor servindo como centralizador do código entre as equipes de desenvolvimento. É um fluxo bastante utilizado em mundo corporativo onde temos uma equipe pequena trabalhando. Porém mostra-se inviável em grandes projetos Open-Source, como por exemplo o projeto do kernel do GNU Linux.

---

**REFERENCES:**  
https://git-scm.com/book/pt-br/v1/  
https://git-scm.com/book/en/v2/  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
