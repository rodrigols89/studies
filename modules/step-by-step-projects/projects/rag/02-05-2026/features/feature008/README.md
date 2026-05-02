# `Script de inicialização do serviço web (entrypoint.sh)`

> O arquivo [entrypoint.sh](../../../entrypoint.sh) é o script de inicialização do container Docker do projeto.

Ele é executado antes do Django subir, garantindo que o ambiente esteja corretamente preparado para rodar a aplicação com segurança.

As responsabilidades principais desse script são:

 - Criar diretórios essenciais (static, media e staticfiles);
 - Ajustar permissões e ownership desses diretórios;
 - Garantir que a aplicação não rode como root, mas sim como um usuário não privilegiado (appuser);
 - Executar o comando final do container de forma segura.

Esse padrão é altamente recomendado em ambientes Docker de produção, especialmente em projetos Django.

[entrypoint.sh](../../../entrypoint.sh)
```bash
#!/bin/bash
set -e

# Cria diretórios necessários se não existirem
mkdir -p /code/static /code/media /code/staticfiles

# Ajusta permissões e ownership dos diretórios
# Garante que o usuário appuser (UID 1000) possa escrever neles
chmod -R /code/static 755 /code/media /code/staticfiles

# Obtém o UID do appuser (geralmente 1000)
APPUSER_UID=$(id -u appuser 2>/dev/null || echo "1000")
APPUSER_GID=$(id -g appuser 2>/dev/null || echo "1000")

# Ajusta ownership se estiver rodando como root
if [ "$(id -u)" = "0" ]; then
    chown -R ${APPUSER_UID}:${APPUSER_GID} \
        /code/media /code/staticfiles 2>/dev/null || true
    # Executa o comando como appuser
    exec gosu appuser "$@"
else
    # Se já estiver rodando como appuser, apenas executa
    exec "$@"
fi
```

 - `#!/bin/bash`
   - Define que o script será interpretado pelo Bash.
   - Sem isso, o sistema pode tentar executar com outro shell incompatível.
 - `set -e`
   - Faz o script encerrar imediatamente se qualquer comando retornar erro (exit code ≠ 0).
   - Isso evita que o container suba parcialmente configurado.
 - `mkdir -p /code/static /code/media /code/staticfiles`
   - Cria os diretórios necessários para o Django:
     - `/code/static` → arquivos estáticos coletados;
     - `/code/media` → arquivos enviados pelos usuários;
     - `/code/staticfiles` → arquivos estáticos coletados
   - **NOTE:** A flag `-p` evita erro caso os diretórios já existam.
 - `chmod -R 755 /code/media /code/staticfiles`
   - Ajusta permissões recursivamente:
     - `Owner:` leitura, escrita e execução;
     - `Grupo:` leitura e execução;
     - `Outros:` leitura e execução.
   - **NOTE:** Isso garante acesso suficiente sem abrir permissões perigosas (777).
 - `APPUSER_UID=$(id -u appuser 2>/dev/null || echo "1000")`
   - Tenta obter o UID do usuário appuser.
   - Se o usuário existir → usa o UID real.
   - Se não existir → usa 1000 como fallback.
   - `2>/dev/null` evita poluir o log com erros.
 - `APPUSER_GID=$(id -g appuser 2>/dev/null || echo "1000")`
   - Faz o mesmo acima, porém para o GID (grupo do usuário).
 - `if [ "$(id -u)" = "0" ]; then`
   - Verifica se o script está sendo executado como root.
   - `id -u` retorna o UID do usuário atual
   - `UID 0 = root`
   - Esse é o ponto de decisão principal do script.
     - `chown -R ${APPUSER_UID}:${APPUSER_GID} \`
     - `/code/media /code/staticfiles 2>/dev/null || true`
       - Se estiver rodando como root:
         - Muda o dono dos diretórios para appuser
         - Garante que o Django possa escrever nesses caminhos
       - `||` true impede que uma falha aqui derrube o container por causa do `set -e`.
     - `exec gosu appuser "$@"`
       - Executa o comando final do container como "*appuser*", não como root.
       - Detalhes importantes:
         - `gosu` troca o usuário sem criar shell intermediário
         - `exec` substitui o processo atual
         - `$@` representa o comando do CMD ou docker-compose
       - Isso garante:
         - Segurança
         - Sinais corretos (SIGTERM, SIGINT)
         - Logs limpos
 - `else`
   - Esse bloco é executado se o container NÃO estiver rodando como root.
   - `exec "$@"`
   - Apenas executa o comando final normalmente, sem trocar de usuário.
   - Isso acontece quando:
     - O container já foi configurado para rodar como appuser
     - Ou o script foi chamado manualmente
 - `fi`
   - Finaliza a estrutura condicional.

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**
