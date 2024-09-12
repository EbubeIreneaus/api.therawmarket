from typing import List
from ninja import NinjaAPI
from models.products import products
from FDM.classes import ProductResponse

api = NinjaAPI()


@api.get("/product", response={200: ProductResponse})
def get_product(request, start: int = 0, limit: int = 20):
    try:
        product = products
        return 200, {"status": "success", "data": product}
    except Exception as e:
        return {"status": "failed", "code": str(e)}


@api.get("/filter_product", response={200: ProductResponse, 400: str})
def filter_product(
    request, cat: str | None = None, minAmount: int = 5000, maxAmount: int = 100000
):
    print(type(cat))

    print("hello world")
    try:

        product = filter(
            lambda p: p["discount_price"] >= minAmount <= maxAmount
            and (
                cat == "null"
                or any(cat in p["category"].split(" ") for cat in cat.split(","))
            ),
            products,
        )
        return 200, {"status": "success", "data": product}
    except Exception as e:
        return {"status": "failed", "code": str(e)}


@api.get("/cart_product", response={200: ProductResponse})
def cart_product(request, cart_ids: str = ""):
    try:
        product = filter(lambda p: str(p["id"]) in cart_ids.split(","), products)
        return 200, {"status": "success", "data": product}
    except Exception as e:
        return {"status": "failed", "code": str(e)}


@api.get("/single_product")
def get_single_product(request, id):
    try:
        for p in products:
            if p["id"] == int(id):
                return {"status": "success", "data": p}
        return {"status": "failed", "code": 404}
    except Exception as e:
        {"status": "failed", "code": e}


@api.get("/related_product", response={200: ProductResponse})
def get_related_product(request, id):
    try:
        cat = []
        for p in products:
            if p["id"] == int(id):
                cat = p["category"].split(" ")
        if len(cat) > 0:
            r_product = filter(lambda p: True, products)
            return 200, {"status": "success", "data": r_product}
        return {"status": "failed", "code": 404}
    except Exception as e:
        return {"status": "failed", "code": str(e)}
