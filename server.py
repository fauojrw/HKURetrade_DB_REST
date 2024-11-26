from flask import Flask
import sqlite3
from flask import request


app = Flask(__name__)

@app.route('/test')
def test_route():
    return 'Hello, World!'


# Insertion (Create)
@app.route('/users', methods=['POST'])
def create_user():
    # name, email, rating - 0
    con = sqlite3.connect('hku_retrade.db')
    name = request.form['name']
    email = request.form['email']

    insertQuery = "INSERT INTO User (name, email, rating) values (?, ?, 0);"
    con.execute(insertQuery, (name, email))
    con.commit()
    con.close()

    return {"status": "1"} # successful

@app.route('/buyers', methods=['POST'])
def create_buyer():
    # Implementation for creating a buyer
    pass

@app.route('/sellers', methods=['POST'])
def create_seller():
    # Implementation for creating a seller
    pass

@app.route('/commodities', methods=['POST'])
def create_commodity():
    # Implementation for creating a commodity
    pass

@app.route('/commodities/<int:CID>/pictures', methods=['POST'])
def create_commodity_picture(CID):
    # Implementation for creating a picture for a commodity
    pass

@app.route('/transactions', methods=['POST'])
def create_transaction():
    # Implementation for creating a transaction
    pass

# Deletion (Delete)
@app.route('/users/<int:UID>', methods=['DELETE'])
def delete_user(UID):
    # Implementation for deleting a user
    pass

@app.route('/buyers/<int:UID>', methods=['DELETE'])
def delete_buyer(UID):
    # Implementation for deleting a buyer
    pass

@app.route('/sellers/<int:UID>', methods=['DELETE'])
def delete_seller(UID):
    # Implementation for deleting a seller
    pass

@app.route('/commodities/<int:CID>', methods=['DELETE'])
def delete_commodity(CID):
    # Implementation for deleting a commodity
    pass

@app.route('/commodities/<int:CID>/pictures/<int:pictureID>', methods=['DELETE'])
def delete_commodity_picture(CID, pictureID):
    # Implementation for deleting a picture for a commodity
    pass

@app.route('/transactions/<int:transactionID>', methods=['DELETE'])
def delete_transaction(transactionID):
    # Implementation for deleting a transaction
    pass

# Selection (Read)
@app.route('/users/<int:UID>', methods=['GET'])
def get_user(UID):
    # Implementation for getting a user
    pass

@app.route('/buyers/<int:UID>', methods=['GET'])
def get_buyer(UID):
    # Implementation for getting a buyer
    pass

@app.route('/sellers/<int:UID>', methods=['GET'])
def get_seller(UID):
    # Implementation for getting a seller
    pass

@app.route('/commodities/<int:CID>', methods=['GET'])
def get_commodity(CID):
    # Implementation for getting a commodity
    pass

@app.route('/commodities/<int:CID>/pictures', methods=['GET'])
def get_commodity_pictures(CID):
    # Implementation for getting pictures of a commodity
    pass

@app.route('/buyers/<int:UID>/transactions', methods=['GET'])
def get_buyer_transactions(UID):
    # Implementation for getting transactions of a buyer
    pass

@app.route('/commodities', methods=['GET'])
def search_commodities_by_seller():
    seller_UID = request.args.get('seller')
    # Implementation for searching commodities by seller's UID
    pass

if __name__ == '__main__':
    app.run(debug=True)