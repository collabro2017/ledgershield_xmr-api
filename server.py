from flask import Flask
from flask_restful import Api
import resources

app = Flask(__name__)

api = Api(app)

api.add_resource(resources.Welcome, '/')
api.add_resource(resources.IntegratedAddress, '/wallet/new')
api.add_resource(resources.WalletPayments, '/wallet/info/<payment_id>')
api.add_resource(resources.WalletTransfer, '/wallet/transfer')

if __name__ == '__main__':
    app.run(debug=True)
