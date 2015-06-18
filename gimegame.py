# coding: utf-8

from flask import Flask, render_template,request,session,flash,redirect,url_for
from flask.ext.sqlalchemy import SQLAlchemy
from config import app, db

from jogo import Jogo
from Pessoa import Pessoa
from Cliente import Cliente
from Funcionario import Funcionario
from Pedido import Pedido

@app.route('/catalogo')
def exibir_jogos():
    ### Alteracao para mostrar apenas os jogos disponíveis de outros usuários
    usuario = Pessoa.query.filter(Pessoa.login == session['login']).first()
    jogos = Jogo.query.filter(Jogo.proprietario != usuario.id).all()
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

@app.route('/comprar/<int:id>')
def comprar(id):
    jogo = Jogo.query.get(id)
    cliente = Cliente.query.filter(Cliente.login == session['login']).first()
    cliente.FazerPropostaTroca(jogo)
    return render_template('catalogo.html')


@app.route('/trocar/<int:id>')
def trocar(id):
    jogo = Jogo.query.get(id)
    cliente = Cliente.query.filter(Cliente.login == session['login']).first()
    cliente.FazerPropostaTroca(jogo)
    return render_template('catalogo.html')

@app.route('/propostas')
def minhasPropostas():
    usuario = Cliente.query.filter(Cliente.login == session['login']).first()
    propostas = pesquisa_pedidos_usuario(usuario.id)
    como_cliente = propostas[0]
    como_vendedor = propostas[1]
    return render_template('propostas.html',como_cliente=como_cliente, como_vendedor=como_vendedor)

@app.route('/aceitarProposta/<int:id>')
def aceitarProposta(id):
    proposta = Pedido.query.filter(Pedido.id == id).first()
    jogo = Jogo.query.filter(Jogo.id == proposta.item).first()
    vendedor = Cliente.query.filter(Cliente.login == session['login']
    and Cliente.id == proposta.vendedor).first()
    vendedor.aceitarProposta(jogo, proposta)
    return render_template('propostas.html')


@app.route('/recusarProposta/<int:id>')
def recusarProposta(id):
    proposta = Pedido.query.filter(Pedido.id == id).first()
    db.session.delete(proposta)
    db.session.commit()
    return render_template('propostas.html')

@app.route('/adicionarjogo', methods=['GET', 'POST'])
def adicionar_jogo():
    if request.method == 'POST':
        usuario = Pessoa.query.filter(Pessoa.login == session['login']).first()
        jogo = Jogo(usuario.id, request.form['nome'], request.form['genero'], request.form['console'], request.form['ano'], request.form['operacao'], request.form['valor'])
        usuario.IncluirJogosPessoal(jogo)
        return redirect('meusjogos')
    return render_template('adicionarjogo.html')

@app.route('/editarjogo/<int:id>', methods=['GET', 'POST'])
def editarjogo(id):
    jogo=Jogo.query.get(id)
    usuario = Pessoa.query.filter(Pessoa.login == session['login']).first()
    if request.method == 'POST':
        jogo.nome = request.form['nome']
        jogo.genero = request.form['genero']
        jogo.console = request.form['console']
        jogo.ano = request.form['ano']
        jogo.operacao = request.form['operacao']
        jogo.valor = request.form['valor']
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
        jogo.operacao = request.form['operacao']
        jogo.valor = request.form['valor']
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

@app.route('/cadastrarcliente', methods=['GET', 'POST'])
def cadastrar_cliente():
    if request.method == 'POST':
        #usuario = Pessoa.query.filter(Pessoa.login == session['login']).first()
        cliente = Cliente(request.form['login'], request.form['senha'], request.form['nome'], request.form['cpf'], \
                          request.form['email'], request.form['telefone'], request.form['endereco'] )
        cliente.CadastrarUsuario(cliente)
        return redirect('home')
    return render_template('cadastrarcliente.html')

@app.route('/cadastrarfuncionario', methods=['GET', 'POST'])
def cadastrar_funcionario():
    if request.method == 'POST':
        #usuario = Pessoa.query.filter(Pessoa.login == session['login']).first()
        funcionario = Funcionario(request.form['login'], request.form['senha'], request.form['nome'], request.form['cpf'], \
                          request.form['email'], request.form['telefone'], request.form['endereco'] )
        funcionario.CadastrarFuncionario(funcionario)
        return redirect('home')
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

def pesquisa_pedidos_usuario(id):
    pedidos_como_cliente = Pedido.query.filter(Pedido.cliente == id).all()
    pedidos_como_vendedor = Pedido.query.filter(Pedido.vendedor == id).all()
    return (pedidos_como_cliente, pedidos_como_vendedor)

if __name__ == '__main__':
    app.run()