# ===============================
# 1️⃣ Imagem base
# ===============================
FROM python:3.12-slim

# ===============================
# 2️⃣ Configuração de ambiente
# ===============================
WORKDIR /code
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

# ===============================
# 3️⃣ Dependências do sistema
# ===============================
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-traditional \
    bash \
    && rm -rf /var/lib/apt/lists/*

# ===============================
# 4️⃣ Instalar dependências Python
# ===============================
COPY requirements-dev.txt /code/
RUN pip install --upgrade pip && pip install -r requirements-dev.txt

# ===============================
# 5️⃣ Copiar código do projeto
# ===============================
COPY . /code/

# ===============================
# 6️⃣ (REMOVIDO) Ajustes de produção
# = NÃO CRIAR USUÁRIO appuser =
# = NÃO MUDAR PARA USER appuser =
# ===============================

# ===============================
# 7️⃣ Porta exposta
# ===============================
EXPOSE 8000

# ===============================
# 8️⃣ Comando padrão
# ===============================
CMD ["bash"]
