# from pydantic import validate_call

# @validate_call
# def calculate_total(prince: int, quantity: int):
#     total = prince * quantity
#     return total


# print(calculate_total("100", 2))

from pydantic import BaseModel

class Product(BaseModel):
    product_name: str 
    price: float
    instock: bool = True

product = Product(product_name="Laptop", price=1000.0, instock=False)

print(product.model_dump_json())