class Orden:
    def __init__(self, usuario, productos, direccion, metodo_pago, descuento=0):
        self.usuario = usuario
        self.productos = productos 
        self.direccion = direccion
        self.metodo_pago = metodo_pago
        self.descuento = descuento
        self.total = None 

    def __str__(self):
        productos_str = ", ".join([f"{nombre} (${precio})" for nombre, precio in self.productos])
        return (
            f"Orden de: {self.usuario}\n"
            f"Productos: {productos_str}\n"
            f"Dirección: {self.direccion}\n"
            f"Pago: {self.metodo_pago}\n"
            f"Descuento: {self.descuento}%\n"
            f"Total a pagar: ${self.total}"
        )


class OrdenBuilder:
    def __init__(self):
        self.usuario = None
        self.productos = []
        self.direccion = None
        self.metodo_pago = None
        self.descuento = 0

    def set_usuario(self, usuario):
        self.usuario = usuario
        return self

    def agregar_producto(self, nombre, precio):
        self.productos.append((nombre, precio))
        return self

    def set_direccion(self, direccion):
        self.direccion = direccion
        return self

    def set_metodo_pago(self, metodo_pago):
        self.metodo_pago = metodo_pago
        return self

    def set_descuento(self, descuento):
        self.descuento = descuento
        return self

    def build(self):
        return Orden(
            usuario=self.usuario,
            productos=self.productos,
            direccion=self.direccion,
            metodo_pago=self.metodo_pago,
            descuento=self.descuento
        )


class CalculadorDeTotal:
    def calcular(self, orden):
        subtotal = sum(precio for _, precio in orden.productos)
        if orden.descuento:
            descuento_aplicado = subtotal * (orden.descuento / 100)
            return round(subtotal - descuento_aplicado, 2)
        return subtotal


# Ejemplo de uso
builder = OrdenBuilder()
orden = (
    builder.set_usuario("Melissa Solorzano")
           .agregar_producto("MacBook Pro 14'", 1600)
           .agregar_producto("Apple Pencil", 100)
           .set_direccion("Pesherman Calle Wallabi 2 Sidney")
           .set_metodo_pago("Credit Card")
           .set_descuento(15)  # 15%
           .build()
)

calculador = CalculadorDeTotal()
orden.total = calculador.calcular(orden)

print(orden)
