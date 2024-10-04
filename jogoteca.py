from flask import Flask, render_template, request, redirect , session, flash

app = Flask(__name__)
app.secret_key = 'fuK1duQhhi1Q4a0'

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

@app.route('/')
def index():
    return render_template('lista.html', titulo = 'Jogos', jogos = lista) #indica O PARAMETRO criado no html por boas praticas

@app.route('/novo')
def novo():
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
    return render_template('login.html')


@app.route('/autenticar' , methods = ['POST',])
def autenticar():
    if 'teste' == request.form['Senha']:
        session['usuario_logado'] = request.form['usuário']
        flash(session['usuario_logado'] + ' logado com sucesso')
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
    
