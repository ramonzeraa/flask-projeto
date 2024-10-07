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

TABLES = {}
TABLES['Jogos'] = ('''
     CREATE TABLE Jogos (
         id int(11) not null auto_increment,
         nome varchar(50) not null,
         categoria varchar(40) not null,
         console varchar(20) not null,
         PRIMARY KEY (id)
     )''')

TABLES['Usuarios'] = ('''
      CREATE TABLE  Usuarios (
          nome varchar(20) not null,
          nickname varchar(20) not null,
          senha varchar(100) not null,
          PRIMARY KEY (nickname)
          )''')

for tabela_nome in TABLES:
    tabela_sql = TABLES[tabela_nome]
    try:
        print(f'Criando tabela {tabela_nome}' , end = '')
        cursor.execute(tabela_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('Já existe')
        else:
            print(err)
    else:
        print('OK')
        
#inserindo usuários
usuario_sql = 'INSERT INTO Usuarios (nome,nickname,senha) VALUES (%s, %s, %s)'
Usuarios = [
    ("Ramon Candido" , "Ramones" , "7532draivp"),
    ("Murilo huff" , "Murinelas" , "1234567"),
    ("Leticia neves" , "Leticines" ,"abcdef")
]        
cursor.executemany(usuario_sql,Usuarios)

cursor.execute('select * from Usuarios')
print('------------ Usuários: ---------------')
for user in cursor.fetchall():
    print(user[1])
    
#inserindo jogos
jogos_sql = 'INSERT INTO Jogos (nome, categoria, console) VALUES (%s , %s, %s)'
jogos = [
    ('Tetris', 'Puzzle', 'Atari'),
    ('Lol', 'MMO','PC'),
    ('Valorant','Tiro','PC'),
    ('Doom','RPG',  'PC')
]

cursor.executemany(jogos_sql , jogos)
cursor.execute('select * from Jogos')
print('------------ Jogos: ---------------')
for jogo in cursor.fetchall():
    print(jogo[1])