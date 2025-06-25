#Logger
class Logger:
    def log(self, mensaje):
        print(f"[LOG] {mensaje}")

#EmailService
class EmailService:
    def enviar_email(self, mensaje):
        print(f"[EMAIL] Enviando email: {mensaje}")

#CuentaBancaria 
class CuentaBancaria:
    def __init__(self, logger, email_service):
        self.logger = logger
        self.email_service = email_service

    def transferir(self, monto):
        mensaje = f"Se transfirieron ${monto}"
        self.logger.log(mensaje)
        self.email_service.enviar_email(mensaje)

# Simulación de uso esperado
logger = Logger()
email = EmailService()
cuenta = CuentaBancaria(logger, email)
cuenta.transferir(100)
