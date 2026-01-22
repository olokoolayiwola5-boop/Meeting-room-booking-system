room_bookings = []

def book_room():
    room = input("Enter room name: ")
    date = input("Enter booking date: ")
    purpose = input("Enter meeting purpose: ")
    room_bookings.append({
        "room": room,
        "date": date,
        "purpose": purpose
    })
    print("Meeting room booked")

def view_bookings():
    if not room_bookings:
        print("No bookings found")
    else:
        for b in room_bookings:
            print("Room:", b["room"])
            print("Date:", b["date"])
            print("Purpose:", b["purpose"])
            print("------------------")

def main():
    while True:
        print("1. Book Room")
        print("2. View Bookings")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            book_room()
        elif choice == "2":
            view_bookings()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

main()
