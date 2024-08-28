class Carro:
    def __init__(self,marca,referencia,color):
        self.marca= marca
        self.referencia= referencia
        self.color= color


versa= Carro("Nissan","Versa","Blanco")
sentra= Carro("Nissan","Sentra","negro")
print(type(versa))
print(type(sentra))


print(versa.marca, versa.referencia, versa.color)
print(sentra.marca, sentra.referencia, sentra.color)