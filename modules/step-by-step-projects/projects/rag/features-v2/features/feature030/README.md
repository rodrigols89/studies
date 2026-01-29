# `Refatorando para quando o usuário digitar um nome para uma pasta existente`

Continuando nas refatorações, nós temos o seguinte problema:

 - Quando um usuário digita o nome de uma pasta que já existe essa pasta não é criada, porém, o fecha.
 - Quando eu clico novamente em "➕ Nova Pasta" ele continua com o mesmo nome que eu digitei e a mensagem:
   - Já existe uma pasta com esse nome nesse diretório.

> **O que nós queremos agora?**

Eu quero que quando eu digitar um nome de ums pasta que já exista:

 - Apareça a mensagem de erro imediatamente: *"Já existe uma pasta com esse nome nesse diretório."*;
 - Se eu clicar em cancelar limpe a frase/palavra que eu digitei no campo;
 - Limpe a mensagem de erro: *"Já existe uma pasta com esse nome nesse diretório."*;
 - **NOTE:** Como se fosse uma nova sessão de criação de pasta.

Vamos começar implementando a função `getExistingFolderNames()` responsável por descobrir quais pastas já existem no diretório atual, diretamente a partir do HTML renderizado na página.

> Ela não consulta o backend, nem faz requisições HTTP.

Em vez disso, ela:

 - Varre o DOM;
 - Identifica todos os itens que representam pastas;
 - Extrai o nome visível de cada pasta;
 - Normaliza esses nomes (minúsculas);
 - Retorna uma lista pronta para comparação

Essa função é a base da validação de nome duplicado, sendo usada por:

 - folderNameExists (Função que vamos criar ainda);
 - Validação em tempo real (evento input);
 - Bloqueio da submissão do formulário;

Ela garante que o usuário não crie uma pasta com nome repetido no mesmo nível:

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
function getExistingFolderNames() {
    const folderItems = document.querySelectorAll(
        '[data-kind="folder"]'
    );
    const folderNames = [];
    
    folderItems.forEach(function (item) {
        // O nome da pasta está no segundo span dentro do item
        // Estrutura: <span><span>📁</span><span>Nome</span></span>
        // Busca todos os spans aninhados
        const allSpans = item.querySelectorAll("span span");
        
        if (allSpans.length >= 2) {
            // Pega o último span que contém o nome da pasta
            const nameSpan = allSpans[allSpans.length - 1];
            const folderName = nameSpan.textContent.trim();
            
            // Normaliza o nome para comparação (minúsculas)
            if (folderName) {
                const normalized = folderName.toLowerCase();
                folderNames.push(normalized);
            }
        }
    });
    
    return folderNames;
}
```

Agora, vamos implementar a função `folderNameExists(folderName)` que vai ser um validador lógico, simples e reutilizável.

O papel dela é responder apenas uma pergunta:

> “Já existe uma pasta com esse nome neste diretório?”

Para isso, ela:

 - Normaliza o nome digitado pelo usuário;
 - Obtém a lista de nomes existentes via `getExistingFolderNames()`;
 - Compara os valores de forma segura (case-insensitive);

Ela centraliza a regra de negócio da validação, evitando:

 - Código duplicado;
 - Lógicas espalhadas pelo JS;
 - Erros de comparação (maiúsculas/minúsculas).

Essa função é usada em:

 - Validação enquanto o usuário digita;
 - Validação antes do envio do formulário.

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
function folderNameExists(folderName) {
    if (!folderName || !folderName.trim()) {
        return false;
    }
    
    const existingNames = getExistingFolderNames();
    const normalizedName = folderName.trim().toLowerCase();
    
    return existingNames.includes(normalizedName);
}
```

Continuando, vamos implementar a função `showErrorMessage(errorElement, message)` responsável por exibir mensagens de erro no modal, de forma padronizada.

Ela abstrai completamente a lógica de:

 - Inserir texto de erro;
 - Tornar a mensagem visível;
 - Garantir consistência visual.

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
function showErrorMessage(errorElement, message) {
    if (!errorElement) return;
    
    errorElement.textContent = message;
    errorElement.classList.remove("hidden");
}
```

Agora, vamos implementar a função `hideErrorMessage(errorElement)` que é um complemento direto de `showErrorMessage()`.

O papel dela é:

 - Limpar o texto de erro;
 - Ocultar visualmente a mensagem;
 - Restaurar o estado “limpo” do modal

Ela é chamada quando:

 - O campo fica vazio;
 - O nome digitado passa a ser válido;
 - O modal é aberto novamente;
 - O modal é cancelado.

Essa separação (show/hide) deixa o fluxo de validação:

 - Mais legível;
 - Mais previsível;
 - Mais fácil de evoluir futuramente.

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
function hideErrorMessage(errorElement) {
    if (!errorElement) return;
    
    errorElement.textContent = "";
    errorElement.classList.add("hidden");
}
```

Agora, vamos implementar a função `initializeFolderValidation()`, essa é a função mais importante de todo o sistema de validação do modal.

Ela é responsável por configurar e garantir que:

 - A validação em tempo real esteja ativa;
 - O formulário não seja enviado com nome inválido;
 - Os listeners não sejam duplicados;
 - O comportamento funcione mesmo quando o modal abre dinamicamente.

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
// Referência ao modal de criação de pasta
const createFolderModal = document.getElementById(
    "create_folder_modal"
);

function initializeFolderValidation() {
    if (!createFolderModal) return;
    
    const folderNameInput = createFolderModal.querySelector(
        "#folder_name"
    );
    const errorMessage = createFolderModal.querySelector(
        "#server-error"
    );
    const createFolderForm = createFolderModal.querySelector(
        "form"
    );
    
    if (!folderNameInput || !errorMessage) return;
    
    // Remove listeners anteriores se existirem (usando clone)
    // para evitar duplicação
    const hasInputListener = folderNameInput.hasAttribute(
        "data-validation-attached"
    );
    
    if (!hasInputListener) {
        // Validação em tempo real enquanto o usuário digita
        folderNameInput.addEventListener("input", function () {
            const folderName = this.value.trim();
            
            // Se o campo estiver vazio, remove o erro
            if (!folderName) {
                hideErrorMessage(errorMessage);
                return;
            }
            
            // Verifica se o nome já existe
            if (folderNameExists(folderName)) {
                showErrorMessage(
                    errorMessage,
                    "Já existe uma pasta com esse nome " +
                    "nesse diretório."
                );
            } else {
                hideErrorMessage(errorMessage);
            }
        });
        
        folderNameInput.setAttribute(
            "data-validation-attached",
            "true"
        );
    }
    
    // Previne submissão do formulário se houver erro
    if (createFolderForm && 
        !createFolderForm.hasAttribute("data-submit-listener")) {
        createFolderForm.addEventListener("submit", function (
            event
        ) {
            const folderName = folderNameInput.value.trim();
            
            // Se o campo estiver vazio, permite validação
            // HTML5 padrão
            if (!folderName) {
                return;
            }
            
            // Se o nome já existe, previne a submissão
            if (folderNameExists(folderName)) {
                event.preventDefault();
                showErrorMessage(
                    errorMessage,
                    "Já existe uma pasta com esse nome " +
                    "nesse diretório."
                );
                // Foca no campo para facilitar correção
                folderNameInput.focus();
                folderNameInput.select();
            }
        });
        
        createFolderForm.setAttribute(
            "data-submit-listener",
            "true"
        );
    }
}
```

Agora vamos atualizar o `document.addEventListener("click", function (event)`:

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
        
        // Limpa o campo e mensagem de erro ao abrir o modal
        if (commandFor === "create_folder_modal") {
            const inputField = modal.querySelector(
                "#folder_name"
            );
            const errorMessage = modal.querySelector(
                "#server-error"
            );
            
            if (inputField) {
                inputField.value = "";
                // Dispara evento input para garantir validação
                inputField.dispatchEvent(new Event("input", {
                    bubbles: true
                }));
            }
            if (errorMessage) {
                errorMessage.textContent = "";
                errorMessage.classList.add("hidden");
            }
            
            // Garante que a validação está inicializada
            setTimeout(initializeFolderValidation, 50);
        }
        
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
        
        // Limpa o campo e mensagem de erro ao cancelar
        if (commandFor === "create_folder_modal") {
            const inputField = modal.querySelector(
                "#folder_name"
            );
            const errorMessage = modal.querySelector(
                "#server-error"
            );
            
            if (inputField) {
                inputField.value = "";
            }
            if (errorMessage) {
                errorMessage.textContent = "";
                errorMessage.classList.add("hidden");
            }
        }
        
        // Fecha o modal usando a API nativa do HTML5
        modal.close();
    }
});
```

Por fim, vamos criar um `bloco if` que vai ser responsável por orquestrador final da validação, o objetivo dele vai ser garantir que:

 - O DOM esteja completamente carregado;
 - O modal exista na página;
 - A validação seja inicializada no momento certo;
 - O comportamento funcione mesmo em cenários especiais.

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
// Inicializa a validação quando o DOM estiver pronto
if (createFolderModal) {
    // Aguarda um pouco para garantir que o DOM está completo
    setTimeout(function () {
        initializeFolderValidation();
        
        // Se o modal abre automaticamente (erro do servidor),
        // garante que a validação esteja ativa
        if (createFolderModal.hasAttribute("data-auto-open")) {
            // Abre o modal automaticamente
            createFolderModal.showModal();
            
            // Aguarda o modal abrir completamente
            setTimeout(function () {
                initializeFolderValidation();
            }, 300);
        }
    }, 100);
}
```

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**
