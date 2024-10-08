import mysql.connector
from mysql.connector import errorcode
from flask import session, request, redirect


print("Testando conexão...")

try:
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '7532draivp',
        database = 'Jogoteca'
    )
    print("conexão bem-sucedida")
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Erro no usuario ou senha")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('Banco de dados nao existe')
    else:
        print(err)
        
        
cursor = conexao.cursor()
def carregar_jogos_do_banco(usuario_id):
    cursor.execute("SELECT nome, categoria, console FROM jogos WHERE usuario_id = %s", (usuario_id,))
    jogos = cursor.fetchall()
    cursor.close()
    conexao.close()
    return jogos



def home():
    # Verifica se o usuário está logado e tem sessão
    if 'usuario_id' in session:
        usuario_id = session['usuario_id']
        if 'jogos' not in session:
            # Carrega jogos do banco de dados apenas uma vez, ao iniciar a sessão
            session['jogos'] = carregar_jogos_do_banco(usuario_id)
        jogos = session['jogos']
        return f"Lista de jogos do usuário: {jogos}"
    else:
        return "Usuário não logado."



TABLES = {}
TABLES['jogos'] = ('''
     CREATE TABLE jogos (
         id int(11) not null auto_increment,
         nome varchar(50) not null,
         categoria varchar(40) not null,
         console varchar(20) not null,
         PRIMARY KEY (id)
     )''')

TABLES['usuarios'] = ('''
      CREATE TABLE  usuarios (
          nome varchar(20) not null,
          nickname varchar(20) not null,
          senha varchar(100) not null,
          PRIMARY KEY (nickname)
          )''')

for tabela_nome in TABLES:
    tabela_sql = TABLES[tabela_nome]
    try:
        print(f'Criando tabela {tabela_nome}...: ' , end = '')
        cursor.execute(tabela_sql)
        print('OK')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('Já existe')
        else:
            print(err)
    else:
        print('OK')
        
#inserindo usuários
usuario_sql = 'INSERT INTO usuarios (nome,nickname,senha) VALUES (%s, %s, %s)'
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
jogos_sql = 'INSERT INTO jogos (nome, categoria, console) VALUES (%s , %s, %s)'
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