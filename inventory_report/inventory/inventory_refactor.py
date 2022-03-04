from collections.abc import Iterable

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, report_type):
        products_data = self.importer.import_data(path)
        for product in products_data:
            self.data.append(product)
        products = self.data
        if report_type == "simples":
            report = SimpleReport.generate(products)
        else:
            report = CompleteReport.generate(products)
        return report

    def __iter__(self):
        return InventoryIterator(self.data)
