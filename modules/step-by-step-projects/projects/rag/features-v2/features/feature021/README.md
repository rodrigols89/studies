# `Reescrevendo as mensagens do Django Allauth`

Continuando, aqui nós temos um probleminha, quando nós deslogamos com alguma das contas sociais aparece uma mensagem na nossa página principal (langin page):

![img](images/social-login-02.png)  

É como se fosse o *"resto"* de uma mensagem do Django depois do login!

> **Como resolver isso?**

#### Criando um `adapter.py`

O arquivo [adapter.py](../../../users/adapter.py) serve para *personalizar o comportamento interno do Django Allauth*, que é o sistema responsável pelos *logins*, *logouts* e *cadastros* — tanto locais quanto via provedores sociais (como Google e GitHub).

Por padrão, o Allauth envia automaticamente mensagens para o sistema de mensagens do Django (django.contrib.messages), exibindo textos como:

 - “Successfully signed in as rodrigols89.”
 - “You have signed out.”
 - “Your email has been confirmed.”

Essas mensagens são geradas dentro dos adapters do `Allauth` — classes que controlam como ele interage com o Django.

Agora, vamos criar (recriar) nossas versões personalizadas dos adapters (`NoMessageAccountAdapter` e `NoMessageSocialAccountAdapter`) para impedir que essas mensagens automáticas sejam exibidas.

> **NOTE:**  
> Assim, temos controle total sobre quais mensagens aparecem para o usuário — mantendo o front mais limpo e sem textos gerados automaticamente.

[users/adapter.py](../../../users/adapter.py)
```python
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import (
    DefaultSocialAccountAdapter
)


class NoMessageAccountAdapter(DefaultAccountAdapter):
    def add_message(
        self,
        request,
        level,
        message_template,
        message_context=None
    ):
        return


class NoMessageSocialAccountAdapter(DefaultSocialAccountAdapter):
    def add_message(
        self,
        request,
        level,
        message_template,
        message_context=None
    ):
        return
```

Por fim, vamos adicionar algumas configurações gerais em `settings.py`:

[settings.py](../../../core/settings.py)
```python
ACCOUNT_ADAPTER = "users.adapter.NoMessageAccountAdapter"
SOCIALACCOUNT_ADAPTER = "users.adapter.NoMessageSocialAccountAdapter"
```

 - Use o caminho Python completo para a classe.
 - No exemplo acima assumimos que:
   - O app se chama `users`;
   - No arquivo `adapter`;
   - Estamos chamando as classes: `NoMessageAccountAdapter` e `NoMessageSocialAccountAdapter`.

Por fim, reinicie o servidor (python manage.py runserver) depois de editar `settings.py` para que as mudanças tenham efeito.

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**
