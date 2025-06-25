from abc import ABC, abstractmethod

# Clases abstractas
class Vehiculo(ABC):
    @abstractmethod
    def mostrar(self):
        pass

class Motor(ABC):
    @abstractmethod
    def usar(self):
        pass

class FabricaVehiculo(ABC):
    @abstractmethod
    def crear_vehiculo(self) -> Vehiculo:
        pass

    @abstractmethod
    def crear_motor(self) -> Motor:
        pass

# Fábrica terrestre
class Carro(Vehiculo):
    def mostrar(self):
        print("Creando vehículo terrestre: Carro")

class MotorCombustion(Motor):
    def usar(self):
        print("Usando motor: Motor de combustión")

class FabricaTerrestre(FabricaVehiculo):
    def crear_vehiculo(self) -> Vehiculo:
        return Carro()

    def crear_motor(self) -> Motor:
        return MotorCombustion()

# Fábrica acuática
class Lancha(Vehiculo):
    def mostrar(self):
        print("Creando vehículo acuático: Lancha")

class MotorNautico(Motor):
    def usar(self):
        print("Usando motor: Motor náutico")

class FabricaAcuatica(FabricaVehiculo):
    def crear_vehiculo(self) -> Vehiculo:
        return Lancha()

    def crear_motor(self) -> Motor:
        return MotorNautico()

# Cliente
def renderizar_fabrica(fabrica: FabricaVehiculo):
    vehiculo = fabrica.crear_vehiculo()
    motor = fabrica.crear_motor()
    vehiculo.mostrar()
    motor.usar()

# Ejecución
print("=== Fábrica Terrestre ===")
renderizar_fabrica(FabricaTerrestre())

print("\n=== Fábrica Acuática ===")
renderizar_fabrica(FabricaAcuatica())
