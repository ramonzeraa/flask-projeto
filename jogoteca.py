from flask import Flask, render_template, request, redirect , session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'fuK1duQhhi1Q4a0'


app.config('SQLALCHEMY_DATABASE_URI') = \
    '{SGBD} : //{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = '7532draivp',
        servidor = 'localhost',
        database = 'jogoteca'
    )
    
db = SQLAlchemy(app)
class Jogos(db.nmodel):
    id = db.Column(db.Integer, primary_key = True, auto_increment=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(35), nullable=False)
    console = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return '<Name %r' % self.name
    
class Jogos(db.nmodel):
    nickname = db.Column(db.String(8), primary_key = True, auto_increment=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return '<Name %r' % self.name
    
    
    
class Jogo:
    def __init__(self,nome,categoria,console) -> None:
        self.nome = nome
        self.categoria = categoria
        self.console = console
       
jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('Lol', 'MMO','PC') 
jogo3 = Jogo('Valorant','Tiro','PC')
jogo4 = Jogo('Doom','RPG',  'PC')
lista = [jogo1,jogo2,jogo3,jogo4]

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha
        
usuario1 = Usuario("Ramon Candido" , "Ramones" , "7532draivp")
usuario2 = Usuario("Murilo huff" , "Murinelas" , "1234567")
usuario3 = Usuario("Leticia neves" , "Leticines" ,"abcdef")

usuarios = { usuario1.nickname : usuario1,
            usuario2.nickname : usuario2, 
            usuario3.nickname : usuario3 }

@app.route('/')
def index():
    return render_template('lista.html', titulo = 'Jogos', jogos = lista) #indica O PARAMETRO criado no html por boas praticas


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session ['usuario_logado'] == None:
        return redirect('/login?proxima=novo')#query string
    return render_template('novo.html', titulo = 'Novo Jogo')


@app.route('/criar' , methods = ['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome ,categoria, console)
    lista.append(jogo)
    return redirect('/')


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html' , proxima = proxima)



@app.route('/autenticar' , methods = ['POST',])
def autenticar():
    if  request.form['usuário'] in usuarios:
        usuario = usuarios[request.form['usuário']]
        if request.form["Senha"] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname) , "logado com sucesso"
            proxima_pagina =  request.form['proxima']
            return redirect('/')
    else:
        flash('Usuário não logado')
        return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect('/')

app.run(debug = True)  
    
