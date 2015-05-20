__author__ = 'liliane'
from config import db

class Funcionario(Pessoa,db.Model):
    __tablename__ = 'funcionario'
    id = db.Column(db.Integer,  db.ForeignKey('pessoa.id'), primary_key=True)
    jogos = db.Column(db.Integer)
    avaliacao = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity':'funcionario',
    }

    def __init__(self):
        return

    def ValidarNovoJogo(self):
        return
    def ValidarOriginalidadeJogo(self):
        return
    def GerenciarCatalogoGeral(self):
        return
    def GerenciarLoja(self):
        return
    def GerenciarPedidos(self):
        return
    def ConfirmarPagamentos(self):
        return
    def EntragarProduto(self):
        return