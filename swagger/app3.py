import json

import MySQLdb.cursors
from flask import request
from flask_parameter_validation import ValidateParameters

from TaxFree import TAX_FREE, TAX_FREESchema
from config import app, mysql


@app.route('/tax-free/<int:ID>', methods=['GET'])
def getByID(ID):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    cursor.execute('SELECT * FROM tax_free WHERE id = % s', (ID,))
    taxFree = cursor.fetchone()

    if taxFree is None:
        return createResponse(404, "Element is not found")

    mysql.connection.commit()
    return app.response_class(response=json.dumps(taxFree, indent=2, default=str), status=200,
                              mimetype="application/json")


@app.route('/tax-free/<int:ID>', methods=['DELETE'])
def deleteById(ID):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    cursor.execute('SELECT * FROM tax_free WHERE id = % s', (ID,))
    taxFree = cursor.fetchone()

    if taxFree is None:
        return createResponse(404, "Element is not found")

    cursor.execute('DELETE FROM tax_free WHERE id = % s', (ID,))
    mysql.connection.commit()
    return createResponse(200, "Tax Free has been successfully deleted.")


@app.route('/tax-free', methods=['GET'])
@ValidateParameters()
def search():
    sortType = request.args.get('sort_type', default='asc')
    sortBy = request.args.get('sort_by', default='id')
    searchString = request.args.get('search_string', default='')
    offset = request.args.get('offset', default=0, type=int)
    limit = request.args.get('limit', type=int)

    if sortType != 'asc' and sortType != 'desc':
        return createResponse(400, "Invalid sort_type asc|desc")

    if sortBy not in TAX_FREESchema.Meta.fields:
        return createResponse(400, "Invalid sort_by")
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT @s := % s; ', (f'%{searchString}%',))

    sqlCommand = 'SELECT * FROM tax_free WHERE country LIKE @s or company LIKE @s ' \
                 'or vat_rate LIKE @s or date_of_purchase LIKE @s or vat_code LIKE @s ' \
                 f'or date_of_tax_free_registration LIKE @s ORDER BY {sortBy} {sortType}'

    if limit is not None:
        if offset and limit < 0:
            return createResponse(400, "Invalid offset or limit < 0")

        sqlCommand = sqlCommand + f' LIMIT {limit} OFFSET {offset * limit}'

    cursor.execute(sqlCommand)
    taxFree = cursor.fetchall()
    cursor.execute('SELECT COUNT(*) as rowsCount FROM tax_free')
    count = cursor.fetchone()
    return app.response_class(response=json.dumps({"result": taxFree,
                                                   "count": count['rowsCount']}, indent=2, default=str),
                              status=200, mimetype="application/json")


@app.route('/tax-free', methods=['POST'])
def create():
    request_data = request.get_json(force=True)

    schema = TAX_FREESchema()
    errors = schema.validate(request_data)

    if len(errors) > 0:
        return createResponse(400, errors)

    tax = TAX_FREE(ID=0, Company=request_data['company'], Country=request_data['country'],
                   vat_rate=int(request_data['vat_rate']), date_of_purchase=request_data['date_of_purchase'],
                   vat_code=request_data['vat_code'],
                   date_of_tax_free_registration=request_data['date_of_tax_free_registration'])

    validationResult = tax.checkIsValid()
    if validationResult is not True:
        return app.response_class(response=json.dumps(validationResult), status=400,
                                  mimetype="application/json")

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('INSERT INTO tax_free VALUES (NULL, % s, % s, % s, % s, % s, % s)',
                   (tax.Company.value, tax.Country.value, tax.vat_rate.value, tax.date_of_purchase.value,
                    tax.vat_code.value, tax.date_of_tax_free_registration.value))
    mysql.connection.commit()

    cursor.execute('SELECT * FROM tax_free WHERE id = (SELECT LAST_INSERT_ID()) LIMIT 1')
    tax = cursor.fetchone()
    return app.response_class(response=json.dumps(tax, indent=2, default=str), status=200,
                              mimetype="application/json", )


@app.route('/tax-free/<int:ID>', methods=['PUT'])
def update(ID):
    request_data = request.get_json(force=True)

    schema = TAX_FREESchema()
    errors = schema.validate(request_data)

    if len(errors) > 0:
        return createResponse(400, errors)

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    cursor.execute('SELECT * FROM tax_free WHERE id = % s', (ID,))
    taxFree = cursor.fetchone()

    if taxFree is None:
        return createResponse(404, "Element is not found")

    tax = TAX_FREE(ID=ID, Company=request_data['company'], Country=request_data['country'],
                   vat_rate=int(request_data['vat_rate']), date_of_purchase=request_data['date_of_purchase'],
                   vat_code=request_data['vat_code'],
                   date_of_tax_free_registration=request_data['date_of_tax_free_registration'])

    validationResult = tax.checkIsValid()
    if validationResult is not True:
        return app.response_class(response=json.dumps(validationResult), status=400,
                                  mimetype="application/json")

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('UPDATE tax_free '
                   'SET company = % s, country = % s, vat_rate = % s,'
                   ' date_of_purchase = % s, vat_code = % s,'
                   ' date_of_tax_free_registration = % s WHERE id = % s',
                   (tax.Company.value, tax.Country.value, tax.vat_rate.value, tax.date_of_purchase.value,
                    tax.vat_code.value, tax.date_of_tax_free_registration.value, ID,))
    mysql.connection.commit()

    cursor.execute('SELECT * FROM tax_free WHERE id = % s', (ID,))
    tax = cursor.fetchone()
    return app.response_class(response=json.dumps(tax, indent=2, default=str), status=200,
                              mimetype="application/json")


def createResponse(status, message):
    return app.response_class(response=json.dumps({"status": status, "message": message}),
                              status=status,
                              mimetype="application/json")


if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"))
