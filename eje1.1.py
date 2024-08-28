class Moto:
    def __init__(self,marca,referencia,color):
        self.marca= marca
        self.referencia= referencia
        self.color= color


ktm250= Moto("Duke","Ktm250","Naranja")
ns200= Moto("Pulsa","Ns 200","Negro")
print(type(ktm250))
print(type(ns200))


print(ktm250.marca, ktm250.referencia, ktm250.color)
print(ns200.marca, ns200.referencia, ns200.color)

