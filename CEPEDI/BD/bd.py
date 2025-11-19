import mysql.connector

# 1. Conectar ao banco
conexao = mysql.connector.connect(
    	   host='localhost',       # ou IP do servidor
    	   user='root',     # ex: 'root'
    	   password='',   # ex: 'admin123'
    	   database='teste'
)

# Cria o objeto responsável por executar comandos SQL dentro dessa conexão.
cursor = conexao.cursor()

# 2. Criar tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Aluno (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        idade INT
    );
''')
# 3. Inserir dados
cursor.execute("INSERT INTO Aluno (nome, idade) VALUES (%s, %s)", ('Carlos', 23))
conexao.commit()

# 4. Consultar dados
cursor.execute("SELECT * FROM Aluno")
for linha in cursor.fetchall():
    print(linha)

# 5. Fechar a conexão
cursor.close()
conexao.close()


