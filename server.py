from flask import Flask, jsonify, request, make_response
from flask_restful import Api
import resources, rpc, redisclient

app = Flask(__name__)

api = Api(app)

api.add_resource(resources.Welcome, '/')
api.add_resource(resources.IntegratedAddress, '/wallet/new')
api.add_resource(resources.WalletPayments, '/wallet/info/<payment_id>')
# api.add_resource(resources.WalletTransfer, '/wallet/transfer')


xmr_rpc = rpc.MoneroRPC()
redis_client =  redisclient.RedisCleint()

@app.route('/wallet/transfer', methods=['POST'])
def transfer():
    if request.is_json:
        data = request.get_json()
        if data:
            txid = data['txid']
            tx_hash = redis_client.get_tx_status(txid)
            if tx_hash is None:
                outputs = data['outs']
                error = False
                destinations = []
                for out in outputs:
                    amount = out['amount']
                    if isinstance(amount, str) and amount.isnumeric():
                        amount =  int(amount)

                    if amount > 0:
                        destinations.append({'address': out['address'], 'amount': amount})
                    else:
                        error = True
                        break

                if not error:
                    ok, data = xmr_rpc.transfer(destinations, None)
                    if ok:
                        tx_hash = data['tx_hash']
                        redis_client.set_tx_status(txid, tx_hash)
                        res_out = []
                        for o in outputs:
                            res_out.append({**o, **{'tx_hash': tx_hash}})
                        return jsonify(res_out)
                    else:
                        return make_response(jsonify(data="Unable to process request at this time!"), 400)
                else:
                    return make_response(jsonify(data="Invalid request!"), 400)
            else:
                return make_response(jsonify(data="Duble spend!"), 409)
    else:
        return make_response(jsonify(data="Invalid content-type header value, please set application/json"), 400)

if __name__ == '__main__':
    app.run(debug=True)
