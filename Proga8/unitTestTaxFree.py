import unittest
from unittest.mock import patch
from TaxFree import TAX_FREE
from collectionTaxFree import TaxFreeCollection
from memento import Memento, Caretaker
from validationForTaxFree import VALIDATION


class TestTaxFree(unittest.TestCase):

    args = {
        "ID": 0,
        "Company": "Google",
        "Country": "Italy",
        "vat_rate": 34,
        "date_of_purchase": "2020-12-12",
        "vat_code": "VA333_33_333",
        "date_of_tax_free_registration": "2020-12-12"
    }
    taxFrees = TaxFreeCollection()
    tax_free = TAX_FREE(*args.values())

    def test_delete(self):
        self.taxFrees.deleteByID(2)
        self.assertEqual(len(self.taxFrees), 6)

    def test_sort(self):
        self.taxFrees.sort("vat_rate")
        self.assertTrue(
            self.taxFrees[0].get_vat_rate() <= self.taxFrees[1].get_vat_rate())

    def test_sort2(self):
        self.taxFrees.sort("Company")
        self.assertFalse(
            self.taxFrees[0].get_Company() >= self.taxFrees[1].get_Company())

    def test_find(self):
        self.assertTrue(self.taxFrees.find("Google") is not None)
        self.assertTrue(self.taxFrees.find("Victor") is None)

    def test_len(self):
        self.assertEqual(self.taxFrees.__len__(), 9)

    def test_get_item(self):
        print(self.taxFrees[8])
        self.assertTrue(isinstance(self.taxFrees[0], TAX_FREE))

    def test_save(self):
        memento = self.taxFrees.save()
        self.assertTrue(isinstance(memento, Memento))

    def test_generate_ID(self):
        self.assertTrue(self.taxFrees.generateID() != 'g')

    def test_getters(self):
        for key, value in self.args.items():
            self.assertEqual(getattr(self.tax_free, f"get_{key}")(), value)

    def test_toJson(self):
        argum = {'Company': 'Google',
                 'Country': 'Italy',
                 'ID': 0,
                 'date_of_purchase': '2020-12-12',
                 'date_of_tax_free_registration': '2020-12-12',
                 'vat_code': 'VA333_33_333',
                 'vat_rate': 34}
        self.assertEqual(self.tax_free.toJson(), argum)

    def test_saveMemento(self):
        caretaker = Caretaker(self.taxFrees)

        caretaker.saveMemento()
        self.assertEqual(caretaker.statesPosition, 0)

    def test_undo(self):
        self.taxFrees.deleteByID(0)
        self.taxFrees.caretaker.saveMemento()
        self.taxFrees.caretaker.undo()
        self.assertEqual(len(self.taxFrees), 3)

        self.taxFrees.caretaker.states = []
        self.assertEqual(self.taxFrees.caretaker.undo(), print("There are no saves"))

        self.taxFrees.caretaker.statesPosition = 0
        self.assertEqual(self.taxFrees.caretaker.undo(), print("There were no new changes"))

    def test_redo(self):
        self.taxFrees.caretaker.redo()
        self.assertEqual(len(self.taxFrees), 9)

        self.taxFrees.caretaker.statesPosition = 0
        self.assertEqual(self.taxFrees.caretaker.redo(), print("There were no new changes"))

    def test_getState(self):
        self.assertTrue(self.taxFrees.caretaker.states[0].getState())

    def test_enter(self):
        argsForSetters = {
            "Company": "Google",
            "Country": "Italy",
            "vat_rate": 34,
            "date_of_purchase": "2020-12-12",
            "vat_code": "VA333_33_333",
            "date_of_tax_free_registration": "2020-12-12"
        }
        tax_free = TAX_FREE(*argsForSetters.values())

        tax_free.set_Company("Django")
        self.assertEqual(tax_free.get_Company(), "Django")
        tax_free.set_Country("Germany")
        self.assertEqual(tax_free.get_Country(), "Germany")
        self.assertTrue(tax_free.set_vat_rate("23"))
        self.assertEqual(tax_free.vat_rate.value, 23)
        tax_free.set_date_of_purchase("2020-12-12")
        self.assertEqual(tax_free.get_date_of_purchase(), "2020-12-12")

        tax_free.set_vat_code("VA333_33_999")
        self.assertEqual(tax_free.get_vat_code(), "VA333_33_999")

        tax_free.set_date_of_tax_free_registration("2020-12-12", "2019-12-12")
        self.assertEqual(tax_free.get_date_of_purchase(), "2020-12-12")

    def test_enterVatRate(self):
        argsForSetters = {
            "Company": "Google",
            "Country": "Italy",
            "vat_rate": 34,
            "date_of_purchase": "2020-12-12",
            "vat_code": "VA333_33_333",
            "date_of_tax_free_registration": "2020-12-12"
        }
        tax_free = TAX_FREE(*argsForSetters.values())
        self.assertTrue(tax_free.set_vat_rate("23"))
        self.assertFalse(tax_free.set_vat_rate("-23"))
        self.assertFalse(tax_free.set_vat_rate("-dss23"))

    @patch('builtins.input', return_value="2002")
    def test_readIntegerWithCheck(self, mock_input):
        assert VALIDATION.readIntegerWithCheck('Enter year : ', lambda x: 0 < x < 2021, 'Invalid data, try again ') == 2002

    @patch('builtins.input', return_value="2")
    def test_readInteger(self, mock_input):
        assert VALIDATION.readInteger('Enter data : ', 'Invalid data') == 2

    def test_validateLowerDate(self):
        self.assertTrue(VALIDATION.validateLowerDate(2020, 2021, "Invalid data"))
        self.assertFalse(VALIDATION.validateLowerDate(2021, 2020, "Invalid data"))

    def test_validateRequiredStringWithTrim(self):
        self.assertTrue(VALIDATION.validateRequiredStringWithTrim('Google'))
        self.assertFalse(VALIDATION.validateRequiredStringWithTrim(' '))

    @patch('builtins.input', side_effect=["Figma", "Germany", "2012-11-11", "2021-12-12", "33", "VA333_33_333"])
    def test_addNew(self, mock_input):
        taxFrees1 = TaxFreeCollection()
        taxFrees1.addNew()
        self.assertEqual(len(taxFrees1), 7)

    @patch('builtins.input', side_effect=["0", "Germany", "2012-11-11", "2021-12-12", "33", "VA333_33_333"])
    def test_editNoteByID(self, mock_input):
        taxFrees2 = TaxFreeCollection()
        taxFrees2.editNoteByID(0)
        self.assertEqual(len(taxFrees2), 9)


if __name__ == '__main__':
    unittest.main()

