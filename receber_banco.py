import mysql.connector
from mysql.connector import errorcode
from flask_sqlalchemy import SQLAlchemy

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

# cursor.execute("DROP DATABASE IF EXISTS Jogoteca")

# cursor.execute("CREATE DATABASE Jogoteca")

# cursor.execute("Use Jogoteca")



# TABLES = {}
# TABLES['usuarios'] = ('''
#       CREATE TABLE  usuarios (
#           nome varchar(20) not null,
#           nickname varchar(20) not null,
#           senha varchar(100) not null,
#           PRIMARY KEY (nickname)
#           )''')


# TABLES['jogos'] = ('''
#      CREATE TABLE jogos (
#          id int(11) not null auto_increment,
#          nome varchar(50) not null,
#          categoria varchar(40) not null,
#          console varchar(20) not null,
#          PRIMARY KEY (id)
#      )''')


# for tabela_nome in TABLES:
#     tabela_sql = TABLES[tabela_nome]
#     try:
#         print(f'Criando tabela {tabela_nome}...:' , end = '')
#         cursor.execute(tabela_sql)
#         print('OK')
#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#             print('Já existe')
#         else:
#             print(err)
#     else:
#         print('OK')


#CREATE     
#inserindo usuários
# usuarios_sql = 'INSERT INTO usuarios (nome,nickname,senha) VALUES (%s, %s, %s)'
# usuarios = [
#     ("Ramon Candido" , "Ramones" , "7532draivp"),
#     ("Murilo huff" , "Murinelas" , "1234567"),
#     ("Leticia neves" , "Leticines" ,"abcdef")
# ]        
#usando executemany para executar varios parametros de uma vez só
# cursor.executemany(usuarios_sql,usuarios)
#confirmando inserção dos dados no banco de dados
# conexao.commit()
# print("usuarios inseridos com sucesso")

#READ
cursor.execute('select * from usuarios')
print('------------ Usuários: ---------------')
for user in cursor.fetchall():
    print(user[1])

#CREATE     
#inserindo jogos
# jogos_sql = 'INSERT INTO jogos (nome, categoria, console) VALUES (%s , %s, %s)'
# jogos = [
#     ('Tetris', 'Puzzle', 'Atari'),
#     ('Lol', 'MMO','PC'),
#     ('Valorant','Tiro','PC'),
#     ('Doom','RPG',  'PC'),
#     ('GTA V' , 'Tiro' , 'PC')
# ]

#usando executemany para executar varios parametros de uma vez só
# cursor.executemany(jogos_sql , jogos)
#confirmando inserção dos dados no banco de dados
conexao.commit()

#READ
cursor.execute('select * from jogos')
print('------------ Jogos: ---------------')
for jogo in cursor.fetchall():
    print(jogo[1])
    

# #UPDATE DO NOME
# nome = "Gun mayhem"
# id_prod = 1
# jogos_sql = 'UPDATE jogos SET nome = %s WHERE id = %s'
# cursor.execute(jogos_sql, (nome, id_prod))
# conexao.commit()

#UPDATE DA CATEGORIA
# categoria = "Tiro"
# id_prod = 1
# jogos_sql = 'UPDATE jogos SET categoria = %s WHERE id = %s'
# cursor.execute(jogos_sql, (categoria, id_prod))
# conexao.commit()

#UPDATE DO CONSOLE
# console = "PC"
# id_prod = 1
# jogos_sql = 'UPDATE jogos SET console = %s WHERE id = %s'
# cursor.execute(jogos_sql, (console, id_prod))
# conexao.commit()


#UPDATE DO nickname
# nickname = "Ramods"
# nome_usuario = 'Ramon Candido'
# jogos_sql = 'UPDATE usuarios SET nickname = %s WHERE nome = %s'
# cursor.execute(jogos_sql, (nickname, nome_usuario))
# conexao.commit()

#UPDATE DA SENHA
# senha = "9521"
# nome_usuario = 'Ramon Candido'
# jogos_sql = 'UPDATE usuarios SET senha = %s WHERE nome = %s'
# cursor.execute(jogos_sql, (senha, nome_usuario))
# conexao.commit()




cursor.close()
conexao.close()