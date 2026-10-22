# Sample transaction history data
transactions = [
    {"account_number": "ACC001", "type": "Deposit", "amount": 5000},
    {"account_number": "ACC002", "type": "Deposit", "amount": 15000},
    {"account_number": "ACC001", "type": "Withdrawal", "amount": 2000},
    {"account_number": "ACC003", "type": "Deposit", "amount": 25000},
    {"account_number": "ACC002", "type": "Withdrawal", "amount": 12000},  # Suspicious withdrawal
    {"account_number": "ACC003", "type": "Withdrawal", "amount": 500},
]

# Variables to track overall totals
total_deposits = 0
total_withdrawals = 0
suspicious_withdrawals = []

# Dictionary to calculate final balance per account
final_balances = {}

# Process each transaction
for tx in transactions:
    acc_num = tx["account_number"]
    tx_type = tx["type"]
    amount = tx["amount"]

    # Initialize account balance if not already present
    if acc_num not in final_balances:
        final_balances[acc_num] = 0

    if tx_type == "Deposit":
        total_deposits += amount
        final_balances[acc_num] += amount
    elif tx_type == "Withdrawal":
        total_withdrawals += amount
        final_balances[acc_num] -= amount
        
        # Identify suspicious withdrawals (> $10,000)
        if amount > 10000:
            suspicious_withdrawals.append((acc_num, amount))

# Find the account with the highest final balance
highest_balance_account = None
highest_balance = float('-inf')

for acc, bal in final_balances.items():
    if bal > highest_balance:
        highest_balance = bal
        highest_balance_account = acc

# --- Display Results ---
print("=== BANK TRANSACTION REPORT ===")
print(f"Total Deposits: ${total_deposits:,}")
print(f"Total Withdrawals: ${total_withdrawals:,}")
print("-" * 30)

print("Final Balances per Account:")
for acc, bal in final_balances.items():
    print(f"  Account {acc}: ${bal:,}")
print("-" * 30)

if highest_balance_account:
    print(f"Account with Highest Balance: {highest_balance_account} (${highest_balance:,})")
else:
    print("Account with Highest Balance: N/A")
print("-" * 30)

print("Suspicious Withdrawals (> $10,000):")
if suspicious_withdrawals:
    for acc, amount in suspicious_withdrawals:
        print(f"  [ALERT] Account {acc} withdrew ${amount:,}")
else:
    print("  None detected.")
print("=" * 30)
