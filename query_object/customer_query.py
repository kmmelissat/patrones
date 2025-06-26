import random

class Customer:
    def __init__(self, name, country, is_active, total_spent):
        self.name = name
        self.country = country
        self.is_active = is_active
        self.total_spent = total_spent

    def __str__(self):
        return f"{self.name} - {self.country} - ${self.total_spent:.2f}"

class CustomerQuery:
    def __init__(self, customers):
        self.customers = customers
        self.filtered = customers

    def active(self):
        self.filtered = [c for c in self.filtered if c.is_active]
        return self

    def from_country(self, country):
        self.filtered = [c for c in self.filtered if c.country == country]
        return self

    def with_min_spent(self, amount):
        self.filtered = [c for c in self.filtered if c.total_spent >= amount]
        return self

    def get(self):
        return self.filtered

# Generar 30 clientes simulados
names = ["John Doe", "Jane Smith", "Alice", "Bob", "Eve", "Charlie", "Daniel", "Laura", "Mia", "Liam",
         "Noah", "Olivia", "Ava", "Emma", "Sophia", "James", "Lucas", "Mason", "Isabella", "Zoe",
         "Leo", "Nina", "Oscar", "Pablo", "Quinn", "Ruby", "Sam", "Tina", "Uma", "Victor"]

countries = ["USA", "Canada", "Mexico", "Germany", "France"]
customers = []

for name in names:
    customer = Customer(
        name=name,
        country=random.choice(countries),
        is_active=random.choice([True, False]),
        total_spent=round(random.uniform(100, 2000), 2)
    )
    customers.append(customer)

# Agregar un cliente que cumple con todos los criterios esperados
customers.append(Customer("John Doe", "USA", True, 1500.00))

# Consultar clientes con los filtros
resultados = CustomerQuery(customers).active().from_country("USA").with_min_spent(1000).get()

# Mostrar resultados
for c in resultados:
    print(c)
