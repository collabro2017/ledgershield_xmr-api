const Wallet = require("monero-nodejs");

class MoneroWallet extends Wallet {

    constructor(host, port, username, passord) {
        super(host, port, username, passord);
    }
}

module.exports = MoneroWallet;