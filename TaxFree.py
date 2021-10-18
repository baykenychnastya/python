import enum
from Inputs import *
from Input import *


class TAX_FREE(object):

    def __init__(self, ID=None, Company=None, Country=None, vat_rate=None, date_of_purchase=None, vat_code=None,
                 date_of_tax_free_registration=None):
        self.ID = Input(ID, 'ID', [validateInteger, validatePositive])
        self.Company = Input(Company, 'Company', [validateRequiredStringWithTrim])
        self.Country = Input(Country, 'Country (Italy or Germany or France)', [lambda value: validateEnumValue(value, CountryEnum)])
        self.vat_rate = InputInteger(vat_rate, "Vat rate", [lambda x: 0 < x < 41])
        self.date_of_purchase = InputDate(date_of_purchase, "Date of purchase", [validateDateString])
        self.vat_code = Input(vat_code, "Vat code (in kind VA***_**_***)", [lambda x: patternValidation(x, "^VA.{3,3}_.{2,2}_.{3,3}$")])
        self.date_of_tax_free_registration = InputDate(date_of_tax_free_registration, "Date of tax free registration", [validateDateString])

        self.inputValues = Inputs([
            self.ID,
            self.Company,
            self.Country,
            self.vat_rate,
            self.date_of_purchase,
            self.vat_code,
            self.date_of_tax_free_registration])

    def validate(self):
        self.inputValues.validate()

    def checkIsValid(self):
        return self.inputValues.get_isValid()

    def get_ID(self):
        return self.ID.value

    def get_Company(self):
        return self.Company.value

    def get_Country(self):
        return self.Country.value

    def get_vat_rate(self):
        return self.vat_rate.value

    def get_date_of_purchase(self):
        return self.date_of_purchase.value

    def get_vat_code(self):
        return self.vat_code.value

    def get_date_of_tax_free_registration(self):
        return self.date_of_tax_free_registration.value

    def enterCompany(self):
        self.Company.readValue()

    def enterCountry(self):
        self.Country.readValue()

    def enterVatRate(self):
        self.vat_rate.readValue()

    def enterDate_of_tax_free_registration(self):
        self.date_of_tax_free_registration.readValue()

    def enterVat_code(self):
        self.vat_code.readValue()

    def enterDate_of_purchase(self):
        self.date_of_purchase.readValue()

    def toJson(self):
        return {
            "ID": self.ID.value,
            "Company": self.Company.value,
            "Country": self.Country.value,
            "vat_rate": self.vat_rate.value,
            "date_of_purchase": str(self.date_of_purchase.value),
            "vat_code": self.vat_code.value,
            "date_of_tax_free_registration": str(self.date_of_tax_free_registration.value)
        }

    def display(self):
        print(self.toJson())


class CountryEnum(str, enum.Enum):
    Germany = "Germany"
    Italy = "Italy"
    France = "France"
