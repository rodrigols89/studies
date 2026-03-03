(function () {

    'use strict';

    // Aguarda o carregamento completo do DOM
    document.addEventListener("DOMContentLoaded", function () {
    
        // Seleciona todos os itens clicáveis
        const items = document.querySelectorAll(".selectable-item");
        let selectedItem = null;

        // ============================================================
        // 🧠 Validação em tempo real do Modal de Pasta
        // ============================================================

        const createFolderModal = document.getElementById(
            "create_folder_modal"
        );

        if (createFolderModal) {

            const folderNameInput = createFolderModal.querySelector(
                "#folder_name"
            );

            const errorMessage = createFolderModal.querySelector(
                "#server-error"
            );

            const createFolderForm = createFolderModal.querySelector(
                "form"
            );

            // ============================================================
            // 🧹 Limpa erro sempre que o modal for fechado
            // ============================================================

            createFolderModal.addEventListener("close", function () {

                folderNameInput.value = "";
                hideErrorMessage(errorMessage);

            });

            // ============================================================
            // 🎯 Foca automaticamente quando o modal abrir
            // ============================================================

            const observer = new MutationObserver(function (mutations) {

                mutations.forEach(function (mutation) {

                    if (
                        mutation.attributeName === "open" &&
                        createFolderModal.hasAttribute("open")
                    ) {
                        setTimeout(function () {
                            folderNameInput.focus();
                            folderNameInput.select();
                        }, 50);
                    }

                });

            });

            observer.observe(createFolderModal, {
                attributes: true
            });

            // Validação enquanto digita
            folderNameInput.addEventListener("input", function () {

                const folderName = this.value.trim();

                if (!folderName) {
                    hideErrorMessage(errorMessage);
                    return;
                }

                if (folderNameExists(folderName)) {

                    showErrorMessage(
                        errorMessage,
                        "Já existe uma pasta com esse nome nesse diretório."
                    );

                } else {
                    hideErrorMessage(errorMessage);
                }
            });

            // Bloqueia envio do formulário se existir duplicata
            createFolderForm.addEventListener("submit", function (
                event
            ) {

                const folderName = folderNameInput.value.trim();

                if (!folderName) return;

                if (folderNameExists(folderName)) {

                    event.preventDefault();

                    showErrorMessage(
                        errorMessage,
                        "Já existe uma pasta com esse nome nesse diretório."
                    );

                    folderNameInput.focus();
                    folderNameInput.select();
                }
            });
        }

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

        const uploadButton = document.getElementById("upload_button");
        const uploadMenu = document.getElementById("upload_menu");

        // Mostrar dropdown ao clicar
        uploadButton.addEventListener("click", function (event) {
            event.stopPropagation();
            uploadMenu.classList.toggle("hidden");
        });

        // Fechar dropdown ao pressionar ESC
        document.addEventListener("keydown", function(event) {
            if (event.key === "Escape" && !uploadMenu.classList.contains("hidden")) {
                uploadMenu.classList.add("hidden");
            }
        });

        // Fechar dropdown ao clicar fora
        document.addEventListener("click", function(event) {
            // Verifica se o clique foi fora do botão e do menu
            const isClickInside = uploadButton.contains(event.target) || 
                                uploadMenu.contains(event.target);
            
            if (!isClickInside && !uploadMenu.classList.contains("hidden")) {
                uploadMenu.classList.add("hidden");
            }
        });

    }); // DOMContentLoaded

    // ============================================================
    // 🔍 Folder Validation Helpers (TEMPO REAL)
    // ============================================================

    function getExistingFolderNames() {
        const folderItems = document.querySelectorAll(
            '[data-kind="folder"]'
        );

        const folderNames = [];

        folderItems.forEach(function (item) {
            const allSpans = item.querySelectorAll("span span");

            if (allSpans.length >= 2) {
                const nameSpan = allSpans[allSpans.length - 1];
                const folderName = nameSpan.textContent.trim();

                if (folderName) {
                    folderNames.push(folderName.toLowerCase());
                }
            }
        });

        return folderNames;
    }

    function folderNameExists(folderName) {
        if (!folderName || !folderName.trim()) {
            return false;
        }

        const existingNames = getExistingFolderNames();
        const normalizedName = folderName.trim().toLowerCase();

        return existingNames.includes(normalizedName);
    }

    function showErrorMessage(errorElement, message) {
        if (!errorElement) return;

        errorElement.textContent = message;
        errorElement.classList.remove("hidden");
    }

    function hideErrorMessage(errorElement) {
        if (!errorElement) return;

        errorElement.textContent = "";
        errorElement.classList.add("hidden");
    }

})(); // IIFE
