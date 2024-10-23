class node:
    def __init__(self, node_id, capacity):
        self.node_id = node_id
        self.capacity = capacity  # computational capacity

class dpov:
    def __init__(self, nodes, network_load):
        self.nodes = nodes  # list of node instances
        self.network_load = network_load

    def total_capacity(self):
        return sum(n.capacity for n in self.nodes)

    def calc_difficulty(self):
        return self.total_capacity() / (self.network_load + 1)

    def assign_tasks(self):
        difficulty = self.calc_difficulty()
        tasks = {}
        for n in self.nodes:
            task_load = n.capacity / difficulty
            tasks[n.node_id] = task_load
        return tasks
