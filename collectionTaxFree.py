from TaxFree import TAX_FREE
import json


class TaxFreeCollection(object):
    taxFrees = []

    def __init__(self):
        with open('dataForTaxFree.json', 'r', encoding='utf-8') as f:
            taxFreesJson = json.load(f)

            for taxFreeJson in taxFreesJson:
                self.taxFrees.append(
                    TAX_FREE(
                        taxFreeJson['ID'],
                        taxFreeJson['Company'],
                        taxFreeJson['Country'],
                        taxFreeJson['vat_rate'],
                        taxFreeJson['date_of_purchase'],
                        taxFreeJson['vat_code'],
                        taxFreeJson['date_of_tax_free_registration'])
                )

    def display(self):
        for obj in self.taxFrees:
            print(obj.ID, obj.Company, obj.Country, obj.vat_rate, obj.date_of_purchase, obj.vat_code,
                  obj.date_of_tax_free_registration, sep=' ')

    def sort(self):
        self.taxFrees.sort(key=lambda t: t.vat_rate)

    def addNew(self):
        tax = TAX_FREE()

        tax.generateID()
        tax.enterCompany()
        tax.enterCountry()
        tax.enterVatRate()
        tax.enterDate_of_purchase()
        tax.enterVat_code()
        tax.enterDate_of_tax_free_registration()

        self.taxFrees.append(tax)

    def saveChanges(self):
        jsonCollection = '['

        for taxFree in self.taxFrees:
            jsonCollection += f'{taxFree.detJsonType()}, '

        jsonCollection = jsonCollection[:-2] + ']'

        with open('dataForTaxFree.json', 'w') as f:
            f.write(jsonCollection)

    def deleteByID(self, ID):
        for taxFree in self.taxFrees:
            if taxFree.ID == ID:
                self.taxFrees.remove(taxFree)
                return

    def editNoteByID(self, ID):
        for taxFree in self.taxFrees:
            if taxFree.ID == ID:
                self.deleteByID(ID)
                self.edit(taxFree)

                return

    def edit(self, taxFree):
        taxFree.enterCompany()
        taxFree.enterCountry()
        taxFree.enterVatRate()
        taxFree.enterDate_of_purchase()
        taxFree.enterVat_code()
        taxFree.enterDate_of_tax_free_registration()

        self.taxFrees.append(taxFree)

    def find(self, value):
        str(value)
        isFind = False
        print("Objects with coincidence:")

        for item in self.taxFrees:
            if str(item.ID).find(value) != -1 or str(item.Company).find(value) != -1\
                    or str(item.Country).find(value) != -1 or str(item.vat_rate).find(value) != -1\
                    or str(item.date_of_purchase).find(value) != -1 or str(item.vat_code).find(value) != -1\
                    or str(item.date_of_tax_free_registration).find(value) != -1:
                item.display()
                isFind = True
        if not isFind:
            print("Oops, there is no coincidence")