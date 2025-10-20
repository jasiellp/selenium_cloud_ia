# 🚀 FastAPI Template com SQLite

## 📦 Instalação
```bash
python -m venv venv
```
```bash
.\venv\Scripts\activate
```
```bash
pip install -r requirements.txt
```

## ▶️ Rodar a aplicação
```bash
uvicorn app.main:app --reload
```

## 🔍 Rotas disponíveis
- http://127.0.0.1:8000/docs
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
