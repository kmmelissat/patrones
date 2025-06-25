class ManejadorBD:
    _instancia = None
    _conectado = False
    _conexiones_abiertas = 0

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def conectar(self):
        if not self._conectado:
            print("Conectando a la base de datos...")
            self._conectado = True
            self._conexiones_abiertas = 1
        else:
            print("Ya existe una conexión activa.")

    def desconectar(self):
        if self._conectado:
            print("Conexión cerrada.")
            self._conectado = False
            self._conexiones_abiertas = 0
        else:
            print("No hay conexión activa.")

    def obtener_conexiones_abiertas(self):
        return self._conexiones_abiertas


# Ejemplo de uso
conn1 = ManejadorBD()
conn1.conectar()

conn2 = ManejadorBD()
conn2.conectar()

conn1.desconectar()

print("Conexiones abiertas:", conn1.obtener_conexiones_abiertas())
