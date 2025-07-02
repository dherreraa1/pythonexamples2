def calculate_finances(monthly_income: float, tax_rate: float, monthly_expenses: float, currency: str) -> None:
    yearly_salary: float = monthly_income * 12
    monthly_tax: float = monthly_income * (tax_rate/100)
    yearly_tax: float = monthly_tax * 12
    monthly_net_income: float = monthly_income - monthly_tax - monthly_expenses
    yearly_net_income: float = yearly_salary - yearly_tax

    print('------------------')
    print(f"Monthly income: {currency}{monthly_income:,.2f}")
    print(f"Monthly expenses: {currency}{monthly_expenses:,.2f}")
    print(f"Tax rate: {tax_rate:,.0f}%")
    print(f"Monthly tax: {currency}{monthly_tax:,.2f}")
    print(f"Monthly net income: {currency}{monthly_net_income:,.2f}")
    print(f"Yearly salary: {currency}{yearly_salary:,.2f}")
    print(f"Yearly tax paid: {currency}{yearly_tax:,.2f}")
    print(f"Yearly net income: {currency}{yearly_net_income:,.2f}")
    print('------------------')


def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0.0:
                return value
            else:
                print("Please enter a number equal or greater than zero!")  
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main() -> None:
    monthly_income: float = get_valid_input("Enter your monthly salary: ")
    tax_rate: float = get_valid_input("Enter your tax rate (%): ")
    monthly_expenses: float = get_valid_input("Enter your monthly expenses: ")


    calculate_finances(monthly_income, tax_rate, monthly_expenses, currency = 'KR')
    
if __name__ == '__main__':
    main()