# `Refatorando o modal para abrir selecionando o campo de digitação`

> Bem, nós precisamos refatorar o modal para assim que abrir selecionar o campo de digitação automaticamente.

Vamos começar adicionando o seguinte código:

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
// Usa delegação de eventos para capturar cliques em
// elementos com atributo "command"
document.addEventListener("click", function (event) {
    // Verifica se o elemento clicado (ou seu pai) tem
    // o atributo "command"
    const commandElement = event.target.closest(
        '[command]'
    );
    
    // Se não encontrou, ignora o evento
    if (!commandElement) return;
    
    // Obtém o tipo de comando (ex: "show-modal", "close")
    const command = commandElement.getAttribute("command");
    
    // Obtém o alvo do comando (ex: "create_folder_modal")
    const commandFor = commandElement.getAttribute(
        "commandfor"
    );
    
    // Se não há comando ou alvo, ignora
    if (!command || !commandFor) return;
    
    // ========================================================
    // COMANDO: show-modal
    // ========================================================
    // Abre um modal e foca no campo de input
    if (command === "show-modal") {
        // Busca o elemento <dialog> pelo ID especificado
        const modal = document.getElementById(commandFor);
        
        // Se o modal não existe, não faz nada
        if (!modal) return;
        
        // Abre o modal usando a API nativa do HTML5
        modal.showModal();
        
        // Busca o campo de input dentro do modal
        // Usa o ID "folder_name" que está no HTML
        const inputField = modal.querySelector(
            "#folder_name"
        );
        
        // Se o campo existe, foca nele
        // O setTimeout garante que o foco aconteça após
        // o modal estar totalmente renderizado
        if (inputField) {
            setTimeout(function () {
                inputField.focus();
                // Seleciona todo o texto (se houver)
                // para facilitar substituição
                inputField.select();
            }, 100);
        }
    }
    
    // ========================================================
    // COMANDO: close
    // ========================================================
    // Fecha um modal
    if (command === "close") {
        // Busca o elemento <dialog> pelo ID especificado
        const modal = document.getElementById(commandFor);
        
        // Se o modal não existe, não faz nada
        if (!modal) return;
        
        // Fecha o modal usando a API nativa do HTML5
        modal.close();
    }
});
```

Agora, vamos explicar algumas partes do código acima (só o necessário, sem repetir o que já foi explicado em outras partes do README):


**Delegação de eventos:**
```js
document.addEventListener("click", function (event) {
    const commandElement = event.target.closest('[command]');
    ...
});
```

 - Usa delegação para capturar cliques em elementos com `command`.
 - Funciona mesmo se o botão for adicionado dinamicamente.

**Identificação do comando:**
```js
const command = commandElement.getAttribute("command");
const commandFor = commandElement.getAttribute("commandfor");
```

 - Lê os atributos para determinar a ação e o alvo.

**Abertura do modal:**
```js
if (command === "show-modal") {
    const modal = document.getElementById(commandFor);
    if (!modal) return;
    modal.showModal();
    ...
}
```

 - Localiza o modal pelo ID e abre com `showModal()`.

**Foco no campo de digitação:**
```js
const inputField = modal.querySelector("#folder_name");
if (inputField) {
    setTimeout(function () {
        inputField.focus();
        inputField.select();
    }, 100);
}
```

 - Localiza o `<input>` dentro do modal.
 - Usa `setTimeout()` para garantir que o foco ocorra após a renderização.
 - `focus()` foca o campo; `select()` seleciona o texto existente.

**Fechamento do modal:**
```js
if (command === "close") {
    const modal = document.getElementById(commandFor);
    if (!modal) return;
    modal.close();
}
```

 - Fecha o modal quando o botão *"Cancelar"* é clicado.

**Verificação do HTML (opcional):**
```html
<!-- Linha 228-241 -->
<input
    type="text"
    name="name"
    id="folder_name"  <!-- ✅ ID único e correto -->
    required
    class="
        mt-1 block
        w-full
        px-4
        py-2
        border
        rounded-lg"
    autocomplete="off"
    value="{{ form.name.value|default:'' }}">


<!-- Linha 160-161 -->
<dialog
    id="create_folder_modal"  <!-- ✅ ID correto -->
    aria-labelledby="modal-title"
    ...
```

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**
