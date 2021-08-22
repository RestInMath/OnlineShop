from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from pymongo.errors import BulkWriteError
from Product import Product

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/shop_test")
db = mongodb_client.db
col = db["goods"]
number_of_elements = col.count_documents({})
Product.update_id_counter(number_of_elements)

#create product
@app.route("/add", methods=['POST'])
def add_one():
    try:
        product_details = request.get_json(force=True)
    except Exception as e:
        return jsonify(message=str(e))

    keys = list(product_details.keys())
    required_fields = ['name', 'description']

    if keys != required_fields:
        return jsonify(error="Wrong request")

    try:
        new_product = Product(product_details['name'], product_details['description'])
        added_product = col.insert_one({
            '_id':new_product.id,
            'name': new_product.name,
            'description':new_product.description
            })
    except BulkWriteError as e:
        return jsonify(message="duplicates encountered and ignored",                             
                             details=e.details)

    return jsonify(message="success", insertedId=added_product.inserted_id)

#home page, returns list of goods with optional filter
@app.route("/", methods=['GET'])
def home():
    requested_fields = {'name':1, '_id':0}
    try:
        query = request.get_json(force=True)
    except Exception as e:
        query = None

    if not query:
        goods = col.find({}, requested_fields)
        number_of_elements = col.count_documents({})
    
    elif len(query.keys())==1 and list(query.keys())[0] in ['name', 'description']:
        #search by parameter
        try:
            key = list(query.keys())[0]
            query = {
                key: {"$regex": query[key]}
                }

            goods = col.find(query, requested_fields)
            number_of_elements = len(list(col.find(query)))
        
        except TypeError as e:
            return jsonify(error=str(e))
    else:
        return jsonify(error="Wrong request")

    goods = list(goods.sort('name'))
    return jsonify(number_of_elements=number_of_elements, goods=goods)

#get details by id
@app.route("/details", methods=['GET'])
def details():
    query = request.get_json(force=True)

    if not query or 'id' not in query.keys() or len(query.keys())!=1:
        return jsonify(error="Wrong request")
    
    product = col.find_one_or_404({'_id':query['id']})
    
    return jsonify(message="success", product=product)

#clear table
@app.route("/delete_all")
def delete_all():
    try:
        col.delete_many({})
        Product.update_id_counter(0)
    except Exception as e:
        return jsonify(str(e))

    return jsonify(message="success")

#An error-handler to ensure that errors are returned as JSON
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify(error=str(e))

if __name__ == "__main__":
    app.run()