from typing import List
from ninja import Schema

class Rate(Schema):
    count: int
    rate: float

class Product(Schema):
    id: int | None
    name: str
    img: str
    category: str
    price: int
    rate :Rate
    suppose_price: int
    discount_price: int
    desc: str

class ProductResponse(Schema):
    status: str
    data: List[Product]
