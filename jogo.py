__author__ = 'liliane'
from config import db

class Jogo(db.Model):
    __tablename__ = 'jogos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    proprietario = db.Column(db.Integer,  db.ForeignKey('pessoa.id'))
    nome = db.Column(db.String(50))
    genero = db.Column(db.String(50))
    console = db.Column(db.String(50))
    ano = db.Column(db.Integer)

    def __init__(self, proprietario, nome, genero='', console='', ano=0):
        self.proprietario = proprietario
        self.nome = nome
        self.genero = genero
        self.console = console
        self.ano = ano
