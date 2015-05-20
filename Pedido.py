__author__ = 'liliane'

class Pedido:
    def __init__(self, id, tipo, status, vendedor, cliente, itens, valor):
        self.id = id
        self.tipo = tipo
        self.status = status
        self.vendedor = vendedor
        self.cliente = cliente
        self.itens = itens
        self.valor = valor
