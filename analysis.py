import pandas as pd
class Analysis:
    def __init__(self):
        pass
    def sum_categories(self, data):
        """
        Returns total spending for each category, sorted from highest to lowest.
        Only includes rows marked as 'Expense' in the type column.
        """
        expense_data = data[data['type'] == 'Expense']
        totals_category = expense_data.groupby('category')['amount'].sum().sort_values(ascending=False)
        return totals_category
    def sum_types(self, data):
        """
        Returns total amount for each transaction type (e.g., Expense, Income).
        Groups and sums by the 'type' column.
        """
        sum_type = data.groupby('type')['amount'].sum()
        return sum_type
    def average_monthly_spending(self, data):
        """
        Calculates the average monthly spending (expenses only), across all years.
        Filters for 'Expense', groups by year and month, then returns the mean total.
        """
        expense_data = data[data['type'] == 'Expense'].copy()
        expense_data['year'] = expense_data['date'].dt.year
        expense_data['month'] = expense_data['date'].dt.month
        monthly_totals = expense_data.groupby(['year', 'month'])['amount'].sum()
        return monthly_totals.mean()
    def monthly_spending_trend(self, data):
        """
        Returns total expenses for each month in each year.
        Output: pandas Series indexed by (year, month), values = amount spent.
        """
        expense_data = data[data['type'] == 'Expense'].copy()
        expense_data['year'] = expense_data['date'].dt.year
        expense_data['month'] = expense_data['date'].dt.month
        monthly_totals = expense_data.groupby(['year', 'month'])['amount'].sum()
        return monthly_totals
analyzer=Analysis()
print(analyzer.average_monthly_spending(data))
analyzer.monthly_spending_trend(data)