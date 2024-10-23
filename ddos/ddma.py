class ddos_node:
    def __init__(self, node_id, capacity_limit):
        self.node_id = node_id
        self.capacity_limit = capacity_limit
        self.traffic = {}  # source_ip: request_count

    def receive_request(self, source_ip):
        self.traffic[source_ip] = self.traffic.get(source_ip, 0) + 1
        if self.traffic[source_ip] > self.capacity_limit:
            self.block_source(source_ip)
        else:
            self.process_request(source_ip)

    def process_request(self, source_ip):
        # Placeholder for processing logic
        pass

    def block_source(self, source_ip):
        # Logic to block the source and share info with other nodes
        pass

    def reset_traffic(self):
        self.traffic.clear()
