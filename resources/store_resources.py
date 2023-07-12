from flask_jwt_extended import jwt_required
from db import stores
from flask_restful import Resource, abort
from flask import request

class StoreData(Resource):
    def get(self,store_id):
            try:
                return stores[store_id]
            except KeyError:
                abort(404, message="store not found")
    
    # @jwt_required()
    def delete(self,store_id):
        if store_id not in stores:
            abort(404, message="Store {} doesn't exist".format(store_id))
        del stores[store_id]
        return {"msg":"Success"}, 201
    
    # @jwt_required()
    def put(self,store_id):
        if store_id not in stores:
            abort(404, message="Store {} doesn't exist".format(store_id))
        requestData = request.get_json()
        stores[store_id]={**requestData,"id":store_id}
        return stores[store_id], 201

