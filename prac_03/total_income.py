"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for monthly_earns over a given number of months."""
    monthly_earns = []
    months = int(input("How many months? "))

    get_monthly_income(monthly_earns, months)

    print("\nIncome Report\n-------------")
    total = 0
    shows_months_and_incomes(monthly_earns, months, total)


def shows_months_and_incomes(monthly_earns, months, total):
    for month in range(1, months + 1):
        income = monthly_earns[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


def get_monthly_income(monthly_earns, months):
    for month in range(1, months + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        monthly_earns.append(income)


main()