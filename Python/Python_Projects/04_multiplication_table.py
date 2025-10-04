"""
Multiplication Table:

To print multiples of numbers from 1 to 100

"""

try:

    while True:
        # Take input from user
        user_input = int(input("Enter a number from 1 to 100 for multiples: "))
        print(f"Multiples of {user_input} are: ")

        # For loop to print multiples from 1 to 10
        if 1 <= user_input <= 100:

            for multiples in range(1, 11):
                multiplication = user_input * multiples
                print(f"{multiples} * {user_input} = {multiplication}")

        else:
            print("Provide a number between 1 and 100")
            continue

        should_continue = input("Continue? (y/n): ").lower()

        if should_continue == "n":
            print()
            print("Thank you for playing!")
            break

except ValueError:
    print("Invalid Input")
