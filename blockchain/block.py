import hashlib
import time

class block:
    def __init__(self, index, prev_hash, transactions, nonce=0, timestamp=None):
        self.index = index
        self.prev_hash = prev_hash
        self.transactions = transactions  # list of transaction strings
        self.nonce = nonce
        self.timestamp = timestamp or time.time()
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha512()
        sha.update(str(self.index).encode('utf-8'))
        sha.update(self.prev_hash.encode('utf-8'))
        sha.update(''.join(self.transactions).encode('utf-8'))
        sha.update(str(self.nonce).encode('utf-8'))
        sha.update(str(self.timestamp).encode('utf-8'))
        return sha.hexdigest()
