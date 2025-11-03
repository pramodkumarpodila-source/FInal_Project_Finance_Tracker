class FinanceAnalysis:
    def __init__(self, df):
        self.data = df

    def total_expenses(self):
        total = self.data[self.data['type'].str.lower() == 'expense']['amount'].sum()
        print(f"Total Expenses: {total:.2f}")

    def total_income(self):
        total = self.data[self.data['type'].str.lower() == 'income']['amount'].sum()
        print(f"Total Income: {total:.2f}")

    def category_summary(self):
        cat_totals = self.data.groupby('category')['amount'].sum().sort_values(ascending=False)
        print("\n--- Total by Category ---")
        print(cat_totals)

    def monthly_summary(self):
        df = self.data.copy()
        df['month'] = df['date'].dt.to_period('M')
        summary = df.groupby(['month', 'type'])['amount'].sum().unstack().fillna(0)
        print("\n--- Monthly Income/Expense ---")
        print(summary)

    def top_spending_category(self):
        spending = self.data.groupby('category')['amount'].sum()
        top = spending.idxmax()
        print('--- Top Spending Category ---')
        print(f'{top} with {spending[top]:.2f} total spending.')

    def average_monthly_spending(self):
        df = self.data.copy()
        df['month'] = df['date'].dt.to_period('M')
        monthly = df.groupby('month')['amount'].sum()
        avg_monthly = monthly.mean()
        print('--- Average Monthly Spending ---')
        print(avg_monthly)

if __name__ == "__main__":
    from import_data import DataImportCleaning
    handler = DataImportCleaning()
    handler.import_data()
    if handler.data is not None:
        analysis = FinanceAnalysis(handler.data)
        analysis.total_expenses()
        analysis.total_income()
        analysis.category_summary()
        analysis.monthly_summary()
        analysis.average_monthly_spending()
        analysis.top_spending_category()
