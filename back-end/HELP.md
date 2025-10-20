## Como iniciar o back-end (FastAPI)

### Pré-requisitos
- **Python 3.13+** instalado
- **pip** disponível no PATH

Diretório do projeto (exemplo): `C:\Oracle\selenium_cloud\selenium_cloud_ia\back-end`

### 1) (Opcional) Criar o ambiente virtual
- Windows (PowerShell):
```bash
python -m venv venv
```
- Windows (cmd):
```bash
python -m venv venv
```
- Linux/macOS:
```bash
python3 -m venv venv
```

Observação: O repositório já contém uma pasta `venv/`. Você pode usar a existente ou criar uma nova.

### 2) Ativar o ambiente virtual
- Windows (PowerShell):
```bash
.\venv\Scripts\Activate.ps1
```
- Windows (cmd):
```bash
.\venv\Scripts\activate.bat
```
- Linux/macOS:
```bash
source venv/bin/activate
```

### 3) Instalar dependências
```bash
pip install -r requirements.txt
```

### 4) Executar o servidor de desenvolvimento (Uvicorn)
- Forma genérica (funciona em todos os SO):
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
- Usando o executável do venv no Windows:
```bash
.\venv\Scripts\uvicorn.exe app.main:app --reload --host 0.0.0.0 --port 8000
```

### 5) Endpoints úteis
- API: `http://127.0.0.1:8000/`
- Documentação (Swagger): `http://127.0.0.1:8000/docs`
- Documentação alternativa (ReDoc): `http://127.0.0.1:8000/redoc`

### Dicas
- Se o PowerShell bloquear a ativação do venv, execute o PowerShell como Administrador e ajuste a política de execução (com cuidado):
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
- Para desativar o venv:
```bash
deactivate
```
