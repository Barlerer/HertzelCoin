class Transaction:
    def __init__(self, from_user, to_user, amount) -> None:
        self.from_user = from_user
        self.to_user = to_user
        self.amount = amount

    def __str__(self) -> str:
        return f"Transaction from {self.from_user} to {self.to_user} for the amount of {self.amount} HertzelCoin"
