from Pessoa import Pessoa

__author__ = 'liliane'
from config import db


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

    def EditarJogoPessoal(self):
        return
    def RemoverJogoPessoal(self):
        return
    def FazerPropostaTroca(self):
        return
    def RespostaPropostaTroca(self):
        return
    def ComprarJogo(self):
        return
    def AvaliarJogo(self):
        return


