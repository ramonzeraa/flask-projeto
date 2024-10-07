import mysql.connector
from mysql.connector import errorcode


print("Testando conexão...")

try:
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '7532draivp',
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Erro no usuario ou senha")
    else:
        print('conexão bem sucedida')
        
cursor = conexao.cursor()

cursor.execute("DROP DATABASE IF EXISTS Jogoteca;")

cursor.execute("CREATE DATABASE Jogoteca;")

cursor.execute("USE Jogoteca;")

        
