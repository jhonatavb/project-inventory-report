import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    # ref https://stackoverflow.com/a/51889958
    @classmethod
    def parse_list(cls, file_type):
        my_list = []
        for row in file_type["dataset"]["record"]:
            my_list.append(row)

        return my_list

    @classmethod
    def read_file_type(cls, path):
        with open(path, "r") as file_type:
            if path.endswith(".csv"):
                reader = csv.DictReader(
                    file_type, delimiter=",", quotechar='"'
                )
                csv_list = []
                for row in reader:
                    csv_list.append(row)

                return csv_list

            if path.endswith(".json"):
                return json.load(file_type)

            if path.endswith(".xml"):
                my_xml = file_type.read()
                my_dict_xml = xmltodict.parse(my_xml)
                my_list = cls.parse_list(my_dict_xml)

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
