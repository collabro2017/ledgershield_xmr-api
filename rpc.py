import json

import requests
from config import RPC_CONFIG


class MoneroRPC:

    def __init__(self):

        self.url = RPC_CONFIG['SERVER']
        self.headers = {
            'content-type': 'application/json'
        }
        self.rpc_data = {"jsonrpc": "2.0", "id": 0}
        self.auth = requests.auth.HTTPDigestAuth(RPC_CONFIG['USER'], RPC_CONFIG['PASS'])

    def call(self, method, params=None):

        self.rpc_data.update({'method': method})

        if params:
            self.rpc_data.update({'params': params})

        r = requests.post(
            url=self.url,
            data=json.dumps(self.rpc_data),
            headers=self.headers,
            auth=self.auth
        )

        if r.status_code == 200:
            return True, r.json()['result']

        return False, r.text

    def get_height(self):
        ok, data = self.call('getheight')
        if ok:
            return data['height']
        return 0;

    def get_integrated_address(self):
        ok, data = self.call('make_integrated_address', {'payment_id': ''})

        if ok:
            return data
        return None

    def get_payments(self, payment_id):
        ok, data = self.call('get_payments', {'payment_id': payment_id})

        if ok:
            return data
        return None

    def transfer(self, destinations, payment_id=None):
        payment_obj = {
            'destinations': destinations,
            'mixin': 4,
            'get_tx_key': True
        }
        if payment_id:
            payment_obj.update({'payment_id': payment_id})
        # return True, {'tx_hash': 'this is transaction hash'}

        ok, data = self.call('transfer', payment_obj)
        return ok, data
