from datetime import date

class Viaje:
    def __init__(self):
        self.destino = None
        self.fecha_inicio = None
        self.fecha_fin = None
        self.transporte = None
        self.hotel = None
        self.actividades = []
        self.seguro = False
        self.costo_total = 0.0

    def __str__(self):
        return (
            f"Destino: {self.destino}\n"
            f"Fechas: {self.fecha_inicio} a {self.fecha_fin}\n"
            f"Transporte: {self.transporte}\n"
            f"Hotel: {self.hotel}\n"
            f"Actividades: {', '.join(self.actividades) if self.actividades else 'Ninguna'}\n"
            f"Seguro de viaje: {'Incluido' if self.seguro else 'No incluido'}\n"
            f"Costo total estimado: ${self.costo_total:.2f}"
        )


class ViajeBuilder:
    def __init__(self):
        self.viaje = Viaje()

    def set_destino(self, destino: str):
        self.viaje.destino = destino.title()
        return self

    def set_fechas(self, inicio: date, fin: date):
        if inicio >= fin:
            raise ValueError("La fecha de inicio debe ser anterior a la de fin")
        self.viaje.fecha_inicio = inicio
        self.viaje.fecha_fin = fin
        return self

    def set_transporte(self, transporte: str):
        transporte = transporte.lower()
        if transporte not in ["avión", "bus", "tren", "barco"]:
            raise ValueError(f"Transporte no válido: {transporte}")
        self.viaje.transporte = transporte
        return self

    def set_hotel(self, nombre_hotel: str):
        self.viaje.hotel = nombre_hotel
        return self

    def agregar_actividad(self, actividad: str):
        self.viaje.actividades.append(actividad)
        return self

    def incluir_seguro(self, incluir=True):
        self.viaje.seguro = incluir
        return self

    def build(self):
        if not self.viaje.destino or not self.viaje.fecha_inicio or not self.viaje.transporte:
            raise Exception("Faltan datos esenciales para construir el viaje")
        return self.viaje


class TravelCostCalculator:
    def calcular(self, viaje: Viaje) -> float:
        dias = (viaje.fecha_fin - viaje.fecha_inicio).days
        costo = 0

        transporte_costos = {
            "avión": 600,
            "bus": 100,
            "tren": 250,
            "barco": 400
        }
        costo += transporte_costos.get(viaje.transporte, 0)
        if viaje.hotel:
            costo += dias * 120  # hotel por noche
        costo += len(viaje.actividades) * 50
        if viaje.seguro:
            costo += 75
        return costo

# Uso: construir primero, luego calcular
builder = ViajeBuilder()
viaje = (
    builder.set_destino("Tokio")
           .set_fechas(date(2025, 7, 1), date(2025, 7, 20))
           .set_transporte("avión")
           .set_hotel("Tokyo Plaza Hotel")
           .agregar_actividad("Tour gastronómico")
           .agregar_actividad("Subida al Monte Fuji")
           .incluir_seguro(True)
           .build()
)

# Calcular costo después
calculador = TravelCostCalculator()
viaje.costo_total = calculador.calcular(viaje)

# Mostrar resultado
print(viaje)