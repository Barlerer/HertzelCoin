import json
from src.blockchain import Blockchain
from src.block import Block
from src.blockvalidatorimpl import BlockValidatorImpl
from src.transaction import Transaction


def main():
    t = Transaction("Bar", "John", 4)

    block_validator = BlockValidatorImpl()

    blockchain = Blockchain(block_validator)
    initial_block = blockchain.get_latest_block()
    block = Block(1, initial_block.hash(), [t])
    blockchain.add_block(block)


if __name__ == "__main__":
    main()
