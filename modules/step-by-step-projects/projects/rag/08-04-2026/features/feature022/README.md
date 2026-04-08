# `Criando o app "workspace"`

> Aqui vamos criar um app Django dedicado ao *Workspace (onde o usuário poderá criar pastas e fazer upload de arquivos)* e registrar esse app nas configurações do projeto.

**SE VOCÊ CRIAR DIRETAMENTE DO CONTAINER NÃO VAI TER PERMISSÕES LOCAIS:**
```bash
python manage.py startapp workspace
```

**AGORA VAMOS REINICIAR O CONTAINER PARA ESSA ALTERAÇÃO REFLETIR NO CONTAINER:**
```bash
task restart_compose
```

Agora vamos registrar esse app nas configurações do projeto:

[settings.py](../../../core/settings.py)
```python
INSTALLED_APPS = [

    ...

    # Seus apps
    "users",
    "workspace",
]
```

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**
