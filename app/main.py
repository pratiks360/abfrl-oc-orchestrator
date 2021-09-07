from typing import Any, Dict

import requests
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.post("/genie")
def root(request: Dict[Any, Any]):
    operation = request.get("operation")
    print(operation)
    if operation is None:
        return "please provide an operation"

    params = request.get("params")
    if params is None:
        return "please provide operation params"
    print(params)
    resp = executor(operation, params)
    return  resp
my_headers = {'x-api-key': 'cognitive_fAshIon_developer'}
def executor(operation, params):

    if operation == "text_search":
        base_url = "http://nls-abfrl.dteroks-662001we93-2srzf-4b4a324f027aea19c5cbc0c3275c4656-0000.che01.containers.appdomain.cloud/v1/catalog/abfrl/text_search"
        query = dict()
        query["query_text"] = params.get("query_text")
        r = requests.get(base_url, params=query, headers=my_headers)
        resp1 = r.json()
        products = resp1.get("products")
        mainarr = []

        for x in products:
            id=x.get("id")
            print(id)
            product=getProduct(id)
            image_url = product.get("data").get("images").get("1").get("image_url")
            main_resp = dict()
            main_resp['id'] = id
            main_resp['url'] = image_url
            mainarr.append(main_resp)



        return mainarr

    if operation == "product":
        id = params.get("id")
        return getProduct(id)

    if operation == "user_preferences":

        return {
        "name": "Amit Sharma",
        "color": "black, white, red",
        "birthday": "10-oct-1977",
        "outfits": "indian, kutra, jeans",
        "budget_min": 400,
        "budget_min": 5000,
        "age": 30,
        "height": 6.1,
        "location": "mumbai"
    }

def getProduct(id):
    base_url = "http://cf-api-catalog-abfrl.dteroks-662001we93-2srzf-4b4a324f027aea19c5cbc0c3275c4656-0000.che01.containers.appdomain.cloud/v1/catalog/abfrl/products/"
    base_url = base_url+str(id)
    r = requests.get(base_url, headers=my_headers)
    return r.json()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)