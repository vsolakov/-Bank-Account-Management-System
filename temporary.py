account_holders = []
balances = []
transaction_histories = []
loans = []


account_holder_name = input("Please input you name: ")
account_holders.append(account_holder_name)
balance = 0
balances.append(balance)
transaction_history = ""
transaction_histories.append(transaction_history)
loan = 0
loans.append(loan)
print(f'Account successfully created!')


account_holder_name = input("Please input you name: ")
account_holders.append(account_holder_name)
balance = 0
balances.append(balance)
transaction_history = ""
transaction_histories.append(transaction_history)
loan = 0
loans.append(loan)
print(f'Account successfully created!')



account_holder_name = input("Please input you name: ")
if account_holder_name in account_holders:
    index = account_holders.index(account_holder_name)
    list(map(int, balances))
    deposit_amount = int(input("Please input amount to deposit: "))
    balances[index] = balances[index] + deposit_amount
    transaction_histories[index] += f'Deposited {deposit_amount} '
    print(f'Current balance: {balances[index]}')
else:
    print(f'The specified account does not exist')

account_holder_name = input("Please input you name: ")
if account_holder_name in account_holders:
    index = account_holders.index(account_holder_name)
    list(map(int, balances))
    withdraw_amount = int(input("Please input amount to withdraw: "))
    if balances[index] >= withdraw_amount:
        balances[index] = balances[index] - withdraw_amount
        transaction_histories[index] = transaction_histories[index] + f'Withdraw {withdraw_amount}'
        print(f'Current balance: {balances[index]}')
    else:
        print(f'Cannot withdraw. Insufficient funds!')
else:
    print(f'The specified account does not exist')

account_holder_name = input("Please input you name: ")
if account_holder_name in account_holders:
    index = account_holders.index(account_holder_name)
    print(f'Current balance: {balances[index]}')
else:
    print(f'The specified account does not exist')


sender_account_name = input("Input sender account name: ")
recipient_account_name = input("Input recipient account name: ")
if sender_account_name in account_holders and recipient_account_name in account_holders:
    sender_index = account_holders.index(sender_account_name)
    recipient_index = account_holders.index(recipient_account_name)
    transfer_amount = float(input("Input transfer amount: "))
    if balances[sender_index] >= transfer_amount:
        balances[sender_index] -= transfer_amount
        balances[recipient_index] += transfer_amount
        transaction_histories[sender_index] += f'Sent {transfer_amount} '
        transaction_histories[recipient_index] += f'Received: {transfer_amount} '
        print(f'Transaction successful!')
    else:
        print(f'{account_holders[sender_index]} has insufficient funds for this transfer!')
else:
    print(f'One or both of the accounts don\'t exist in the system')

if len(account_holders) != 0:
    for index, account in enumerate(account_holders):
        print(f'Account holder: {account_holders[index]}', end="; ")
        print(f'Balance: {balances[index]}', end="; ")
        print(f'Transaction_history: {transaction_histories[index]}', end="; ")
        print(f'Outstanding loans: {loans[index]}')
else:
    print(f'There are no registered accounts')
