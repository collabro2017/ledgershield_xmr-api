import redis
from config import REDIS_CONFIG

class RedisCleint:

    def __init__(self):
        self.client = redis.StrictRedis(host=REDIS_CONFIG['HOST'], port=REDIS_CONFIG['PORT'], db=REDIS_CONFIG['DB'])


    def set_tx_status(self, txid, tx_hash):
        key = 'tx:{}'.format(txid)
        self.client.set(key, tx_hash)

    def get_tx_status(self, txid):
        key = 'tx:{}'.format(txid)
        return self.client.get(key)
