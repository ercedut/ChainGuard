from blockchain.block import block

class chain:
    def __init__(self):
        self.blocks = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = block(index=0, prev_hash='0', transactions=['genesis'])
        self.blocks.append(genesis_block)

    def get_last_block(self):
        return self.blocks[-1]

    def add_block(self, new_block):
        new_block.prev_hash = self.get_last_block().hash
        new_block.hash = new_block.calc_hash()
        self.blocks.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.blocks)):
            curr = self.blocks[i]
            prev = self.blocks[i - 1]
            if curr.hash != curr.calc_hash():
                return False
            if curr.prev_hash != prev.hash:
                return False
        return True
