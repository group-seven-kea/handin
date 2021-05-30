import database

client = database.connect()["bank"]["bank_accounts"]

class BankAccount:
    def __init__(self, type, balance):
        self.type = type
        self.balance = balance
        self.transactions = []
    
    def store_account(self):
        return client.insert_one(self.create_account_object())

    def create_account_object(self):
        return {"account_type": self.type, "balance": self.balance, "transactions": self.transactions}
