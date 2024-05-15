class Bank():
    def __init__(self):
        self.storage = {}
        self.id_generator_obj = self.id_generator()

    def id_generator(self):
        current_id = 1
        while True:
            yield current_id
            current_id += 1

    def create_account(self, owner, initial_balance=0):
        account_id = next(self.id_generator_obj)
        new_storage_record = {'owner': owner, 'balance': initial_balance}
        print(
            f'Your account has been created. Name: {new_storage_record["owner"]}, Balance: {new_storage_record["balance"]}')
        self.storage[account_id] = new_storage_record
        return account_id

    def transfer(self, from_account_id, to_account_id, amount):
        if self.storage[from_account_id] and self.storage[to_account_id]:
            sender_record = self.storage[from_account_id]
            getter_record = self.storage[to_account_id]
            if sender_record['balance'] >= amount:
                sender_record['balance'] -= amount
                getter_record['balance'] += amount
            else:
                print("Insufficient funds for transfer")
        else:
            print("Invalid account ID")

    def get_account_balance(self, account_id):
        if account_id in self.storage:
            print(self.storage[account_id]['balance'])
        else:
            print("Invalid account ID")

    def get_all_accounts(self):
        for i in range(1, len(self.storage) + 1):
            print(self.storage[i])

    def deposit(self, account_id, amount):
        if account_id in self.storage:
            account = self.storage[account_id]
            account['balance'] += amount


bank = Bank()
acc1_id = bank.create_account('Yaroslav')  # id = 1
acc2_id = bank.create_account('Nikita')  # id = 2
bank.deposit(acc1_id, 1000)
bank.deposit(acc2_id, 2000)
bank.transfer(acc1_id, acc2_id, 500)
bank.get_account_balance(acc2_id)
bank.get_all_accounts()