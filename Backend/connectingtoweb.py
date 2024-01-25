from flask import Flask, request
import crud_datalayer as dl

from flask_cors import CORS

app = Flask("R & K Collection|Kabir Ahmad")
CORS(app)


@app.get("/products")
def web_get_products():
    return dl.get_products().to_json(orient='records')

@app.get("/products/<product_id>")
def web_get_product(product_id):
    return dl.get_product(product_id).to_json(orient='records')

@app.post("/products")
def web_add_product():
    product = request.get_json()
    dl.add_product(product['pid'],
                   product['name'],
                   product['description'],
                   product['price'],
                   product['image'],
                   product['rating'])
    return "product added"

@app.patch("/products")
def web_update_product():
    product = request.get_json()
    dl.update_product(product['pid'],product['name'],product['description'],product['price'],product['rating'])
    return "Updated Successfully."

@app.delete("/products")
def web_delete_product():
    product = request.get_json()
    dl.delete_product(product['pid'])
    return "Product is Deleted"


app.run(port=8008,debug=True)