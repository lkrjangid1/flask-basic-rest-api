import uuid

from flask_jwt_extended import jwt_required
from db import stores
from flask_restful import Resource
from flask import request

class AllStoreData(Resource):
    # @jwt_required()
    def get(self):
        return {"data":list(stores.values())}, 200
    
    # @jwt_required()
    def post(self):
        requestData = request.get_json()
        store_id = uuid.uuid4().hex
        stores[store_id]={**requestData,"id":store_id}
        return stores[store_id], 201

