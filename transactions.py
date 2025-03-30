import datetime
import csv
import os
import matplotlib.pyplot as plt
class Transaction:
    
    def __init__(self, amount = 0, note = None, category = None, account = None):

        current_time = datetime.datetime.now()
        self.date = current_time.strftime("%Y-%m-%d %H:%M:%S")

        self.amount = amount

        self.note = note

        self.account = account

        self.category = category
    

    def process(self):
        # Print transaction details
        print(f'Date : {self.date}\nAmount : ${self.amount}\nNote : {self.note}\nAccount : {self.account}\nCategory : {self.category}\n')
        
        # Write to CSV file
        csv_file = 'transactions.csv'
        file_exists = os.path.exists(csv_file)
        
        with open(csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                # Write headers if file is new
                writer.writerow(['Date', 'Amount', 'Note', 'Category', 'Account'])
            # Write transaction data
            writer.writerow([self.date, self.amount, self.note, self.category, self.account])

entry1 = Transaction(amount=150, note="chocolate", category='food', account='UPI')
entry2 = Transaction(amount=65,note="notebook",category='Education', account='Cash')
entry3 = Transaction(amount=115,note="wall sticker",category='Household', account='Card')
entry4 = Transaction(amount=170, note="ice cream", category='food', account='UPI')

entry1.process()
entry2.process()
entry3.process()
entry4.process()

class categorization:
    pass


class FinanceTracker:
    def __init__(self):
        self.transactions = []  # Stores all transactions
    
    def load_transactions(self, file):
    # Read file and store transactions in self.transactions
        try:
            with open(file, 'r') as trns:
                reader =  csv.DictReader(trns)
                for row in reader:
                    self.transactions.append(row)
            print("successfully loaded")
        except FileNotFoundError:
            print("File not found")

    def generate_report(self):
        category_totals = {}
        for transaction in self.transactions:
            category = transaction.get('Category', 'Uncategorized')
            amount = float(transaction['Amount'])
            category_totals[category] = category_totals.get(category, 0) + amount
        
        # Create pie chart
        plt.figure(figsize=(10, 6))
        plt.subplot(1, 2, 1)
        plt.pie(category_totals.values(), 
                labels=category_totals.keys(),
                autopct='%1.1f%%',
                startangle=90)
        plt.title('Expense Distribution by Category')
        
        # Create bar chart
        plt.subplot(1, 2, 2)
        plt.bar(category_totals.keys(), category_totals.values())
        plt.xticks(rotation=45)
        plt.title('Expenses by Category')
        plt.ylabel('Amount ($)')
        
        # Adjust layout and display
        plt.tight_layout()
        plt.show()
    
    def save_transactions(self, filename):
        """Save categorized transactions to a JSON file."""
        # Write self.transactions to JSON

tracker = FinanceTracker()
tracker.load_transactions('transactions.csv')
tracker.generate_report()

