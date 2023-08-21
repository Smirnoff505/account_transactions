import datetime
from src.utils import load_operation, amount, date_formation, get_executed_only, get_sorted, hide_number


def main():
    transactions = load_operation()
    operations_executed = get_executed_only(transactions)
    last_transactions = get_sorted(operations_executed)
    for transaction in last_transactions:
        print(f"{date_formation(transaction)}  {transaction['description']}")
        print(f"{hide_number(transaction.get('from'))} -> {hide_number(transaction['to'])}")
        print(amount(transaction))
        print()


main()


