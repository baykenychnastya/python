#!flask/bin/python
import json
from flask_swagger_ui import get_swaggerui_blueprint

from flask import Flask, jsonify
from flask import request

from TaxFree import TAX_FREE
from collectionTaxFree import TaxFreeCollection
from flask_parameter_validation import ValidateParameters, Route, Json, Query

app = Flask(__name__)

collectionTaxFree = TaxFreeCollection()


@app.route('/TAX_FREE/<int:ID>', methods=['GET'])
def getByID(ID):
    taxFree = collectionTaxFree.GetByID(ID)
    if taxFree is None:
        return jsonify({"status": 404,
                        "message": "Element is not found"})
    return app.response_class(response=json.dumps(taxFree.toJson(), indent=2, default=str), status=200,
                              mimetype="application/json", )


@app.route('/TAX_FREE/<int:ID>', methods=['DELETE'])
def deleteById(ID):
    taxFree = collectionTaxFree.GetByID(ID)
    if taxFree is None:
        return jsonify({"status": 404,
                        "message": "Element is not found"})
    collectionTaxFree.deleteByID(ID)
    collectionTaxFree.saveChanges()
    return jsonify({"status": 200,
                    "message": "Tax Free has been successfully deleted."})


@app.route('/TAX_FREE', methods=['GET'])
@ValidateParameters()
def search(
        sort_type: str = Query('asc')
):
    sortType = request.args.get('sort_type')

    if sortType != 'asc' and sortType != 'desc':
        return jsonify({"status": 400, "message": "Invalid sort_type asc|desc"})
    sortBy = request.args.get('sort_by')
    searchString = request.args.get('search_string')

    taxFrees = collectionTaxFree.find(searchString)
    if len(taxFrees) == 0:
        return jsonify({"status": 404, "message": "Element is not found"})

    try:
        if sortBy == 'Company':
            taxFrees.sort(key=lambda x: str(getattr(x, f"get_{sortBy}")()).lower(), reverse=sortType == 'desc')
        else:
            taxFrees.sort(key=lambda x: getattr(x, f"get_{sortBy}")(), reverse=sortType == 'desc')
    except:
        return jsonify({"status": 400, "message": "Invalid request"})

    return app.response_class(response=json.dumps([obj.toJson() for obj in taxFrees], indent=2, default=str),
                              status=200,
                              mimetype="application/json")


@app.route('/TAX_FREE', methods=['POST'])
def create():
    tax = TAX_FREE(ID=collectionTaxFree.generateID(), Company=request.form['Company'], Country=request.form['Country'],
                   vat_rate=int(request.form['vat_rate']), date_of_purchase=request.form['date_of_purchase'],
                   vat_code=request.form['vat_code'],
                   date_of_tax_free_registration=request.form['date_of_tax_free_registration'])

    if tax.checkIsValid() is True:
        collectionTaxFree.taxFrees.append(tax)
        collectionTaxFree.saveChanges()
        return app.response_class(response=json.dumps(tax.toJson(), indent=2, default=str), status=200,
                                  mimetype="application/json", )
    massage = tax.checkIsValid()
    return jsonify({"status": 400,
                    "errors": {massage}})


@app.route('/TAX_FREE/<int:ID>', methods=['PUT'])
def update(ID):
    taxFree = collectionTaxFree.GetByID(ID)
    if taxFree is None:
        return jsonify({"status": 404,
                        "message": "Element is not found"})
    collectionTaxFree.deleteByID(ID)
    taxFree = TAX_FREE(ID=ID, Company=request.form['Company'], Country=request.form['Country'],
                       vat_rate=int(request.form['vat_rate']), date_of_purchase=request.form['date_of_purchase'],
                       vat_code=request.form['vat_code'],
                       date_of_tax_free_registration=request.form['date_of_tax_free_registration'])
    massage = taxFree.checkIsValid()
    if massage is True:
        collectionTaxFree.taxFrees.append(taxFree)
        collectionTaxFree.saveChanges()
        return app.response_class(response=json.dumps(taxFree.toJson(), indent=2, default=str), status=200,
                                  mimetype="application/json", )
    return jsonify({"status": 400,
                    "errors": {massage}})


if __name__ == '__main__':
    app.run(debug=True)
