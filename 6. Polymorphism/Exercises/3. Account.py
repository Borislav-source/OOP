class Account:
    def __init__(self, owner: str, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __getattr__(self, item):
        return self._transactions

    def __repr__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __len__(self):
        return len(self._transactions)

    def repr(self):
        return f'Account({self.owner}, {self.amount})'

    def add_transaction(self, amount):
        if type(amount) is not int:
            raise ValueError("please use int for amount")
        self._transactions.append(amount)
        self.amount += amount

    @property
    def balance(self):
        return self.amount

    @property
    def acc(self):
        return self._transactions

    def validate_transaction(self, account, amount_to_add: int):
        if amount_to_add > account.amount:
            raise ValueError("sorry cannot go in debt!")
        self.amount -= amount_to_add
        self._transactions.append(amount_to_add)
        return f'New balance: {account.amount}'


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
# for transaction in acc:
#     print(transaction)
# print(acc[1])
# print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
# print(acc >= acc2)
# print(acc < acc2)
# print(acc <= acc2)
# print(acc == acc2)
# print(acc != acc2)
# acc3 = acc + acc2
# print(acc3)
# print(acc3._transactions)
