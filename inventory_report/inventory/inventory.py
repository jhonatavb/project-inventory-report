import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    # ref https://stackoverflow.com/a/51889958
    @classmethod
    def parse_list(cls, path, data):
        my_list = []
        for row in data:
            my_list.append(row)

        return my_list

    @classmethod
    def read_file_type(cls, path):
        with open(path, "r") as data:
            if path.endswith(".csv"):
                reader = csv.DictReader(
                    data, delimiter=",", quotechar='"'
                )
                my_list = cls.parse_list(path, reader)

                return my_list

            if path.endswith(".json"):
                return json.load(data)

            if path.endswith(".xml"):
                my_xml = data.read()
                my_dict_xml = xmltodict.parse(my_xml)
                my_list = cls.parse_list(path, my_dict_xml["dataset"]["record"])

                return my_list

    @classmethod
    def import_data(cls, path, report_type):
        product_list = cls.read_file_type(path)

        if report_type == "simples":
            type_report_return = SimpleReport.generate(product_list)
            return type_report_return

        if report_type == "completo":
            type_report_return = CompleteReport.generate(product_list)
            return type_report_return

        if report_type != "simples" or report_type != "completo":
            type_report_return = "Invalid format"
            return type_report_return
