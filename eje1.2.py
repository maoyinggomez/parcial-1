class Computador:
    def __init__(self,marca,referencia,color):
        self.marca= marca
        self.referencia= referencia
        self.color= color


d3520= Computador("Dell","d3520","Plateado")
pavilion= Computador("Hp","pavilion","negro")
print(type(d3520))
print(type(pavilion))


print(d3520.marca, d3520.referencia, d3520.color)
print(pavilion.marca, pavilion.referencia, pavilion.color)
