# `Criando o script de inicialização do serviço web (entrypoint.sh)`

> O arquivo `entrypoint.sh` é o script de inicialização que *nós vamos utilizar dentro do container*.

Ele é executado *antes do Django subir (no container)*, garantindo que o ambiente esteja corretamente preparado para rodar a aplicação com segurança.

As responsabilidades principais desse script são:

 - Criar diretórios essenciais (static, media e staticfiles);
 - Ajustar permissões e ownership desses diretórios;
 - Garantir que a aplicação não rode como root, mas sim como um usuário não privilegiado (appuser);
 - Executar o comando final do container de forma segura.

### `Código completo`

[entrypoint.sh](../../../entrypoint.sh)
```bash
#!/bin/bash
set -e

mkdir -p /code/static /code/media /code/staticfiles

APPUSER_UID=$(id -u appuser 2>/dev/null || echo "1000")
APPUSER_GID=$(id -g appuser 2>/dev/null || echo "1000")

if [ "$(id -u)" = "0" ]; then
    chown -R ${APPUSER_UID}:${APPUSER_GID} \
        /code/static \
        /code/media \
        /code/staticfiles 2>/dev/null || true
fi

# 👇 Só executa gosu se um comando foi passado
if [ "$#" -gt 0 ]; then
    exec gosu appuser "$@"
fi

# 👇 Mantém o container vivo
tail -f /dev/null
```

### `🧠 Esse script roda quando? Antes ou depois do container subir? Quem executa?`

Esse script vai ser executado no momento em que o container estiver iniciando, ou seja, depois que ele foi criado e os volumes já foram montados, mas antes do comando principal (CMD/command) ser executado.

 - Inicialmente ele é executado como root (porque o container inicia como root por padrão).
 - Se a condição do `if` for verdadeira, ele troca o usuário para `appuser` e então executa o comando principal do container como esse usuário.

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**
