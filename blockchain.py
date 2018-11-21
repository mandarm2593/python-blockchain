blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction_value=[1]):
    blockchain.append([last_transaction_value, transaction_amount])


add_value(5)
add_value(10, get_last_blockchain_value())
add_value(1.1, get_last_blockchain_value())

print(blockchain)


