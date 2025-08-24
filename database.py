# --- database.py ---

import mysql.connector
from mysql.connector import Error

def criar_conexao():
    """Cria e retorna uma conexão com o banco de dados MySQL."""
    try:
        conexao = mysql.connector.connect(
            host='localhost',       # Ou o IP do seu servidor de banco de dados
            database='homogenizacao_db', # O nome do banco que criamos
            user='root',            # Seu usuário do MySQL
            password=''    
        )
        if conexao.is_connected():
            print("Conexão com o MySQL bem-sucedida!")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None