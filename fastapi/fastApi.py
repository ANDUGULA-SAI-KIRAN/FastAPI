from fastapi import FastAPI,HTTPException
from typing import Optional


app = FastAPI()

# basic get Http method ----------------------------------------------------------------------
@app.get('/')
def main_func():

    # business logic
    return "function accessed"



# Get HTTP with path params  -----------------------------------------------------------

users = {
    1 : {
        'name': 'suresh',
        'orders':{
            101: {'laptop': 60000, 'stand': 300},
            102: {'mobile': 30000, 'backcase': 150}
        }
    },
    2 : {
        'name': 'ramesh',
        'orders':{
            201: {'laptop': 60000, 'stand': 300},
            202: {'mobile': 30000, 'backcase': 150}
        }
    }
}

@app.get('/user/{user_id}/order/{order_id}')
def path_params(user_id: int, order_id: int):

    if user_id not in users:
        raise HTTPException(status_code=404, detail="Product id not found")
    
    return users[user_id]['orders'][order_id]



# Get HTTP with query params -------------------------------------------


products= [
        {"id": 101, "name": "Ballpoint Pen", "category": "Pens", "price": 1.50},
        {"id": 102, "name": "Gel Pen", "category": "Pens", "price": 2.20},
        {"id": 103, "name": "Fountain Pen", "category": "Pens", "price": 15.00},
        {"id": 104, "name": "Marker Pen", "category": "Pens", "price": 3.00},
        {"id": 105, "name": "Highlighter", "category": "Pens", "price": 2.80},

        {"id": 201, "name": "A4 Notebook", "category": "Notebooks", "price": 5.00},
        {"id": 202, "name": "Spiral Notebook", "category": "Notebooks", "price": 4.50},
        {"id": 203, "name": "Hardcover Notebook", "category": "Notebooks", "price": 8.00},
        {"id": 204, "name": "Pocket Notebook", "category": "Notebooks", "price": 3.00},
        {"id": 205, "name": "College Ruled Notebook", "category": "Notebooks", "price": 6.00},
        {"id": 206, "name": "Graph Notebook", "category": "Notebooks", "price": 5.50},

        {"id": 301, "name": "Wooden Pencil", "category": "Pencils", "price": 0.50},
        {"id": 302, "name": "Mechanical Pencil", "category": "Pencils", "price": 2.50},
        {"id": 303, "name": "Colored Pencils (Set)", "category": "Pencils", "price": 7.00},
        {"id": 304, "name": "HB Pencil", "category": "Pencils", "price": 0.80},
        {"id": 305, "name": "2B Pencil", "category": "Pencils", "price": 0.90},
    ]

@app.get('/query_products')
def query_params(category: Optional[str] =None, price: Optional[int] =None):

    filtered_products = products

    if category:
        filtered_products = [ p for p in filtered_products if p['category'].lower() == category.lower()]

    if price:
        filtered_products = [ p for p in filtered_products if p['price'] <= price]

    return filtered_products




@app.get('/add_/a/{a}/b/{b}')
def add_(a: int ,b: int):
    print(f"type-a: {type(a)} | type-b: {type(b)}")
    return a+b
