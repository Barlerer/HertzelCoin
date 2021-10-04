from json.encoder import JSONEncoder
from typing import List
import json
import hashlib
from src.transaction import Transaction
from time import time


class Block:

    def __init__(self, block_id: int, prev_block_hash, transactions: List[Transaction], time=time()) -> None:
        self.block_id = block_id
        self.prev_block_hash = prev_block_hash
        self.transactions = transactions
        self.time = time

    def jsonify(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def hash(self):
        return hashlib.sha256(self.jsonify().encode()).hexdigest()

    def __str__(self) -> str:
        return f"Block number {self.block_id} with {len(self.transactions)} transactions"
