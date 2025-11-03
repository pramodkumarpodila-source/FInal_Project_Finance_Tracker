import pandas as pd

def save_transactions_to_csv(data):
    """
    Save DataFrame to CSV file (with user-supplied name).
    """
    filename = input("Enter filename to save transactions (e.g., mydata.csv): ").strip()
    if not filename.endswith('.csv'):
        filename += '.csv'

    try:
        data.to_csv(filename, index=False)
        print(f"✓ Saved to {filename} ({len(data)} records)")
    except Exception as e:
        print(f"Error saving file: {e}")

def load_transactions_from_csv():
    """
    Load a DataFrame from a CSV file.
    """
    filename = input("Enter CSV filename to load: ").strip()
    try:
        df = pd.read_csv(filename)
        print(f"✓ Loaded {len(df)} records from {filename}")
        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        return pd.DataFrame()
