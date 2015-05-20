__author__ = 'liliane'
from config import db
from jogo import Jogo

class Pessoa(db.Model):
    __tablename__ = 'pessoa'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(50), unique = True)
    senha = db.Column(db.String(50))
    nome = db.Column(db.String(50))
    cpf = db.Column(db.String(11))
    email = db.Column(db.String(50))
    telefone = db.Column(db.String(20))
    endereco = db.Column(db.String(100))
    tipo = db.Column(db.String(50))
    jogos = db.relationship(Jogo)

    __mapper_args__ = {
        'polymorphic_identity':'pessoa',
        'polymorphic_on': tipo
    }

    def __init__(self, login, senha, nome='', cpf='', email='', telefone='', endereco=''):
        self.login = login
        self.senha = senha
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.endereco = endereco