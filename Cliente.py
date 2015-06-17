from Pessoa import Pessoa
from config import db
from Pedido import *

class Cliente(Pessoa):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer,  db.ForeignKey('pessoa.id'), primary_key=True)
    avaliacao = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'cliente'
    }

    def __init__(self, login, senha, nome='', cpf='', email='', telefone='', endereco='', avaliacao=''):
        self.login = login
        self.senha = senha
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.avaliacao = avaliacao

    def CadastrarUsuario(self, Cliente):
        db.session.add(Cliente)
        db.session.commit()
        return

    def GerenciarJogos(self):
        return
    def CadastrarNovoJogo(self):
        return

    def IncluirJogosPessoal(self, jogo):
        db.session.add(jogo)
        db.session.commit()
        return

    def EditarJogoPessoal(self, jogo):
        db.session.commit()
        return

    def RemoverJogoPessoal(self, jogo):
        db.session.delete(jogo)
        db.session.commit()
        return

    def FazerPropostaTroca(self, jogo):
        tipo = jogo.operacao
        status = 'disponivel'
        vendedor = jogo.proprietario
        cliente = self.id
        itens = 1
        valor = jogo.valor

        pedido = Pedido(tipo, status, vendedor, cliente, itens, valor)

        db.session.add(pedido)
        db.session.commit()
        return


    def RespostaPropostaTroca(self):
        return
    def ComprarJogo(self):
        return
    def AvaliarJogo(self):
        return


