from flask_restful import Resource, reqparse
import rpc

xmr_rpc = rpc.MoneroRPC()

parser = reqparse.RequestParser()
parser.add_argument('payment')


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
        return {'response': data}


class WalletTransfer(Resource):

    def post(self):
        args = parser.parse_args()
        ok, data = xmr_rpc.transfer(args.dest, args.payment_id)
        return  data
