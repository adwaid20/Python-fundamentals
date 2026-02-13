class BankError(Exception):
    def __init__(self, balance, message="Insufficient funds"):
        self.balance = balance
        self.message = message
        super().__init__(self.message)

try:
    balance = 100
    withdraw = 200
    if withdraw > balance:
        raise BankError(balance, f"Cannot withdraw {withdraw}, only {balance} available")
except BankError as e:
    print(f"Error: {e}")
    print("Balance left:", e.balance)
