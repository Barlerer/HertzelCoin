from src.block import Block
from src.blockvalidator import BlockValidator


class BlockValidatorImpl(BlockValidator):
    def validate_block(self, block: Block, last_block: Block):
        if last_block.block_id + 1 != block.block_id:
            raise BlockIDMismatch(block.block_id, last_block.block_id + 1)
        if last_block.hash() != block.prev_block_hash:
            raise BlockHashMismatch()


class BlockIDMismatch(Exception):
    def __init__(self, block_id, expected_id, *args: object) -> None:
        self.block_id = block_id
        self.expected_id = expected_id
        super().__init__(*args)

    def __str__(self) -> str:
        return f"Non-consecutive block-id numbers! expected: {self.expected_id} but received: {self.block_id}"


class BlockHashMismatch(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return "Block hash does not match previous hash"
