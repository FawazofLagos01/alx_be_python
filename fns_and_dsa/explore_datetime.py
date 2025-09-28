from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    format_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {format_date}")
    return current_date

def calculate_future_date(days_to_add):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    format_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {format_future_date}")
    return future_date

def main():
    display_current_datetime()
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()

