
# file_operations.py
import pandas as pd

def save_transactions_to_csv(data):
    """
    Saves the DataFrame to a CSV file.
    Prompts user for filename.
    """
    filename = input("Enter filename to save the transactions (e.g., transactions.csv): ").strip()
    
    if not filename:
        print("Error: Filename cannot be empty.")
        return
    
    if not filename.endswith('.csv'):
        filename += '.csv'
    
    try:
        data.to_csv(filename, index=False)
        print(f"\n✓ Success! Transactions saved to '{filename}'")
        print(f"Total transactions saved: {len(data)}")
    except Exception as e:
        print(f"\n✗ Error saving file: {e}")

