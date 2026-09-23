def show_rooms():
    print("\nRoom Status:")
    for room, guest in rooms.items():
        print(f"  {room} -> {guest if guest else 'empty'}")

def book(room, name):
    if room not in rooms:
        print("no such room")
    elif rooms[room]:
        print(f"room {room} already taken by {rooms[room]}")
    else:
        rooms[room] = name
        print(f"booked room {room} for {name}")

def checkout(room):
    if rooms.get(room):
        print(f"{rooms[room]} checked out of room {room}")
        rooms[room] = None
    else:
        print("that room's already empty")

while True:
    print("\n1) show rooms  2) book  3) checkout  4) quit")
    ch = input("> ")

    if ch == "1":
        show_rooms()
    elif ch == "2":
        r = int(input("room no: "))
        n = input("guest name: ")
        book(r, n)
    elif ch == "3":
        r = int(input("room no: "))
        checkout(r)
    elif ch == "4":
        print("bye!")
        break
    else:
        print("try again")
