# from flask_jwt_extended import create_access_token,get_jwt_identity, jwt_required, create_refresh_token
# from flask_restful import Resource
# from flask import jsonify


# class GenerateNewJWT(Resource):
#     @jwt_required(refresh=True)
#     def post(cls):
#         current_user = get_jwt_identity()
#         access_token = create_access_token(identity=current_user)
#         ret_json = {
#             'Token':access_token
#         }
#         return jsonify(ret_json)
    
# class GenerateRefreshJWT(Resource):
#     def post(cls):
#         _id_toset_hash = str("aaaaaaaaaa") + "_" + "9999999"
#         access_token = create_access_token(identity=_id_toset_hash, fresh=True)
#         refresh_token = create_refresh_token(identity=_id_toset_hash)
#         ret_json = {
#             "Token": access_token,
#             "Refresh_Token": refresh_token
#         }
#         return jsonify(ret_json)
