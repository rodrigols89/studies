# `Refatorando as mensagens de erro`

> Aqui vamos refatorar as mensagens de erro.

Por exemplo, vamos mostrar algumas mensagens de erro:

 - **Extensão não aceita:**
   - `video-completo.mp4: ["Arquivo inválido: 'video-completo.mp4'. O formato '.mp4' não é permitido. Apenas .XLSM, .XLS, .CSV, .XLSX, .PDF, .TXT, .DOCX, .DOC são aceitos."]`
 - **Arquivo que excede o limite de tamanho (100mb):**
   - `857mb-test.pdf: ["O arquivo '857mb-test.pdf' excede o limite de 100MB."]`

Vejam que na mensagem de erro acima nós:

 - Estamos mostrando o nome do arquivo que foi enviado (tentado) 2 vezes;
 - E a resposta está entre [].

Vamos começar atualizando a mensagem de erro na função `validate_file_type()` em `workspace/validators.py`:

[workspace/validators.py](../../../workspace/validators.py)
```python
# ANTES
def validate_file_type(uploaded_file):

    ext = os.path.splitext(uploaded_file.name)[1].lower()

    if ext not in ALLOWED_EXTENSIONS:
        msg = (
            f"Arquivo inválido: '{uploaded_file.name}'. "
            f"O formato '{ext}' não é permitido. "
            f"Apenas {ALLOWED_FORMATTED} são aceitos."
        )
        raise ValidationError(msg)


# DEPOIS
def validate_file_type(uploaded_file):

    ext = os.path.splitext(uploaded_file.name)[1].lower()

    if ext not in ALLOWED_EXTENSIONS:
        msg = (
            f"Arquivo '{uploaded_file.name}' inválido. "
            f"Apenas {ALLOWED_FORMATTED} são aceitos."
        )
        raise ValidationError(str)
```

**OUTPUT:**  
```bash
video-completo.mp4: ["Arquivo 'video-completo.mp4' inválido. Apenas .XLS, .PDF, .XLSM, .DOCX, .TXT, .DOC, .XLSX, .CSV são aceitos."]
```

Bem, ainda temos 2 coisas para corrijir:

 - O nome do arquivo está aparecendo 2 vezes;
 - Está vindo dentro de uma lista.

Agora vamos atualizar a função auxiliar `_validate_uploaded_file()` na nossa `view.py`:

[workspace/views.py](../../../workspace/views.py)
```python
# ANTES
def _validate_uploaded_file(uploaded_file):

    try:
        validate_file(uploaded_file)
        return None
    except Exception as e:
        if hasattr(e, '__str__'):
            error_message = str(e)  # ❌ Isso adiciona os colchetes []
        else:
            error_message = getattr(e, 'message', 'Erro desconhecido')
        return f"{uploaded_file.name}: {error_message}"  # ❌ Isso adiciona o prefixo


# DEPOIS
def _validate_uploaded_file(uploaded_file):

    try:
        validate_file(uploaded_file)
        return None
    except Exception as e:
        error_message = _extract_error_message(e)  # ✅ Remove os colchetes
        return error_message  # ✅ Retorna apenas a mensagem, sem prefixo
```

**OUTPUT:**
```bash
Arquivo 'video-completo.mp4' inválido. Apenas .CSV, .PDF, .DOCX, .XLS, .XLSX, .DOC, .TXT, .XLSM são aceitos.
```

> **E a mensagem quando o arquivo que excede o limite de tamanho (100mb):**

Na verdade ao atualizar a função auxiliar `_validate_uploaded_file()` nós já resolvemos esse problema também:

**OUTPUT:**
```bash
O arquivo '857mb-test.pdf' excede o limite de 100MB.
```

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**
