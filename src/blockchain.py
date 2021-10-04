from src.block import Block


class Blockchain:
    def __init__(self) -> None:
        self.blocks = []
        self._create_initial_block()

    def add_block(self, block: Block) -> Block:
        if not self.blocks:
            self.blocks.append(block)
            return block
        latest_block = self.get_latest_block()
        if latest_block.block_id + 1 != block.block_id:
            raise BlockIDMismatch(block.block_id, latest_block.block_id + 1)
        if latest_block.hash() != block.prev_block_hash:
            raise BlockHashMismatch()
        self.blocks.append(block)
        return block

    def get_latest_block(self):
        return self.blocks[-1]

    def _create_initial_block(self):
        initial_block = Block(0, "initial hash", [])
        self.add_block(initial_block)


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
