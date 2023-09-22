# import uuid
# from flask import request
# from flask import Flask
# from flask_smorest import abort
# from db import items, stores

# #python -m venv venv
# #ctrl+shift+p select interpretor with venv

# app = Flask(__name__)

# @app.get("/store")
# def gerAllStoreData():
#     return {"data":list(stores.values())}

# @app.get("/store/<string:store_id>")
# def gerStoreData(store_id):
#     try:
#         return stores[store_id]
#     except KeyError:
#         return {"status":404,"message":"store not found"}
#         # abort(404, message="store not found")

# @app.post("/store")
# def createStore():
#     requestData = request.get_json()
#     store_id = uuid.uuid4().hex
#     #https://www.geeksforgeeks.org/args-kwargs-python/
#     stores[store_id]={**requestData,"id":store_id}
#     return stores[store_id], 201

# @app.post("/item")
# def create_item():
#     requestData = request.get_json()
#     if requestData['store_id'] not in stores:
#         return {"msg":"store not found"}, 404
#     item_id = uuid.uuid4().hex
#     stores[item_id]={**requestData,"id":item_id}
#     return stores[item_id], 201 
    
# @app.get("/item")
# def gerItemsData():
#     return {"data":list(items.values())}

# @app.get("/item/<string:item_id>")
# def get_item(item_id):
#     try:
#         return items[item_id]
#     except KeyError:
#         abort(404, message="item not found")
    
    
# if __name__=="__main__":
#     app.run(host="192.168.62.1", port=8005, debug=True)





##############   NEW   ##############

from datetime import timedelta
import secrets
from flask import Flask
# from flask_jwt_extended import JWTManager
# https://flask-restful.readthedocs.io/en/latest/quickstart.html
from flask_restful import Api

from resources.all_store_resources import AllStoreData
# from resources.jwt_token_handeler import GenerateNewJWT, GenerateRefreshJWT
from resources.store_resources import StoreData

app = Flask(__name__)
api = Api(app)
    
# app.config['JWT_SECRET_KEY'] = "276422361312391064885154713925495712873" ## generate from "secrets.SystemRandom().getrandbits(128)"
# app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
# app.config['PROPAGATE_EXCEPTION'] = True
# app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

# jwt = JWTManager(app)

api.add_resource(AllStoreData,"/store")
api.add_resource(StoreData,"/store/<string:store_id>")
# api.add_resource(GenerateRefreshJWT,"/create_refresh_jwt/")
# api.add_resource(GenerateNewJWT,"/create_jwt/")


if __name__=="__main__":
    app.run(host="192.168.62.1", port=8005, debug=True)