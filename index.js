const MoneroWallet = require("./monero_wallet");


const host = "127.0.0.1";
const port = 18032
const user  = "admin"
const password = "admin123"

const wallet = new MoneroWallet(host, port, user, password);

wallet.address().then((res)=> {
    console.log(res)
}, (err) => {
    console.log(err)
})

wallet.integratedAddress().then((res) => {
    console.log(`Integrated Address: ${res.integrated_address}`)
    console.log(`Payment ID: ${res.payment_id}`)
}, (err) => {
    console.log(err)
})

wallet.height().then((res) => {
    console.log(res);
}, (err) => {
    console.log(err);
})

wallet.getBulkPayments('43c667ef11a6c5cf').then((res) => {
    console.log(res)
}, (err) => {
    console.log(err)
})


wallet.balance().then((res) => {
    console.log(res)
}, err => {
    console.log(err)
})
// console.log(address)
