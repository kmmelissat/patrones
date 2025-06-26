from abc import ABC, abstractmethod

# Exporter - Implementador
class Exporter(ABC):
    @abstractmethod
    def export(self, data: str):
        pass

class PDFExporter(Exporter):
    def export(self, data: str):
        print(f"Exporting {data} to PDF...")

class HTMLExporter(Exporter):
    def export(self, data: str):
        print(f"Exporting {data} to HTML...")

class JSONExporter(Exporter):
    def export(self, data: str):
        print(f"Exporting {data} to JSON...")

# Report - Abstracción
class Report(ABC):
    def __init__(self, exporter: Exporter):
        self.exporter = exporter

    @abstractmethod
    def generate(self):
        pass

class UserReport(Report):
    def generate(self):
        data = "User Report"
        self.exporter.export(data)

class SalesReport(Report):
    def generate(self):
        data = "Sales Report"
        self.exporter.export(data)

class InventoryReport(Report):
    def generate(self):
        data = "Inventory Report"
        self.exporter.export(data)

# Cliente
if __name__ == "__main__":
    user_pdf = UserReport(PDFExporter())
    sales_html = SalesReport(HTMLExporter())
    inventory_json = InventoryReport(JSONExporter())

    user_pdf.generate()
    sales_html.generate()
    inventory_json.generate()
