# `Refatorando a exibição das pastas e arquivos (Clicks, Houver, Select, Escape, Click Outside)`

> Aqui nós vamos refatorar a exibição de pastas e arquivos porque algumas funcionalidades não estão funcionando corretamente.

Por exemplo, vamos atualizar para:

 - Quando alguém clicar 1 vez em um arquivo ou pasta seja apenas selecionado;
 - Quando alguém clicar 2 vezes em um arquivo ou pasta seja aberto;
 - Quando alguém aperta *ESC* a pasta ou arquivo selecionado deixe de ser selecionado;
 - Quando alguém aperta fora da pasta ou arquivo selecionado o mesmo deixa de ser selecionado.

> **Mas como fazer isso?**

Vamos começar entendo e atualizando o nosso template `workspace_home.html`:

[workspace/templates/pages/workspace_home.html](../../../workspace/templates/pages/workspace_home.html)
```html
<!-- 📁 Listagem de pastas e arquivos -->
{% if folders or files %}
    <ul class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">


      ...


{% else %}
    <p class="pt-4 text-gray-500 italic">
        Nenhum item encontrado neste diretório.
    </p>
{% endif %}
```

Olhando para o código acima nós temos que:

 - `{% if folders or files %}`
   - Nós temos um `if` verificando se existe algum folder(s) ou file(s).
   - Se tiver nesse parte que nós vamos implementar algum mecanismo para exibir as pastas e arquivos.
 - `{% else %}`
   - Se não tiver nenhuma pasta (folders) ou arquivos (files) então vamos exibir uma mensagem dizendo que nenhuma pasta ou arquivo foi encontrada.

> **E agora como eu listo minhas pastas no bloco if**

```html
<ul class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">

    <!-- Pastas -->
    {% for folder in folders %}
        <li class="
                bg-white
                border
                rounded-lg
                p-4
                cursor-pointer
                transition
                transform
                hover:scale-102
                hover:bg-gray-200
                selectable-item"
            data-url="?folder={{ folder.id }}"
            data-target="_self"
            data-kind="folder"
            data-id="{{ folder.id }}"
            draggable="true">
                <div class="block">
                    <span class="text-gray-800
                                font-semibold flex
                                items-center space-x-2">
                        <span>📁</span>
                        <span>{{ folder.name }}</span>
                    </span>
                </div>
        </li>
    {% endfor %}

</ul>
```

 - **Primeiro veja que nós estamos criando uma lista:**
   - `<ul class="..."></ul>`
 - **Depois vejam nós estamos criando os itens da lista dinamicamente:**
   - `{% for folder in folders %}`
     - `<li class="..."></li>`

> **E os atributos desta lista?**

```html
<li class="
        bg-white
        border
        rounded-lg
        p-4
        cursor-pointer
        transition
        transform
        hover:scale-102
        hover:bg-gray-200
        selectable-item"
    data-url="?folder={{ folder.id }}"
    data-target="_self"
    data-kind="folder"
    data-id="{{ folder.id }}"
    draggable="true">
```

 - `bg-white`
   - Define a cor de fundo como branco (Tailwind).
 - `border`
   - Adiciona uma borda padrão (1px sólida).
   - Cor padrão: border-gray-200.
 - `rounded-lg`
   - Arredonda os cantos do elemento.
   - lg = tamanho grande do raio.
 - `p-4`
   - Adiciona padding interno.
   - 4 = escala do Tailwind (1rem / 16px)
 - `cursor-pointer`
   - Muda o cursor do mouse para a “mãozinha”.
   - Indica que o item é clicável.
 - `transition`
   - Ativa transições suaves para propriedades animáveis.
   - Normalmente usada junto com `hover:*`
 - `transform`
   - Habilita transformações CSS.
   - Obrigatório para: `hover:scale-105`
   - Sem isso, o scale não funciona corretamente.
 - `hover:scale-102`
   - Aumenta o item 2% ao passar o mouse.
   - Dá sensação de “card elevando”.
 - `hover:bg-gray-200`
   - Muda o fundo no hover.
 - `selectable-item`
   - 📌 Classe customizada (sua ou do projeto).
   - ❗ Não existe no Tailwind por padrão.
   - Exemplo típico de uso: `document.querySelectorAll('.selectable-item')`
 - `data-url="?folder={{ folder.id }}"`
   - Guarda a URL da pasta (atual).
   - Usado pelo JS para abrir o arquivo.
   - Exemplo: `const url = item.dataset.url;`
 - `data-target="_self"`
   - Diz ao JS para abrir em nova aba.
   - Exemplo: `window.open(url, "_blank");`
 - `data-kind="folder"`
   - Define o tipo do item.
   - Pode ser:
     - file.
     - folder.
 - `data-id="{{ folder.id }}"`
   - ID do arquivo no backend (Django).
   - Usado para:
     - seleção.
     - drag & drop.
     - ações (delete, rename).
 - `draggable="true"`
   - Habilita drag and drop.
   - HTML puro (não é Tailwind).
   - 📌 Permite arrastar arquivos/pastas

> **E agora como eu listo meus arquivos no bloco if**

A lógica é a mesma, porém, para listar os arquivos:

```html
<ul class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">

<!-- Arquivos -->
{% for file in files %}
    <li class="
            bg-white
            border
            rounded-lg
            p-4
            cursor-pointer
            transition
            transform
            hover:scale-102
            hover:bg-gray-200
            selectable-item"
        data-url="{{ file.file.url }}"
        data-target="_blank"
        data-kind="file" data-id="{{ file.id }}"
        draggable="true">
            <div class="block">
                <span class="
                            text-gray-800
                            font-semibold
                            flex items-center
                            space-x-2">
                    <span>📄</span>
                    <span>{{ file.name }}</span>
                </span>
            </div>
    </li>
{% endfor %}

</ul>
```

Porém, agora nós temos a seguinte situação, quando nós passamos o mouse em cima de alguma pasta ou arquivo:

 - Ele aumenta 2% (hover:scale-102).
 - Muda o fundo (hover:bg-gray-200).
 - **NOTE:** Porém, eu não abrir ou selecionar nenhum deles ainda.

Para resolver isso vamos criar o `workspace_home.js`:

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
(function () {

    'use strict';

})(); // IIFE
```

De início nós temos a seguinte implementação:

 - `(function () { ... })();`
   - IIFE (Immediately Invoked Function Expression).
   - Isso é uma função autoexecutável.
   - **O que significa?**
     - A função é criada;
     - E executada imediatamente;
     - Sem precisar chamar pelo nome.
 - `'use strict';`
   - Ativa o modo estrito do JavaScript.
   - Ele torna o JavaScript mais rigoroso e seguro.
   - Exemplo: `x = 10; // cria variável global sem querer`

Agora, vamos continuar com a implementação:

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
(function () {

    'use strict';

    // Aguarda o carregamento completo do DOM
    document.addEventListener("DOMContentLoaded", function () {
    
    }); // DOMContentLoaded

})(); // IIFE
```

 - `document.addEventListener("DOMContentLoaded", function () { ... })`
   - **Esse trecho é um dos mais importantes do JavaScript em páginas HTML.**
   - `document`
     - Representa toda a página HTML.
     - É o objeto principal do DOM (Document Object Model).
     - Tudo que você faz com HTML via JS começa aqui:
       - `document.querySelector(...)`
       - `document.getElementById(...)`
   - `addEventListener(...)`
     - Método que escuta eventos.
     - Diz ao navegador:
       - “Quando isso acontecer, execute essa função”
       - Sintaxe geral:
         - `element.addEventListener(evento, callback);`
   - `"DOMContentLoaded"`
     - *O que é esse evento?*
     - É um evento que dispara quando o HTML foi totalmente carregado e interpretado.
     - ⚠️ Importante:
       - Não espera imagens;
       - Não espera vídeos;
       - Não espera fontes externas.
     - Só espera:
       - ✔ HTML;
       - ✔ estrutura do DOM pronta.
   - `function () { ... }`
     - Callback (função de retorno).
     - Essa função não executa imediatamente.
     - Ela fica registrada.
     - Só roda quando o evento acontece.
     - 📌 Em português:
       - *“Quando o DOM estiver pronto, execute isso aqui”*

Bem, até então só implementamos a estrutura da função IIFE, agora vamos implementar a lógica para satisfazer os objetivos desta seção:

 - Quando alguém clicar 1 vez em um arquivo ou pasta seja apenas selecionado;
 - Quando alguém clicar 2 vezes em um arquivo ou pasta seja aberto;
 - Quando alguém aperta *ESC* a pasta ou arquivo selecionado deixe de ser selecionado;
 - Quando alguém aperta fora da pasta ou arquivo selecionado o mesmo deixa de ser selecionado.

[static/workspace/js/workspace_home.js](../../../static/workspace/js/workspace_home.js)
```js
(function () {

    'use strict';

    // Aguarda o carregamento completo do DOM
    document.addEventListener("DOMContentLoaded", function () {
    
        // Seleciona todos os itens clicáveis
        const items = document.querySelectorAll(".selectable-item");
        let selectedItem = null;

        /**
         * Remove seleção de todos os itens
         */
        function clearSelection() {
            items.forEach(item => {
                item.classList.remove("ring-2", "ring-blue-500");
            });
            selectedItem = null;
        }

        /**
         * Seleciona visualmente um item
         */
        function selectItem(item) {
            clearSelection();
            item.classList.add("ring-2", "ring-blue-500");
            selectedItem = item;
        }

        // Aplica eventos a cada item
        items.forEach(item => {

            // Clique simples → seleciona
            item.addEventListener("click", function (event) {
                event.preventDefault();
                selectItem(item);
            });

            // Duplo clique → navega
            item.addEventListener("dblclick", function () {
                const url = item.dataset.url;
                const target = item.dataset.target || "_self";

                if (!url) return;

                if (target === "_blank") {
                    window.open(url, "_blank");
                } else {
                    window.location.href = url;
                }
            });

        }); // items.forEach

        // Clique fora → limpa seleção
        document.addEventListener("click", function (event) {
            const clickedItem = event.target.closest(".selectable-item");
            if (!clickedItem) {
                clearSelection();
            }
        });

        // Limpa seleção ao pressionar ESC
        document.addEventListener("keydown", (event) => {
            if (event.key === "Escape") {
                clearSelection();
            }
        });

    }); // DOMContentLoaded
})(); // IIFE
```

Agora, vamos explicar algumas partes do código acima (só o necessário, sem repetir o que já foi explicado em outras partes do README):

```js
const items = document.querySelectorAll(".selectable-item");
let selectedItem = null;
```

 - `items`
   - Guarda todos os itens do workspace que podem ser selecionados (pastas e arquivos).
   - **const por que?**
     - a lista não muda.
     - os itens continuam os mesmos.
 - `selectedItem`
   - Guarda qual item está selecionado no momento.
   - **let por que?**
     - let → valor pode mudar.
     - começa como null → nenhum item selecionado.
     - Depois: selectedItem = itemClicado;
 - **Instrução por instrução:**
   - `document` → página HTML.
   - `querySelectorAll` → busca vários elementos.
   - `".selectable-item"` → classe usada nos `<li>`.

**Função clearSelection:**
```js
/**
 * Remove seleção de todos os itens
 */
function clearSelection() {
    items.forEach(item => {
        item.classList.remove("ring-2", "ring-blue-500");
    });
    selectedItem = null;
}
```

 - **Para que serve?**
   - Remove a seleção visual de todos os itens.
   - Reseta o estado interno de seleção.
 - `items.forEach(item => {}`
   - Percorre cada item do workspace.
   - item = um `<li>` por vez.
 - `item.classList.remove("ring-2", "ring-blue-500");`
   - Remove classes Tailwind que indicam seleção.
   - Essas classes criam o “contorno azul”.
   - Visualmente:
     - antes → item selecionado;
     - depois → item normal.
 - `selectedItem = null;`
   - Nenhum item está selecionado.
   - Estado interno limpo.
   - Muito importante para:
     - evitar conflito de seleção.
     - saber se algo está selecionado ou não.

**Função selectItem:**
```js
/**
 * Seleciona visualmente um item
 */
function selectItem(item) {
    clearSelection();
    item.classList.add("ring-2", "ring-blue-500");
    selectedItem = item;
}
```

 - **Para que serve?**
   - Seleciona um único item.
   - Garante que só um fique selecionado por vez.
 - `clearSelection();`
   - Remove qualquer seleção anterior.
   - Evita múltiplos itens selecionados.
   - Comportamento de explorador de arquivos real.
 - `item.classList.add("ring-2", "ring-blue-500");`
   - Adiciona borda azul ao item.
   - Feedback visual claro.
 - `selectedItem = item;`
   - Guarda o item selecionado.
   - Permite ações futuras:
     - delete;
     - rename;
     - move;
     - abrir.

**Aplica eventos a cada item:**
```js
items.forEach(item => {});
```

 - **Para que serve?**
   - Percorre cada item do workspace.
   - Permite adicionar eventos em todos.
 - **Sem isso:**
   - só um item teria comportamento.
   - os outros não responderiam.

**Clique simples → seleciona:**
```js
item.addEventListener("click", function (event) {
    event.preventDefault();
    selectItem(item);
});
```

 - **Para que serve?**
   - Selecionar o item com clique simples.
 - `item.addEventListener("click", function (event) {...})`
   - Escuta o clique do mouse.
   - *event* = informações do clique.
 - `event.preventDefault();`
   - Evita comportamento padrão.
   - Importante se:
     - `houver <a>`;
     - `houver drag`;
     - houver navegação automática.
 - `selectItem(item);`
   - Marca visualmente o item.
   - Atualiza *"selectedItem"*.
   - Igual ao Windows / macOS:
     - 1 clique → seleciona.
     - não abre.

**Duplo clique → navega:**
```js
item.addEventListener("dblclick", function () {
    const url = item.dataset.url;
    const target = item.dataset.target || "_self";

    if (!url) return;

    if (target === "_blank") {
        window.open(url, "_blank");
    } else {
        window.location.href = url;
    }
});
```

 - **Para que serve?**
   - Abrir arquivo ou pasta com duplo clique.

**Clique fora → limpa seleção:**
```js
document.addEventListener("click", function (event) {
    const clickedItem = event.target.closest(".selectable-item");
    if (!clickedItem) {
        clearSelection();
    }
});
```

 - **Para que serve?**
   - Clicou fora dos itens → desseleciona tudo.

**ESC → limpa seleção:**
```js
document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
        clearSelection();
    }
});
```

 - **Para que serve?**
   - Pressionar ESC remove a seleção.

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**
