from src.block import Block
from src.blockvalidator import BlockValidator


class Blockchain:
    def __init__(self, validator: BlockValidator) -> None:
        self.blocks = []
        self.validator = validator
        self._create_initial_block()

    def add_block(self, block: Block) -> Block:
        if not self.blocks:
            self.blocks.append(block)
            return block
        latest_block = self.get_latest_block()
        # Will throw an expection if the wrong block is added
        self.validator.validate_block(block, latest_block)
        self.blocks.append(block)
        return block

    def get_latest_block(self):
        return self.blocks[-1]

    def _create_initial_block(self):
        initial_block = Block(0, "initial hash", [])
        self.add_block(initial_block)
