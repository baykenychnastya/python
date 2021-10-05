import json
from validationForTaxFree import checkVadCoode
import datetime
from validationForTaxFree import readIntegerWithCheck


class TAX_FREE(object):

    def __init__(self, ID=None, Company=None, Country=None, vat_rate=None, date_of_purchase=None, vat_code=None,
                 date_of_tax_free_registration=None):
        self.ID = ID
        self.Company = Company
        self.Country = Country
        self.vat_rate = vat_rate
        self.date_of_purchase = date_of_purchase
        self.vat_code = vat_code
        self.date_of_tax_free_registration = date_of_tax_free_registration

    import enum

    class Country(enum.Enum):
        Germany = 0
        Italy = 1
        France = 2

    file = open('dataForTaxFree.json')

    import itertools

    id_iter = itertools.count()

    def generateID(self):

        self.ID = next(TAX_FREE.id_iter)
        # print('ID', self.ID)
        return self.ID

    def enterCompany(self):
        self.Company = input('Enter Company: ')

    def enterCountry(self):
        selectCountry = input('Select a country:\t1-Germany\t2-Italy \t3-France: ')
        if selectCountry == '1':
            self.Country = 'Germany'
        elif selectCountry == '2':
            self.Country = 'Italy'
        elif selectCountry == '3':
            self.Country = 'France'
        else:
            print('Please select only the options listed above!')

    def enterVatRate(self):
        self.vat_rate = readIntegerWithCheck('Enter Vat Rate:', lambda x: 0 < x < 41, 'Invalid data, try again ')

    def enterDate_of_purchase(self):
        year = readIntegerWithCheck('Enter year of purchase: ', lambda x: 0 < x < 2021, 'Invalid data, try again ')
        month = readIntegerWithCheck('Enter moth of purchase: ', lambda x: 0 < x < 13, 'Invalid data, try again ')
        day = readIntegerWithCheck('Enter day of purchase: ', lambda x: 0 < x < 31, 'Invalid data, try again ')
        self.date_of_purchase = datetime.date(year, month, day)

    def enterVat_code(self):
        self.vat_code = checkVadCoode('Enter Vat code in kind VA***_**_***: ')

    def enterDate_of_tax_free_registration(self):
        year = readIntegerWithCheck('Enter year of registration: ', lambda x: 0 < x < 2021, 'Invalid data, try again ')
        month = readIntegerWithCheck('Enter moth of registration: ', lambda x: 0 < x < 13, 'Invalid data, try again ')
        day = readIntegerWithCheck('Enter day of registration: ', lambda x: 0 < x < 31, 'Invalid data, try again ')
        self.date_of_tax_free_registration = datetime.date(year, month, day)

    def detJsonType(self):
        return f'{{ "ID": {self.generateID()}, "Company": "{self.Company}", "Country": "{self.Country}", "vat_rate": {self.vat_rate},"date_of_purchase": "{self.date_of_purchase}", "vat_code": "{self.vat_code}","date_of_tax_free_registration": "{self.date_of_tax_free_registration}"}} '

    def display(self):
        print(f'"ID": {self.generateID()}, "Company": "{self.Company}", "Country": "{self.Country}", "vat_rate": {self.vat_rate},"date_of_purchase": "{self.date_of_purchase}", "vat_code": "{self.vat_code}","date_of_tax_free_registration": "{self.date_of_tax_free_registration}"')