from src.block import Block


class Blockchain:
    def __init__(self) -> None:
        self.blocks = []
        self._create_initial_block()

    def add_block(self, block: Block):
        self.blocks.append(block)

    def get_latest_block(self):
        return self.blocks[-1]

    def _create_initial_block(self):
        initial_block = Block(0, "initial hash", [])
        self.add_block(initial_block)
