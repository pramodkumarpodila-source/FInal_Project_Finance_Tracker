import matplotlib.pyplot as plt

def visualize_monthly_trend(data):
    """
    Prompts user for a year and plots monthly spending for that year only.
    """
    year = input("Enter the year to visualize (e.g., 2023): ").strip()
    try:
        year = int(year)
    except ValueError:
        print("Invalid year input.")
        return

    # Filter rows to the chosen year
    data['year'] = data['date'].dt.year
    year_data = data[data['year'] == year]

    if year_data.empty:
        print(f"No data found for year {year}.")
        return

    year_data['month'] = year_data['date'].dt.month
    monthly = year_data.groupby('month')['amount'].sum()
    months = range(1, 13)
    monthly = monthly.reindex(months, fill_value=0)

    plt.plot(months, monthly.values, marker='o')
    plt.title(f'Monthly Spending Trend - {year}')
    plt.xlabel('Month')
    plt.ylabel('Total Spending')
    plt.xticks(months)
    plt.tight_layout()
    plt.show()

def pie_by_category(data):
    """
    Pie chart showing the breakdown for expenses by category.
    """
    expense_data = data[data['type'].str.lower() == 'expense']
    cat = expense_data.groupby('category')['amount'].sum()
    if cat.empty:
        print("No expense data to plot.")
        return
    plt.figure(figsize=(7,7))
    cat.plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title('Expense Distribution by Category')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()

def bar_by_category(data):
    """
    Bar chart showing total amounts by category.
    """
    cat = data.groupby('category')['amount'].sum()
    cat.plot(kind='bar')
    plt.title('Total By Category')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.tight_layout()
    plt.show()
