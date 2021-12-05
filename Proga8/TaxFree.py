import enum

from marshmallow import validate
from sqlalchemy import Column, CheckConstraint

from Inputs import *
from Input import *
from datetime import datetime
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy, Model

from config import ma, db


class TAX_FREE(object):
    def __init__(self, ID=None, Company=None, Country=None, vat_rate=None, date_of_purchase=None, vat_code=None,
                 date_of_tax_free_registration=None):
        self.ID = Input(ID, 'ID', [VALIDATION.validateInteger, VALIDATION.validatePositive])
        self.Company = Input(Company, 'Company', [VALIDATION.validateRequiredStringWithTrim])
        self.Country = Input(Country, 'Country (Italy or Germany or France)',
                             [lambda value: VALIDATION.validateEnumValue(value, CountryEnum)])
        self.vat_rate = InputInteger(vat_rate, "Vat rate", [lambda x: 0 < x < 41])
        self.date_of_purchase = InputDate(date_of_purchase, "Date of purchase", [VALIDATION.validateDateString])
        self.vat_code = Input(vat_code, "Vat code (in kind VA***_**_***)",
                              [lambda x: VALIDATION.patternValidation(x, "^VA.{3,3}_.{2,2}_.{3,3}$")])
        self.date_of_tax_free_registration = InputDate(date_of_tax_free_registration, "Date of tax free registration",
                                                       [VALIDATION.validateDateString,
                                                        lambda x: VALIDATION.validateLowerDateInputFile(
                                                            self.date_of_purchase, x,
                                                            "Date of tax free registration must be more date of "
                                                            "purchase")])

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
        value = input(f'Enter Company: ')
        if self.set_Company(value) is False:
            self.enterCompany()

    @VALIDATION.validation_decorator(VALIDATION.validateRequiredStringWithTrim)
    def set_Company(self, value):
        self.Company.value = value
        return True

    def enterCountry(self):
        value = input(f'Enter Country (Italy or Germany or France): ')
        if self.set_Country(value) is False:
            self.enterCountry()

    @VALIDATION.validation_decorator(lambda value: VALIDATION.validateEnumValue(value, CountryEnum))
    def set_Country(self, value):
        self.Country.value = value
        return True

    def enterVat_Rate(self):
        value = input(f'Enter VAT Rate from 1 to 41: ')
        if self.set_vat_rate(value) is False:
            self.enterVat_Rate()

    @VALIDATION.validation_decorator(lambda x: VALIDATION.validateInteger(x) and (0 < int(x) <= 41))
    def set_vat_rate(self, value):
        self.vat_rate.value = int(value)
        return True

    def enterDate_of_tax_free_registration(self):
        value = input(f'Enter Date of tax free registration in format YYYY-MM-DD: ')
        if self.set_date_of_tax_free_registration(value, self.date_of_purchase.value) is False:
            self.enterDate_of_tax_free_registration()

    @VALIDATION.validation_decorator_with_two_arguments(
        lambda x, date_of_purchase: VALIDATION.validateDateString(x) and
                                    VALIDATION.validateLowerDate(datetime.strptime(date_of_purchase, '%Y-%m-%d'),
                                                                 datetime.strptime(x, '%Y-%m-%d'),
                                                                 "Date of tax free registration must be more date of purchase"))
    def set_date_of_tax_free_registration(self, value, date_of_purchase):
        self.date_of_tax_free_registration.value = value
        return True

    def enterVat_code(self):
        value = input(f'Enter VAT CODE (in kind VA***_**_***): ')
        if self.set_vat_code(value) is False:
            self.enterVat_code()

    @VALIDATION.validation_decorator(lambda x: VALIDATION.patternValidation(x, "^VA.{3,3}_.{2,2}_.{3,3}$"))
    def set_vat_code(self, value):
        self.vat_code.value = value
        return True

    def enterDate_of_purchase(self):
        value = input(f'Enter Date of purchase in format YYYY-MM-DD: ')
        if self.set_date_of_purchase(value) is False:
            self.enterDate_of_purchase()

    @VALIDATION.validation_decorator(VALIDATION.validateDateString)
    def set_date_of_purchase(self, value):
        self.date_of_purchase.value = value
        return True

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


class TAX_FREEModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(10), nullable=False)
    vat_rate = db.Column(db.Integer, nullable=False)
    date_of_purchase = db.Column(db.Date, nullable=False)
    vat_code = db.Column(db.String(12), nullable=False)
    date_of_tax_free_registration = db.Column(db.Date, nullable=False)


class TAX_FREESchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TAX_FREEModel
        fields = ("id", "company", "country", "vat_rate", "date_of_purchase",
                  "vat_code", "date_of_tax_free_registration")

