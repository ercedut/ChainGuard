from blockchain.chain import chain
from blockchain.block import block
from consensus.dpov import node, dpov
from ddos.ddma import ddos_node
from ecc.ecc import elliptic_curve, ecc_keypair

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    # Initialize blockchain
    my_chain = chain()

    # Dynamic input for transactions
    num_transactions = get_valid_int("Enter number of transactions: ")
    transactions = []
    for _ in range(num_transactions):
        tx = input("Enter transaction data: ")
        transactions.append(tx)

    # Create new block with user input
    new_block = block(
        index=len(my_chain.blocks),
        prev_hash='',
        transactions=transactions
    )
    my_chain.add_block(new_block)

    # Display blockchain status
    print("\nBlockchain:")
    for blk in my_chain.blocks:
        print(f"Block {blk.index}: {blk.transactions}")

    # Initialize nodes for DPoV
    num_nodes = get_valid_int("\nEnter number of nodes: ")
    nodes = []
    for i in range(num_nodes):
        node_id = input(f"Enter ID for node {i+1}: ")
        capacity = get_valid_int(f"Enter capacity for node {node_id}: ")
        nodes.append(node(node_id=node_id, capacity=capacity))

    # Get network load dynamically
    network_load = get_valid_int("Enter current network load: ")

    # DPoV consensus
    consensus = dpov(nodes=nodes, network_load=network_load)
    tasks = consensus.assign_tasks()
    print("\nTask assignments:")
    for nid, tload in tasks.items():
        print(f"Node {nid}: Task load {tload}")

    # DDoS Mitigation
    ddos_nodes = []
    for n in nodes:
        ddos_nodes.append(ddos_node(node_id=n.node_id, capacity_limit=100))

    # Simulate receiving requests
    print("\nSimulating network requests...")
    while True:
        source_ip = input("Enter source IP (or 'stop' to end): ")
        if source_ip.lower() == 'stop':
            break
        for dn in ddos_nodes:
            dn.receive_request(source_ip)

    # ECC Key Generation
    print("\nECC Key Generation:")
    curve = elliptic_curve(a=2, b=3, p=97)
    base_point = (3, 6)
    if not curve.is_on_curve(*base_point):
        print("Base point is not on the curve.")
        return

    keypair = ecc_keypair(curve=curve, base_point=base_point)
    print(f"Private Key: {keypair.private_key}")
    print(f"Public Key: {keypair.public_key}")

if __name__ == "__main__":
    main()
