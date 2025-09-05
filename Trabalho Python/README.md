# Sistema de Controle de Estoque (Flask + SQLite)

## Como rodar
1) Crie um ambiente virtual e instale dependências:
```
python -m venv venv
venv\Scripts\activate   # Windows
# ou: source venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
```

2) Rode o script para criar usuário admin:
```
python create_admin.py
```

3) Inicie a aplicação:
```
python run.py
```
Acesse http://127.0.0.1:5000

Usuário padrão: admin / Senha: admin123 (altere depois)
