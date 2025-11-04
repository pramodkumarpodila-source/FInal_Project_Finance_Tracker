import pandas as pd

class DataImportCleaning:
    # These columns should be present in the csv
    Required_cols = ['date', 'category', 'type', 'amount']

    # Makes category names the same even if written differently
    Category_maps = {
        'groceries': 'Groceries',
        'food': 'Groceries',
        'salary': 'Income',
        'rent': 'Rent',
        'movie': 'Entertainment'
    }
    # Makes type names the same even if written differently
    Type_map = {
        'expense': 'Expense',
        'income': 'Income'
    }

    def __init__(self):
        self.data = None

    # Loads and cleans CSV data
    def import_data(self):
        # Ask the user where the CSV file is
        path = input("Enter CSV path: ").strip()

        # Try to load the CSV file as a pandas DataFrame
        try:
            data = pd.read_csv(path)
        except Exception as e:
            print(f"Error opening file: {e}")
            return None

        print("File loaded! First few rows:")
        print(data.head())

        # Change all column names to lowercase and underscores
        data.columns = [col.lower().replace(" ", "_") for col in data.columns]
        print("Columns after cleaning:", data.columns.tolist())
        # If the CSV uses 'transaction_description', rename it to 'description' for consistency throughout the app
        if 'transaction_description' in data.columns:
            data['description'] = data['transaction_description']
            data.drop(columns=['transaction_description'], inplace=True)


        # Check that all required columns are present
        for col in self.Required_cols:
            if col not in data.columns:
                print(f"Missing required column: {col}")
                return None
        print("All required columns are present!")

        # Convert 'date' column to datetime
        data['date'] = pd.to_datetime(data['date'], errors='coerce')
        # Convert 'amount' column to numeric
        data['amount'] = pd.to_numeric(data['amount'], errors='coerce')
        print("Sample dates after conversion:", data['date'].head())
        print("Sample amounts after conversion:", data['amount'].head())

        # Standardize 'category' and 'type' columns
        data['category'] = data['category'].str.strip().str.lower().map(self.Category_maps).fillna(data['category'].str.strip().str.title())
        data['type'] = data['type'].str.strip().str.lower().map(self.Type_map).fillna(data['type'].str.strip().str.title())

        # If any row's category is 'salary', make sure type is 'Income'
        data.loc[data['category'].str.lower() == 'salary', 'type'] = 'Income'
        print("Sample categories after clean:", data['category'].unique())
        print("Sample types after clean:", data['type'].unique())

        # Remove rows with missing required info
        before_drop = len(data)
        data = data.dropna(subset=self.Required_cols)
        print(f"Removed {before_drop - len(data)} rows with missing info.")

        # Remove duplicate rows
        dupes = data.duplicated().sum()
        if dupes > 0:
            print(f"Removed {dupes} duplicate rows.")
            data = data.drop_duplicates()

        # Remove rows where 'amount' is zero or negative
        negs = data[data['amount'] <= 0].shape[0]
        if negs > 0:
            print(f"Removed {negs} rows where 'amount' was zero or negative.")
            data = data[data['amount'] > 0]

        # Warn if any categories/types are not recognized
        unknown_cats = set(data['category'].unique()) - set(self.Category_maps.values())
        if unknown_cats:
            print(f"Warning: Unknown categories found: {unknown_cats}")
        unknown_types = set(data['type'].unique()) - set(self.Type_map.values())
        if unknown_types:
            print(f"Warning: Unknown transaction types found: {unknown_types}")

        # Save clean data
        self.data = data
        print("Data cleaning complete!\n")

    # Optional: Print a summary of the cleaned data
    def report(self):
        if self.data is None:
            print("No data loaded.")
        else:
            print("Rows, Columns:", self.data.shape)
            print(self.data.head())
            print("Column Types:\n", self.data.dtypes)
            print("Amount Stats:\n", self.data['amount'].describe())
            print("Categories:", self.data['category'].unique())
            print("Types:", self.data['type'].unique())

# Example usage
if __name__ == "__main__":
    handler = DataImportCleaning()
    handler.import_data()
    handler.report()
