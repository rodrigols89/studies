# FastAPI

## Conteúdo

 - [`Como montar (ou descobrir) um endpoint (rota) no FastAPI`](#descobrir-endpoint)
<!---
[WHITESPACE RULES]
- "20" Whitespace character.
--->





















---

<div id="descobrir-endpoint"></div>

## `Como montar (ou descobrir) um endpoint (rota) no FastAPI`

Imagine que nós (ou alguém) definou a seguinte rota (endpoint):

```python
router = APIRouter(
    prefix="/test",
)
```

E em determinada função nós temos a seguinte annotação:

```python
@router.post("/send-message")
def test_send_message:
    ...
```

Juntando tudo nós vamos ter:

```bash
/test + /send-message
```

Que vira:

```
/test/send-message
```

Agora, se seu FastAPI roda em:

 - [http://localhost:8000](http://localhost:8000)

a URL completa vai ser a seguinte:

 - [http://localhost:8000/test/send-message](http://localhost:8000/test/send-message)


> **Como descobrir as rotas?**

Abra:

 - [http://localhost:8000/docs](http://localhost:8000/docs)

Você verá algo parecido com:

 - POST -> `/test/send-message`
 - POST `/webhook/evolution`
 - GET `/healthcheck`

> **NOTE:**  
> O Swagger mostra todas as rotas registradas.

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**
