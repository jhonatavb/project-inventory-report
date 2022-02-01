from collections import Counter
import datetime

mock = [
        {
            "id": 1,
            "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2020-07-04",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
            "instrucoes_de_armazenamento": "in blandit ultrices enim",
        },
        {
            "id": 2,
            "nome_do_produto": "sodium ferric gluconate complex",
            "nome_da_empresa": "sanofi-aventis U.S. LLC",
            "data_de_fabricacao": "2020-05-31",
            "data_de_validade": "2023-01-17",
            "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
            "instrucoes_de_armazenamento": "duis bibendum morbi",
        },
        {
            "id": 3,
            "nome_do_produto": "Dexamethasone Sodium Phosphate",
            "nome_da_empresa": "sanofi-aventis U.S. LLC",
            "data_de_fabricacao": "2019-09-13",
            "data_de_validade": "2023-02-13",
            "numero_de_serie": "BA52 2034 8595 7904 7131",
            "instrucoes_de_armazenamento": "morbi quis tortor id",
        },
        {
            "id": 4,
            "nome_do_produto": "Uricum acidum, Benzoicum acidum",
            "nome_da_empresa": "Newton Laboratories, Inc.",
            "data_de_fabricacao": "2019-11-08",
            "data_de_validade": "2019-11-25",
            "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
            "instrucoes_de_armazenamento": "velit eu est congue elementum",
        },
        {
            "id": 5,
            "nome_do_produto": "Uricum acidum, Benzoicum acidum",
            "nome_da_empresa": "Newton Laboratories, Inc.",
            "data_de_fabricacao": "2019-11-08",
            "data_de_validade": "2019-11-26",
            "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
            "instrucoes_de_armazenamento": "velit eu est congue elementum",
        }
    ]

class SimpleReport:
    def __init__(self, products_list):
      self.generate = self.generate(products_list)
      pass

    def get_company_with_more_products(products_list):
        company_names = []
        company_with_more_repetitinos = ''
        total = 0
        for company in products_list:
            company_names.append(company['nome_da_empresa'])
        for company in company_names:
            repetitions = Counter(company_names)[company]

            if repetitions > total:
              company_with_more_repetitinos = company
              total = total + 1
        return f'Empresa com maior quantidade de produtos estocados: {company_with_more_repetitinos}'


    def get_product_with_oldest_fabrication_date(products_list):
        fabrication_dates = []
        for date in products_list:
            fabrication_dates.append(date['data_de_fabricacao'])
        oldest_date = sorted(fabrication_dates)[0]
        return f'Data de fabricação mais antiga: {oldest_date}'

    def get_product_with_closest_validate_date(products_list):
        data = datetime.datetime.now()
        validate_dates = []
        for date in products_list:
            if date['data_de_validade'] < str(data):
              validate_dates.append(date['data_de_validade'])
        nearest_date = max(validate_dates)
        return f'Data de validade mais próxima: {nearest_date}'

    def generate(self, products_list):
        company_with_more_products = self.get_company_with_more_products(products_list)
        oldest_fabrication_date = self.get_product_with_oldest_fabrication_date(products_list)
        nearest_validation_date = self.get_product_with_closest_validate_date(products_list)
        return f'{oldest_fabrication_date}\n{nearest_validation_date}\n{company_with_more_products}'
        
# print(generate(mock))

print(SimpleReport.generate(mock))
