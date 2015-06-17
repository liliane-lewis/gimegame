import config
import jogo
import Pessoa
import Cliente
import Funcionario
import Pedido


config.db.drop_all()
config.db.create_all()
#config.db.create_table(funcionario)

f1 = Funcionario.Funcionario('admin','senhaAdmin','Admin')

p1 = Cliente.Cliente('liliane','senhateste','Liliane')
p2 = Cliente.Cliente('andre','senhateste','Andre')
p3 = Cliente.Cliente('arthur','senhateste','Arthur')
p4 = Cliente.Cliente('victor','senhateste','Victor')

config.db.session.add(f1)
config.db.session.add(p1)
config.db.session.add(p2)
config.db.session.add(p3)
config.db.session.add(p4)
config.db.session.commit()

print p1.id


j1 = jogo.Jogo(p1.id,'Sonic','Arcade','Megadrive',1990, 'Troca','0')
j2 = jogo.Jogo(p1.id,'The Legend of Zelda: The Ocarina of Time','Arcade','Nintendo',1990, 'Venda', '52,00')
j3 = jogo.Jogo(p2.id,'Super Mario Kart','Arcade','Wii',1990,'Venda', '100,50')
j4 = jogo.Jogo(p2.id,'Doom','Arcade','PC',1990, 'Troca','0')
j5 = jogo.Jogo(p2.id,'Street Fighter','Arcade','Super Nintendo',1990, 'Troca','0')

#j2 = jogo.Jogo(p1.id,'Pacman','Arcade','Atari',1980)
config.db.session.add(j1)
config.db.session.add(j2)
config.db.session.add(j3)
config.db.session.add(j4)
config.db.session.add(j5)
config.db.session.commit()
