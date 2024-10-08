from flask import Flask, render_template, request, redirect , session, flash, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'fuK1duQhhi1Q4a0'

app.config['SQLALCHEMY_DATABASE_URI'] = \
   '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
       SGBD='mysql+mysqlconnector',
       usuario = 'root',
       senha = '7532draivp',
       servidor = '127.0.0.1',
       database = 'Jogoteca'
   )
db = SQLAlchemy(app)

class Jogos(db.Model):
    
    __tablename__ = 'jogos'

    id = db.Column(db.Integer , primary_key = True , autoincrement = True)
    nome = db.Column(db.String(50), nullable = False)
    categoria = db.Column(db.String(40), nullable = False)
    console = db.Column(db.String(20), nullable = False)

    def __repr__(self):
        return '<Name %r>' % self.name
    
class Usuarios(db.Model):
        
    __tablename__ = 'usuarios'

    
    nickname = db.Column(db.String(20) , primary_key = True)
    nome = db.Column(db.String(20), nullable = False)
    senha = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return '<Name %r>' % self.name

    
@app.route('/')
def index():
    lista = Jogos.query.order_by(Jogos.id)
    return render_template('lista.html', titulo = 'jogos', jogos=lista) #indica O PARAMETRO criado no html por boas praticas


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

    jogo = Jogos.query.filter_by(nome=nome).first()

    if jogo:
        flash('Jogo já existe')
        return redirect(url_for('index'))

    novo_jogo = Jogos(nome=nome, categoria=categoria, console=console)
    db.session.add(novo_jogo)
    db.session.commit()
    
    return redirect(url_for('index')) 


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html' , proxima=proxima)



# @app.route('/autenticar' , methods = ['POST',])
# def autenticar():
#     usuario = Usuarios.query.filter_by(nickname=request.form.get['usuário']).first()
#     if usuario:
#         if request.form["Senha"] == usuario.senha:
#             session['usuario_logado'] = usuario.nickname
#             flash(usuario.nickname) , "logado com sucesso"
#             proxima_pagina =  request.form['proxima']
#             return redirect('/')
#     else:
#         flash('Usuário não logado')
#         return redirect('/login')

@app.route('/autenticar' , methods = ['POST',])
def autenticar():
    nickname = request.form.get('usuário')  # Pegando o nickname do formulário
    senha = request.form.get('Senha') 
    usuario = Usuarios.query.filter_by(nickname=nickname).first()
    
    if usuario and usuario.senha == senha:
            session['usuario_logado'] = usuario.nickname
            flash(f"{usuario.nickname} logado com sucesso")
            
            proxima_pagina =  request.form.get('proxima')
            return redirect(proxima_pagina or '/')
    else:
        flash('Usuário ou senha inválidos')
        return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect('/')

app.run(debug = True)  
    
 