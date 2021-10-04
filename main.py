import json
from src.blockchain import Blockchain
from src.block import Block
from src.transaction import Transaction


def main():
    t = Transaction("Bar", "John", "2HC")
    blockchain = Blockchain()
    initial_block = blockchain.get_latest_block()
    block = Block(1, initial_block.hash(), [t])
    blockchain.add_block(block)

    print(block.prev_block_hash)
    print(block.hash())


if __name__ == "__main__":
    main()
