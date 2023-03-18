import json

def retrieve_all_products():
    with open('products.json', 'r') as json_file:
        all_products = json.load(json_file)
    return all_products


def retrieve_requested_product(product_id):
    requested_product = [el for el in retrieve_all_products() if el['ProductId'] == product_id]
    print(requested_product)
    return requested_product
