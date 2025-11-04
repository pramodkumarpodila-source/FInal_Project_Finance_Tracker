from import_data import DataImportCleaning
from file_operations import save_transactions_to_csv
from analysis import FinanceAnalysis
from visualize import visualize_monthly_trend, pie_by_category, bar_by_category
import pandas as pd

def print_menu():
    print("=== MPG FinTech App ===")
    print("0. Import a CSV File")
    print("1. View All Transactions")
    print("2. View Transactions by Date Range")
    print("3. Add a Transaction")
    print("4. Edit a Transaction")
    print("5. Delete a Transaction")
    print("6. Analyze Spending by Category")
    print("7. Calculate Average Monthly Spending")
    print("8. Show Top Spending Category")
    print("9. Visualize Monthly Spending Trend")
    print("10. Visualize Expense Pie Chart")
    print("11. Visualize Category Bar Chart")
    print("12. Save Transactions to CSV")
    print("13. Exit")

def show_transactions(data):
    print('--- All Transactions ---')
    print(data.reset_index(drop=True)[['date', 'category', 'description', 'amount']])

def view_by_date_range(data):
    start = input('Enter start date (YYYY-MM-DD): ')
    end = input('Enter end date (YYYY-MM-DD): ')
    try:
        start = pd.to_datetime(start)
        end = pd.to_datetime(end)
        filtered = data[(data['date'] >= start) & (data['date'] <= end)]
        if filtered.empty:
            print('No transactions found in this date range.')
        else:
            print(f'--- Transactions from {start.date()} to {end.date()} ---')
            print(filtered[['date', 'category', 'description', 'amount']])
    except Exception as e:
        print('Invalid date input.')

def add_transaction(data):
    date = input('Enter the date (YYYY-MM-DD): ')
    category = input('Enter the category: ')
    description = input('Enter a description: ')
    amount = input('Enter the amount: ')
    type_val = input('Enter the type (Expense/Income): ')
    try:
        new_row = {
            'date': pd.to_datetime(date),
            'category': category,
            'type': type_val,
            'description': description,
            'amount': float(amount)
        }
        data.loc[len(data)] = new_row
        print('Transaction added successfully!')
    except Exception as e:
        print('Error adding transaction:', e)

def edit_transaction(data):
    idx = input('Enter the index of the transaction to edit: ')
    try:
        idx = int(idx)
        if idx < 0 or idx >= len(data):
            print('Invalid index.')
        else:
            trans = data.loc[idx]
            print('Current Transaction Details:')
            print(trans)
            date = input('Enter new date (YYYY-MM-DD) or press Enter to keep current: ')
            category = input('Enter new category or press Enter to keep current: ')
            type_val = input('Enter new type or press Enter to keep current: ')
            description = input('Enter new description or press Enter to keep current: ')
            amount = input('Enter new amount or press Enter to keep current: ')
            if date: data.at[idx, 'date'] = pd.to_datetime(date)
            if category: data.at[idx, 'category'] = category
            if type_val: data.at[idx, 'type'] = type_val
            if description: data.at[idx, 'description'] = description
            if amount: data.at[idx, 'amount'] = float(amount)
            print('Transaction updated successfully!')
    except Exception as e:
        print('Invalid input.')

def delete_transaction(data):
    idx = input('Enter the index of the transaction to delete: ')
    try:
        idx = int(idx)
        if idx < 0 or idx >= len(data):
            print('Invalid index.')
        else:
            data.drop(idx, inplace=True)
            data.reset_index(drop=True, inplace=True)
            print('Transaction deleted successfully!')
    except Exception as e:
        print('Invalid input.')

def analyze_spending(data):
    # Uses analysis class so it's always correct!
    analysis = FinanceAnalysis(data)
    analysis.category_summary()

def average_monthly_spending(data):
    analysis = FinanceAnalysis(data)
    analysis.average_monthly_spending()

def top_spending_category(data):
    analysis = FinanceAnalysis(data)
    analysis.top_spending_category()

def main():
    handler = DataImportCleaning()
    data = None
    while True:
        print_menu()
        choice = input('Choose an option (0-13): ')
        if choice == '0':
            handler.import_data()
            data = handler.data
            if data is not None and 'description' not in data.columns:
                data['description'] = ''
        elif choice == '1' and data is not None:
            show_transactions(data)
        elif choice == '2' and data is not None:
            view_by_date_range(data)
        elif choice == '3' and data is not None:
            add_transaction(data)
        elif choice == '4' and data is not None:
            edit_transaction(data)
        elif choice == '5' and data is not None:
            delete_transaction(data)
        elif choice == '6' and data is not None:
            analyze_spending(data)
        elif choice == '7' and data is not None:
            average_monthly_spending(data)
        elif choice == '8' and data is not None:
            top_spending_category(data)
        elif choice == '9' and data is not None:
            visualize_monthly_trend(data)
        elif choice == '10' and data is not None:
            pie_by_category(data)
        elif choice == '11' and data is not None:
            bar_by_category(data)
        elif choice == '12' and data is not None:
            save_transactions_to_csv(data)
        elif choice == '13':
            print('Exiting the Personal Finance Tracker. Goodbye!')
            break
        else:
            print('Invalid choice or no data loaded. Choose "0" to import CSV first.')

if __name__ == "__main__":
    main()
