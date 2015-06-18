__author__ = 'liliane'

from config import db

class Pedido(db.Model):
	__tablename__ = 'pedidos'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	tipo = db.Column(db.String(50))
	status = db.Column(db.String(50))
	vendedor = db.Column(db.Integer, db.ForeignKey('pessoa.id'))
	cliente = db.Column(db.Integer, db.ForeignKey('pessoa.id'))
	item = db.Column(db.Integer, db.ForeignKey('jogos.id'))
	valor = db.Column(db.Integer)


	def __init__(self, tipo, status, vendedor, cliente, item, valor):
		self.tipo = tipo
		self.status = status
		self.vendedor = vendedor
		self.cliente = cliente
		self.item = item
		self.valor = valor