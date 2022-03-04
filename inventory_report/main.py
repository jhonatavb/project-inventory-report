#!/usr/bin/python
from sys import argv, stderr, stdout
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(argv) < 3:
        return stderr.write("Verifique os argumentos\n")
    path = argv[1]
    report_type = argv[2]
    file_format = path.split(".")[-1]

    if file_format == "csv":
        data_reader = InventoryRefactor(CsvImporter)
        report = data_reader.import_data(path, report_type)

    elif file_format == "json":
        data_reader = InventoryRefactor(JsonImporter)
        report = data_reader.import_data(path, report_type)

    else:
        data_reader = InventoryRefactor(XmlImporter)
        report = data_reader.import_data(path, report_type)

    stdout.write(report)
