# coding: utf-8

from flask import Flask, render_template,request,session,flash,redirect,url_for
from flask.ext.sqlalchemy import SQLAlchemy
from config import app, db

from jogo import Jogo
from Pessoa import Pessoa
from Cliente import Cliente
from Funcionario import Funcionario

#@app.teardown_appcontext
#def shutdown_session(exception=None):
#    db_session.remove()

#def conectar_bd():
#    return sqlite3.connect(app.config['DATABASE'])

#def criar_bd():
#    with closing(conectar_bd()) as bd:
#        with app.open_resource('db/esquema.sql') as sql:
#            bd.cursor().executescript(sql.read())
#        bd.commit()
#@app.before_request
#def pre_requisicao():
#    g.bd = conectar_bd()

#@app.teardown_request
#def encerrar_requisicao(exception):
#    g.bd.close()

@app.route('/catalogo')
def exibir_jogos():
    jogos = Jogo.query.all()
    return render_template('catalogo.html', jogos=jogos)

@app.route('/gerenciarcatalogo')
def gerenciar_jogos():
    jogos = Jogo.query.all()
    return render_template('gerenciarcatalogo.html', jogos=jogos)


@app.route('/meusjogos')
def exibir_meus_jogos():
    usuario = Pessoa.query.filter(Pessoa.login == session['login']).first()
    meus_jogos = pesquisa_jogos_usuario(usuario.id)
    return render_template('meusjogos.html', meus_jogos=meus_jogos)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/comprar')
def comprar():
    return 'A ser implementado'

@app.route('/editarjogo/<int:id>', methods=['GET', 'POST'])
def editarjogo(id):
    jogo=Jogo.query.get(id)
    usuario = Pessoa.query.filter(Pessoa.login == session['login']).first()
    if request.method == 'POST':
        jogo.nome = request.form['nome']
        jogo.genero = request.form['genero']
        jogo.console = request.form['console']
        jogo.ano = request.form['ano']
        usuario.EditarJogoPessoal(jogo)
        return redirect('meusjogos')

    return render_template('editarjogo.html', meujogo=jogo)

@app.route('/editarcatalogo/<int:id>', methods=['GET', 'POST'])
def editarcatalogo(id):
    jogo=Jogo.query.get(id)
    funcionario = Pessoa.query.filter(Pessoa.login == session['login']).first()
    if request.method == 'POST':
        jogo.nome = request.form['nome']
        jogo.genero = request.form['genero']
        jogo.console = request.form['console']
        jogo.ano = request.form['ano']
        funcionario.EditarCatalogo(jogo)
        return redirect('gerenciarcatalogo')

    return render_template('editarcatalogo.html', jogo=jogo)


@app.route('/removerjogo/<int:id>', methods=['GET'])
def removerjogo(id):
    jogo=Jogo.query.get(id)
    usuario = Pessoa.query.filter(Pessoa.login == session['login']).first()
    usuario.RemoverJogoPessoal(jogo)
    return redirect('meusjogos')


@app.route('/removercatalogo/<int:id>', methods=['GET'])
def removercatalogo(id):
    jogo=Jogo.query.get(id)
    funcionario = Pessoa.query.filter(Pessoa.login == session['login']).first()
    funcionario.RemoverCatalogo(jogo)
    return redirect('gerenciarcatalogo')


    #return render_template('editarjogo.html', meujogo=jogo)


@app.route('/adicionarjogo', methods=['GET', 'POST'])
def adicionar_jogo():
    if request.method == 'POST':
        usuario = Pessoa.query.filter(Pessoa.login == session['login']).first()
        jogo = Jogo(usuario.id, request.form['nome'], request.form['genero'], request.form['console'], request.form['ano'])
        usuario.IncluirJogosPessoal(jogo)
        return redirect('meusjogos')
    return render_template('adicionarjogo.html')

@app.route('/cadastrarcliente', methods=['GET', 'POST'])
def cadastrar_cliente():
    if request.method == 'POST':
        #usuario = Pessoa.query.filter(Pessoa.login == session['login']).first()
        cliente = Cliente(request.form['login'], request.form['senha'], request.form['nome'], request.form['cpf'], \
                          request.form['email'], request.form['telefone'], request.form['endereco'] )
        cliente.CadastrarUsuario(cliente)
        return redirect('meusjogos')
    return render_template('cadastrarcliente.html')

@app.route('/cadastrarfuncionario', methods=['GET', 'POST'])
def cadastrar_funcionario():
    if request.method == 'POST':
        #usuario = Pessoa.query.filter(Pessoa.login == session['login']).first()
        funcionario = Funcionario(request.form['login'], request.form['senha'], request.form['nome'], request.form['cpf'], \
                          request.form['email'], request.form['telefone'], request.form['endereco'] )
        funcionario.CadastrarFuncionario(funcionario)
        return redirect('catalogo')
    return render_template('cadastrarfuncionario.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':

        usuario = Pessoa.query.filter(Pessoa.login == request.form['username'], Pessoa.senha == request.form['password']).first()

        admin = Funcionario.query.filter(Funcionario.login == request.form['username']).first()


        #print(request.form['username'])
        #print(request.form['password'])
        #print(usuario)
        if not usuario:
            error = 'Usuário inválido ou senha inválida'
            flash('Usuario invalido ou senha invalida')
        else:

            session['logado'] = True
            session['login'] = request.form['username']
            if admin:
                session['admin'] = True
            else:
                session['admin'] = False
            return redirect(url_for('home'))

            flash('Login OK')
            return redirect(url_for('home'))
    return render_template('login.html', erro=erro)

@app.route('/logout')
def logout():
    session.pop('logado', None)
    flash('Logout OK')
    return redirect(url_for('login'))

def pesquisa_jogos_usuario(id):
    return Jogo.query.filter(Jogo.proprietario == id).all()


if __name__ == '__main__':
    app.run()