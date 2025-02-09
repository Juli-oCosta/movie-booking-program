seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def show_seats(seats):
    print("\nCurrent seat status:")
    for seat in seats:
        if isinstance(seat, int):
            print(f"Available: {seat}")
        else:
            print(f"Reserved: {seat[1]}")

def book_seat(seats):
    while True:
        try:
            choice = int(input("\nEnter the seat number you want to book: "))

            if choice not in seats:
                print("\nInvalid or already reserved seat. Please try again.")
                continue

            index = seats.index(choice)
            seats[index] = ("Reserved", choice)
            print(f"\nSeat {choice} successfully reserved!")
            break

        except ValueError:
            print("\nPlease enter a valid number.")

show_seats(seats)
book_seat(seats)
show_seats(seats)
