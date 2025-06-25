# Clase base
class Bebida:
    def calcular_precio(self):
        return 1.00  # Café solo

# Clase decoradora base
class DecoradorBebida(Bebida):
    def __init__(self, bebida):
        self.bebida = bebida

    def calcular_precio(self):
        return self.bebida.calcular_precio()

# Decoradores
class Leche(DecoradorBebida):
    def calcular_precio(self):
        return self.bebida.calcular_precio() + 0.50

class LecheSoya(DecoradorBebida):
    def calcular_precio(self):
        return self.bebida.calcular_precio() + 0.75

class LecheCoco(DecoradorBebida):
    def calcular_precio(self):
        return self.bebida.calcular_precio() + 1.00

class Canela(DecoradorBebida):
    def calcular_precio(self):
        return self.bebida.calcular_precio() + 0.25

class CremaBatida(DecoradorBebida):
    def calcular_precio(self):
        return self.bebida.calcular_precio() + 1.50

class Saborizante(DecoradorBebida):
    def calcular_precio(self):
        return self.bebida.calcular_precio() + 1.25

class Mediana(DecoradorBebida):
    def calcular_precio(self):
        return self.bebida.calcular_precio() + 1.00

class Grande(DecoradorBebida):
    def calcular_precio(self):
        return self.bebida.calcular_precio() + 2.00

bebida = Bebida()
bebida = Leche(bebida)
bebida = Canela(bebida)
bebida = CremaBatida(bebida)
bebida = Saborizante(bebida)
bebida = Saborizante(bebida)  # Doble saborizante
bebida = Grande(bebida)

print(f"Precio total: ${bebida.calcular_precio():.2f}")
