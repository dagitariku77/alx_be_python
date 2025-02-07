# explore_datetime.py

import datetime

def display_current_datetime():
    """Displays the current date and time in a readable format."""
    current_datetime = datetime.datetime.now()
    print(f"Current date and time: {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_datetime.date() # Return the date part


def calculate_future_date(current_date):
    """Calculates and displays a future date based on user input."""
    try:
        num_days = int(input("Enter the number of days to add to the current date: "))
        if num_days < 0:
            print("Number of days must be non-negative.")
            return

        future_date = current_date + datetime.timedelta(days=num_days)
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")


if __name__ == "__main__":
    current_date = display_current_datetime()
    calculate_future_date(current_date)