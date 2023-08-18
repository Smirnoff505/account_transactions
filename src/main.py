import datetime
from src.utils import load_operation, last_five_transactions, amount, date_formation, hide_number_from, hide_number_to

transactions = load_operation()

last_transactions = last_five_transactions(transactions)

for transaction in last_transactions:
    print(date_formation(transaction), transaction['description'])
    print(hide_number_from(transaction), hide_number_to(transaction))
    print(amount(transaction))
    print()


