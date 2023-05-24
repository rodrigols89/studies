# Setting

## Contents

 - [Configurando sua identidade (Username + Email)](#identity)
 - [Verificando suas configurações (git config --list)](#check)
 - [Configurando uma chave GPG (Assinando commits)](#sign-commits)

---

<div id="identity"></div>

## Configurando sua identidade (Username + Email)

A primeira coisa que você deve fazer quando instalar o **Git** é definir o seu:

 - **Nome de usuário;**
 - **Endereço de e-mail.**

Isso é importante porque todos os commits no **Git** utilizam essas informações, e está imutavelmente anexado nos commits que você realizar:

```python
$ git config --global user.name "drigols"
$ git config --global user.email drigols.creative@gmail.com
```
  
Relembrando, você só precisará fazer isso uma vez caso passe a opção <strong>--global</strong>, pois o Git sempre usará essa informação para qualquer coisa que você faça nesse sistema.

> **NOTE:**  
> Caso você queira sobrepor estas com um nome ou endereço de e-mail diferentes para projetos específicos, você pode executar o comando <strong>sem a opção --global</strong> quando estiver no próprio projeto.

---

<div id="check"></div>

## Verificando suas configurações (git config --list)

Caso você queira verificar suas configurações, você pode utilizar o comando **git config --list** para listar todas as configurações que o Git encontrar naquele momento:

```python
user.name=drigols
user.email=drigols.creative@gmail.com
core.editor=emacs
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
```

**NOTE:**  
Você também pode verificar qual o valor que uma determinada **chave** tem para o **Git** digitando **git config {key}**:

**Check username:**  
```python
git config user.name
drigols
```

**Check email:**  
```python
git config user.email
drigols.creative@gmail.com
```

---

<div id="sign-commits"></div>

## Configurando uma chave GPG (Assinando commits)

> Antes de configurar uma **chave GPG para assinar nossos commits**, primeiros nós devemos saber **"por que utilizar uma?"**.

Bem, se eu utilizar os comandos:

```bash
git config user.name your-user-name
```

e

```bash
git config user.email your-email
```

**NOTE:**  
Se eu adicionar o username de outra pessoa e o e-mail dela corretamente o Git vai entender que é ela quem está fazendo o commit. E isso nós gera um problema de **"autenticidade"**. Ou seja, eu não posso garantir que sou a pessoa **"x"** sem assinar o commit.

 - Do ponto de vista do Git, isso está realmente funcionando conforme o esperado. Os detalhes do committer são projetados apenas para identificar quem de seus colaboradores fez uma alteração e não devem ser usados ​​para autenticar pessoas.
 - Ser capaz de representar outros committers não introduz uma vulnerabilidade por si só:

No entanto, embora isso não seja uma vulnerabilidade de segurança em si, pode causar outros problemas. Ao ver um commit não assinado, você não tem garantia de que:

 - O autor é realmente a pessoa cujo nome está no commit.
 - A mudança de código que você vê é realmente o que o autor escreveu (ou seja, não foi adulterado).
 - Outro exemplo é alguém criando uma Pull Request maliciosa em um projeto de código aberto e fazendo com que pareça outra pessoa, por exemplo, alguém com uma grande reputação, co-autor dela, para tornar mais provável que o PR seja aceito (se você mantiver bibliotecas de código aberto, você sabe como pode ser demorado revisar completa e minuciosamente cada PR).

> **NOTE:**  
> - Em vez disso, criar o hábito de assinar seus commits do Git dá a você a capacidade de provar que você foi o autor de uma alteração de código específica. Ele também oferece a capacidade de garantir que ninguém possa modificar seu commit (ou seus metadados, como a hora em que você afirmou que foi feito) no futuro.
> - Observe que só porque você assina seus commits do Git, isso não impede que outras pessoas se passem por você. Porém, **elas não podem garantir que são você**.

Sabendo de tudo isso, agora vamos criar uma **chave GPG** para garantir que nossos commits vão ser assinados. Para isso vamos utilizar a **CLI "gpg"***:

**INPUT:**
```bash
gpg --help
```

**OUTPUT:**
```bash
gpg (GnuPG) 2.2.27
libgcrypt 1.9.4
Copyright (C) 2021 Free Software Foundation, Inc.
License GNU GPL-3.0-or-later <https://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Home: /home/drigols/.gnupg
Supported algorithms:
Pubkey: RSA, ELG, DSA, ECDH, ECDSA, EDDSA
Cipher: IDEA, 3DES, CAST5, BLOWFISH, AES, AES192, AES256, TWOFISH,
        CAMELLIA128, CAMELLIA192, CAMELLIA256
Hash: SHA1, RIPEMD160, SHA256, SHA384, SHA512, SHA224
Compression: Uncompressed, ZIP, ZLIB, BZIP2

Syntax: gpg [options] [files]
Sign, check, encrypt or decrypt
Default operation depends on the input data

Commands:
 
 -s, --sign                  make a signature
     --clear-sign            make a clear text signature
 -b, --detach-sign           make a detached signature
 -e, --encrypt               encrypt data
 -c, --symmetric             encryption only with symmetric cipher
 -d, --decrypt               decrypt data (default)
     --verify                verify a signature
 -k, --list-keys             list keys
     --list-signatures       list keys and signatures
     --check-signatures      list and check key signatures
     --fingerprint           list keys and fingerprints
 -K, --list-secret-keys      list secret keys
     --generate-key          generate a new key pair
     --quick-generate-key    quickly generate a new key pair
     --quick-add-uid         quickly add a new user-id
     --quick-revoke-uid      quickly revoke a user-id
     --quick-set-expire      quickly set a new expiration date
     --full-generate-key     full featured key pair generation
     --generate-revocation   generate a revocation certificate
     --delete-keys           remove keys from the public keyring
     --delete-secret-keys    remove keys from the secret keyring
     --quick-sign-key        quickly sign a key
     --quick-lsign-key       quickly sign a key locally
     --quick-revoke-sig      quickly revoke a key signature
     --sign-key              sign a key
     --lsign-key             sign a key locally
     --edit-key              sign or edit a key
     --change-passphrase     change a passphrase
     --export                export keys
     --send-keys             export keys to a keyserver
     --receive-keys          import keys from a keyserver
     --search-keys           search for keys on a keyserver
     --refresh-keys          update all keys from a keyserver
     --import                import/merge keys
     --card-status           print the card status
     --edit-card             change data on a card
     --change-pin            change a card's PIN
     --update-trustdb        update the trust database
     --print-md              print message digests
     --server                run in server mode
     --tofu-policy VALUE     set the TOFU policy for a key

Options:
 
 -a, --armor                 create ascii armored output
 -r, --recipient USER-ID     encrypt for USER-ID
 -u, --local-user USER-ID    use USER-ID to sign or decrypt
 -z N                        set compress level to N (0 disables)
     --textmode              use canonical text mode
 -o, --output FILE           write output to FILE
 -v, --verbose               verbose
 -n, --dry-run               do not make any changes
 -i, --interactive           prompt before overwriting
     --openpgp               use strict OpenPGP behavior

(See the man page for a complete listing of all commands and options)

Examples:

 -se -r Bob [file]          sign and encrypt for user Bob
 --clear-sign [file]        make a clear text signature
 --detach-sign [file]       make a detached signature
 --list-keys [names]        show keys
 --fingerprint [names]      show fingerprints
```

Você pode utilizar o comando **"gpg --list-keys"** para listar quais chaves você tem salvas no seu computador:

**INPUT:**
```bash
gpg --list-keys
```

Se você não tiver uma chave, poderá gerar uma com o comando **"gpg --full-generate-key"**:

**INPUT:**
```bash
gpg --full-generate-key
```

**NOTE:**  
A CLI lhe fará várias perguntas, responda e ela lhe retornará um output com várias informações sobre sua nova chave criada.

**OUTPUT:**
```bash
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
gpg: key ABA466EE517C403F marked as ultimately trusted
gpg: revocation certificate stored as 'source/.gnupg/openpgp-revocs.d/E43A4E0A13E0C738EC67B198ABA466EE517C403F.rev'
public and secret key created and signed.

pub   rsa3072 2023-05-24 [SC]
      E43A4E0A13E0C738EC67B198ABA466EE517C403F
uid                      test gpg (this is a GPG test key) <testgpg@gmail.com>
sub   rsa3072 2023-05-24 [E]
```

Você pode listar novamente para ver quais chaves você tem agora:

**INPUT:**
```bash
gpg --list-keys
```

**OUTPUT:**
```bash
pub   rsa3072 2023-05-24 [SC]
      E43A4E0A13E0C738EC67B198ABA466EE517C403F
uid           [ultimate] test gpg (this is a GPG test key) <testgpg@gmail.com>
sub   rsa3072 2023-05-24 [E]
```

**NOTE:**  
Você também pode utilizar comando **"gpg --list-secret-keys --keyid-format=long" (mais recomendado)** para listar o formato longo das chaves GPG para as quais você possui uma *chave pública* e *privada*:

**INPUT:**
```bash
gpg --list-secret-keys --keyid-format=long
```

**OUTPUT:**
```bash
sec   rsa3072/ABA466EE517C403F 2023-05-24 [SC]
      E43A4E0A13E0C738EC67B198ABA466EE517C403F
uid                 [ultimate] test gpg (this is a GPG test key) <testgpg@gmail.com>
ssb   rsa3072/D3E0801728E02250 2023-05-24 [E]
```

**NOTE:**  
Você pode identificar a **chave primária** pelo que segue após **“sec”**. No exemplo acima, o *ID* da chave primária é **"ABA466EE517C403F"**.

Agora extraia a **chave pública** da **chave privada** executando o comando **"export"** e especificando o **ID** da chave privada:

**INPUT:**
```bash
gpg --armor --export ABA466EE517C403F
```

**OUTPUT:**
```bash
-----BEGIN PGP PUBLIC KEY BLOCK-----
<YOUR PUBLIC KEY INFO HERE>
-----END PGP PUBLIC KEY BLOCK-----
```

Copie todo o conteúdo das informações da chave pública. Em seguida, precisamos dizer ao seu cliente git para usar a chave GPG gerada para assinar os commits.

**INPUT:**
```bash
git config --global user.signingkey ABA466EE517C403F
```

Se você rodar o comando **"git config --list"** novamente vai ver que a chave foi adicionada:

**INPUT:**
```bash
git config --list
```

**OUTPUT:**
```bash
user.name=your-git-username
user.email=your-git-email
user.signingkey=ABA466EE517C403F
```

 - Agora, toda vez que você fizer um git commit, ele será assinado com esta chave GPG.
 - **Chave de acesso a chave GPG:** Quando nós criamos nossa chave GPG nós criamos uma senha que dá acesso a nossa chave GPG.
   - Ao fazer um commit, você será solicitado a inserir a chave de acesso para a chave GPG.

Porém, nós também precisamos configuar o GitHub, vá no seu GitHub em **settings/SSH and GPG Keys**:

![img](images/ssh-gpg-settings.png)  

Selecione **"New GPG Key"**:

![img](images/add-key-button-github.png)  

Cole todo o bloco de chave pública aqui e selecione **"Add GPG key"**.

![img](images/paste-gpg-key-github.png)  

Sua chave agora foi adicionada ao GitHub.

Quando um git commit assinado for enviado para o GitHub, ele será verificado pela chave pública e o commit aparecerá como **“Verified”** nos logs de commit. Por exemplo:

![img](images/verified-commit-github.png)  



**INPUT:**
```bash

```

**OUTPUT:**
```bash

```



















Agora você tem que configurar o Git para utilizar essa chave, mas primeiro você tem que ativar a assinaturas de commits no Git com o comando **"git config commit.gpgsign true"**:

**INPUT:**
```bash
git config commit.gpgsign true
```

Você pode verificar essa alteração com o comando **"git config --list"**:

**INPUT:**
```bash
git config --list
```

**OUTPUT:**
```bash
...
...
...
commit.gpgsign=true
```


**INPUT:**
```bash

```

**OUTPUT:**
```bash

```


**INPUT:**
```bash

```

**OUTPUT:**
```bash

```


**INPUT:**
```bash

```

**OUTPUT:**
```bash

```


**INPUT:**
```bash

```

**OUTPUT:**
```bash

```


---

**REFERENCES:**  
https://git-scm.com/book/pt-br/v1/  
https://git-scm.com/book/en/v2/  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**

GnuPG needs to construct a user ID to identify your key.

Real name: Rodrigo Leite da Silva
Email address: drigols.creative@gmail.com
Comment: GPG key to sign commits
You selected this USER-ID:
    "Rodrigo Leite da Silva (GPG key to sign commits) <drigols.creative@gmail.com>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? o
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
gpg: key 31986A69EB370948 marked as ultimately trusted
gpg: revocation certificate stored as '/home/drigols/.gnupg/openpgp-revocs.d/3D309B81A8C0DF31D57F305E31986A69EB370948.rev'
public and secret key created and signed.

pub   rsa4096 2023-05-24 [SC]
      3D309B81A8C0DF31D57F305E31986A69EB370948
uid                      Rodrigo Leite da Silva (GPG key to sign commits) <drigols.creative@gmail.com>
sub   rsa4096 2023-05-24 [E]
