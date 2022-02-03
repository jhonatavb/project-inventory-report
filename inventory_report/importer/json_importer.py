from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class JsonImporter(Importer):
    @classmethod
    def import_data(self, path: str):
        if path.endswith(".json"):
            return Inventory.read_file_type(path) 
        else:
            raise ValueError("Arquivo inválido")
