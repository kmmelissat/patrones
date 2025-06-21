class Pizza:
    def __init__(self):
        self.ingredientes = []

    def __str__(self):
        return f"Pizza con: {', '.join(self.ingredientes)}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    # Ingredientes básicos
    def add_queso(self):
        self.pizza.ingredientes.append("queso")
        return self

    def add_pepperoni(self):
        self.pizza.ingredientes.append("pepperoni")
        return self

    def add_jamon(self):
        self.pizza.ingredientes.append("jamón")
        return self

    def add_champinones(self):
        self.pizza.ingredientes.append("champiñones")
        return self

    def add_pina(self):
        self.pizza.ingredientes.append("piña")
        return self

    def add_aceitunas(self):
        self.pizza.ingredientes.append("aceitunas")
        return self

    def add_pimientos(self):
        self.pizza.ingredientes.append("pimientos")
        return self

    def add_salchicha(self):
        self.pizza.ingredientes.append("salchicha")
        return self

    def add_cebolla(self):
        self.pizza.ingredientes.append("cebolla")
        return self

    def build(self):
        return self.pizza


# Builder con recetas prediseñadas
class EspecialidadPizzaBuilder(PizzaBuilder):

    def build_super_suprema(self):
        return (self.add_queso()
                    .add_pepperoni()
                    .add_jamon()
                    .add_champinones()
                    .add_aceitunas()
                    .add_pimientos()
                    .add_cebolla()
                    .add_salchicha()
                    .build())

    def build_hawaiana(self):
        return (self.add_queso()
                    .add_jamon()
                    .add_pina()
                    .build())

    def build_vegetariana(self):
        return (self.add_queso()
                    .add_champinones()
                    .add_pimientos()
                    .add_aceitunas()
                    .add_cebolla()
                    .build())


# Uso de pizzas sencillas
builder = PizzaBuilder()
pizza_basica = builder.add_queso().add_pepperoni().build()
print(pizza_basica)

# Uso de pizzas especialidad
especial = EspecialidadPizzaBuilder()
print(especial.build_super_suprema())
print(especial.build_hawaiana())
print(especial.build_vegetariana())