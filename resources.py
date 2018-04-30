from flask import make_response, jsonify
from flask_restful import Resource
import rpc

xmr_rpc = rpc.MoneroRPC()


class Welcome(Resource):

    def get(self):
        height = xmr_rpc.get_height()
        return {'height': height}


class IntegratedAddress(Resource):

    def post(self):
        data = xmr_rpc.get_integrated_address()
        return data


class WalletPayments(Resource):

    def get(self, payment_id):
        data = xmr_rpc.get_payments(payment_id)
        return data

