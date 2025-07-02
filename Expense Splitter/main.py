def calculate_splits(total_amount: float, number_of_people: int, currency: str) -> None:
    if number_of_people < 1:
        raise ValueError('Number of people must be greater than 1.')
    
    share_per_person: float = total_amount / number_of_people

    print(f'Total expense: {currency}{total_amount:,.2f}')
    print(f'Nunmber of people: {number_of_people}')
    print(f'Each person should pay: {currency}{share_per_person:,.2f}')

def get_valid_str_input(prompt) -> str:
    while True:
        value = input(prompt)
        if value.lower() == "y" or value.lower() == "n" or value == "":
            return value
        else:
            print("Please type Y/y or enter for YES, N/n for NO")  

def get_valid_num_input(prompt) -> float:
    while True:
        try:
            value = float(input(prompt))
            if 0.0 <= value <= 100.0:
                return value
            else:
                print("Please enter a number between 0 and 100!")  
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculate_splits_new(total_amount: float, number_of_people: int, currency: str) -> None:
    if number_of_people < 1:
        raise ValueError('Number of people must be greater than 1.')
    
    decision = get_valid_str_input("Do you want even splits? (Y/n) ")
    if decision.lower() == "y" or decision == "":
        share_per_person: float = total_amount / number_of_people
        print(f'Total expense: {currency}{total_amount:,.2f}')
        print(f'Number of people: {number_of_people}')
        print(f'Each person should pay: {currency}{share_per_person:,.2f}')      
    else:
        while True:
            individual_splits: list[float] = []
            for i in range(number_of_people):
                individual_splits.append(get_valid_num_input(f"Enter % split for person {i+1}: "))
            if sum(individual_splits) == 100.0:
                break
            else: 
                print("Individual splits must sum up 100%")
        
        print(f'Total expense: {currency}{total_amount:,.2f}')
        print(f'Number of people: {number_of_people}')
        for i in range(number_of_people):
            print(f'Person {i+1} should pay: {currency}{total_amount*individual_splits[i]/100:,.2f}')   

def main() -> None:
    while True:
        try:
            total_amount: float = float(input('Enter the total amount of the expense: '))
            number_of_people: int = int(input('Enter the number of people sharing the expense: '))
            calculate_splits_new(total_amount, number_of_people, currency='€')
            break
        except ValueError as e:
            print(f'Error: {e}') 
            print("Please enter valid values.") 

if __name__ == "__main__":
    main()