# Exercício Proposto
# Crie um bd com a tabela Livro (id, titulo, autor, ano)
# Insira pelo menos 2 livros
# Mostre todos os livros cadastrados

import mysql.connector

# Conexão com o banco
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='minhasenha',
    database='teste'
)

cursor = conexao.cursor()

# Cria a tabela se não existir (com restrição UNIQUE para evitar duplicatas)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS livro (
        id INT AUTO_INCREMENT PRIMARY KEY,
        titulo VARCHAR(100) NOT NULL,
        autor VARCHAR(100) NOT NULL,
        ano INT,
        UNIQUE (titulo, autor)
    )
''')

# Lista de livros
livros = [
    ('A morte como despertar', 'Desconhecido', 2020),
    ('Diário de Anny Frank', 'Anny Frank', 2000)
]

# Tenta inserir os livros (ignora se já existirem)
for livro in livros:
    try:
        cursor.execute(
            "INSERT INTO livro (titulo, autor, ano) VALUES (%s, %s, %s)",
            livro
        )
    except mysql.connector.errors.IntegrityError:
        # Essa exceção acontece se o livro já estiver no banco (por causa do UNIQUE)
        pass

conexao.commit()

# Exibe todos os livros cadastrados
cursor.execute("SELECT * FROM livro")
print("\nLivros cadastrados:")
for linha in cursor.fetchall():
    print(f"ID: {linha[0]} | Título: {linha[1]} | Autor: {linha[2]} | Ano: {linha[3]}")

# Fecha tudo
cursor.close()
conexao.close()
