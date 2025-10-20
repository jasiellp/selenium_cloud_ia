# 🚀 FastAPI Template com SQLite

## 📦 Instalação
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

## ▶️ Rodar a aplicação
```bash
uvicorn app.main:app --reload
```

## 🔍 Rotas disponíveis
- `GET /` → Status da API  
- `GET /items/` → Lista todos os itens  
- `POST /items/` → Cria um novo item  
  Exemplo de body:
  ```json
  {
    "nome": "Notebook",
    "descricao": "Computador pessoal"
  }
  ```
