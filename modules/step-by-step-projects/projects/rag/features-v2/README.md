# RAG Project

> **Tutorial de como este projeto foi desenvolvido, passo a passo.**

## Conteúdo

 - [`Adicionando .editorconfig e .gitignore`](features/feature001)
 - [`Iniciando o projeto com "poetry init"`](features/feature002)
 - [`Instalando e configurando o Ruff`](features/feature003)
 - [`Instalando e configurando o pre-commit`](features/feature004)
 - [`Criando o container com PostgreSQL (db)`](features/feature005)
 - [`Criando o container com Redis (redis_cache)`](features/feature006)
 - [`Instalando/Configurando/Exportando o Django + Uvicorn`](features/feature007)
 - [`Script de inicialização do serviço web (entrypoint.sh)`](features/feature008)
 - [`Criando o Dockerfile do serviço web`](features/feature009)
 - [`Configurando o Django para reconhecer o PostgreSQL (+ .env) como Banco de Dados`](features/feature010)
 - [`Criando o docker compose para o container web`](features/feature011)
 - [`Criando o container Nginx (nginx)`](features/feature012)
 - [`Criando App "users"`](features/feature013)
 - [`Criando a landing page da aplicação (base.html + index.html)`](features/feature014)
 - [`Criando a página de cadastro (create-account.html + DB Commands)`](features/feature015)
 - [`Criando a sessão de login/logout + página home.html`](features/feature016)
 - [`Instalando e preparando o django-allauth para fazer logins sociais`](features/feature017)
 - [`Pegando as credenciais (chaves) do Google e GitHub`](features/feature018)
 - [`Criando um super usuário e logins sociais automaticamente`](features/feature019)
 - [`Linkando os botões de login social`](features/feature020)
 - [`Reescrevendo as mensagens do Django Allauth`](features/feature021)
 - [`Criando o app "workspace"`](features/feature022)
 - [`Mapeando a rota home/ com a workspace/`](features/feature023)
 - [`Modelando o workspace: Pastas (Folders) e Arquivos (Files)`](features/feature024)
 - [`Customizando os formulários FolderForm e FileForm`](features/feature025)
 - [`Atualizando a view (ação) para exibir as pastas e arquivos`](features/feature026)
 - [`Refatorando a exibição das pastas e arquivos (Clicks, Houver, Select, Escape, Click Outside)`](features/feature027)
 - [`Adicionando o botão (➕ Nova Pasta)`](features/feature028)
 - [`Refatorando o modal para abrir selecionando o campo de digitação`](features/feature029)
 - [`Refatorando para quando o usuário digitar um nome para uma pasta existente`](features/feature030)
 - [`Implementando a inserção de arquivos (📤 Fazer Upload | Arquivo/Pasta)`](features/feature031)
 - [`Implementando a inserção de pasta`](features/feature032)
 - [`Implementando a exclusão de um arquivo (soft delete)`](features/feature033)
 - [`Implementando a exclusão de um pasta (soft delete)`](features/feature034)
 - [`Implementando a renomeação de pastas (✏ Renomear)`](features/feature035)
 - [`Implementando a renomeação de arquivos (✏ Renomear)`](features/feature036)
 - [`Implementando a funcionalidade de mover um arquivo ou pasta (Drag and Drop)`](features/feature037)
 - [`Refatorando static/workspace/js/workspace_home.js e workspace/views.py (Removendo códigos duplicados)`](features/feature038)
 - [`Refatorando as mensagens de erro`](features/feature039)
 - [`Descobrindo e mapeando os arquivos do app workspace`](features/feature040)
 - [`Extraindo textos por tipo de arquivo`](features/feature041)
 - [`Criando chunking de textos para RAG`](features/feature042)

---

**Rodrigo** **L**eite da **S**ilva - **rodirgols89**
