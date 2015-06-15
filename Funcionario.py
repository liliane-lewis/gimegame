from Pessoa import Pessoa
from config import db

#class Funcionario(Pessoa,db.Model):
class Funcionario(Pessoa):
    __tablename__ = 'funcionario'
    id = db.Column(db.Integer,  db.ForeignKey('pessoa.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity':'funcionario',
    }

    def __init__(self, login, senha, nome='', cpf='', email='', telefone='', endereco=''):
        self.login = login
        self.senha = senha
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def CadastrarFuncionario(self,Cliente):
        db.session.add(Cliente)
        db.session.commit()

    def ValidarNovoJogo(self):
        return
    def ValidarOriginalidadeJogo(self):
        return

    def EditarCatalogo(self, jogo):
        db.session.commit()
        return
    def RemoverCatalogo(self, jogo):
        db.session.delete(jogo)
        db.session.commit()
        return

 #   def GerenciarCatalogoGeral(self):
 #       return
    def GerenciarLoja(self):
        return
    def GerenciarPedidos(self):
        return
    def ConfirmarPagamentos(self):
        return
    def EntragarProduto(self):
        return