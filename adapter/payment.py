import json
from abc import ABC, abstractmethod

# Interfaz 
class ProcesadorPago(ABC):
    @abstractmethod
    def procesar_pago(self, json_data):
        pass

# Clase moderna
class PagoModerno(ProcesadorPago):
    def procesar_pago(self, json_data):
        data = json.loads(json_data)
        print(f"[MODERNO] Procesando pago de {data['amount']} {data['currency']} para usuario {data['user_id']}")

# Clase legacy 
class ServicioPagoLegacy:
    def pagar(self, datos_legacy):
        print(f"[LEGACY] Procesando pago para cliente {datos_legacy['cliente']} por {datos_legacy['monto_total']} {datos_legacy['moneda']}")

# Adaptador
class PagoAdapter(ProcesadorPago):
    def __init__(self, servicio_legacy):
        self.servicio_legacy = servicio_legacy

    def procesar_pago(self, json_data):
        moderno = json.loads(json_data)
        print(f"[JSON moderno recibido] {moderno}")

        legacy = {
            "cliente": moderno["user_id"],
            "monto_total": moderno["amount"],
            "moneda": moderno["currency"]
        }

        print(f"[Adaptado a legacy] {legacy}")
        self.servicio_legacy.pagar(legacy)

# Ejecución
if __name__ == "__main__":
    json_input = json.dumps({
        "user_id": "u123",
        "amount": 250.0,
        "currency": "USD"
    })

    print("\n--- Uso de clase moderna ---")
    moderno = PagoModerno()
    moderno.procesar_pago(json_input)

    print("\n--- Uso de clase legacy con adaptador ---")
    legacy = ServicioPagoLegacy()
    adaptador = PagoAdapter(legacy)
    adaptador.procesar_pago(json_input)
