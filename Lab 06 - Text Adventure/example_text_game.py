# A text adventure game
class Room:
    """
    this class represents the rooms in the playing area
    """

    def __init__(self, name, descr, north, east, south, west, go_up, go_down):
        """ This is a method that sets up the variables in the object. """
        self.name = name
        self.description = descr
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = go_up
        self.down = go_down


def main():
    """ This is my main program function """

    # this code populates the room info
    room_list = []
    names = ['Living Room', 'Hall', 'Library', 'Dining Room', 'Kitchen', 'Office']
    descriptions = [
        'You are in a living room. There is a giant flatscreen tv and multiple colorful couches shaped'
        ' like potatoes. There are doors to the north and to the east.',
        'You are in a grand entrance hall with marble walls and floors. There is a giant glass chandelier and '
        'fifteen dogs. There are doors to the east and the west.',
        'You are in the library. You see bookshelves with color-coded books and the occasional chicken. There are doors '
        'in the north and the west.',
        'You are in the dining room. There is a giant wooden table that looks like justin bieber and chairs with nine'
        ' legs. You can smell broccoli pudding coming from the kitchen. There are doors to the north and the east',
        'You are in the kitchen. There is a broccoli pudding (ew) and a sock with a hole. The floor is covered in '
        'ketchup. You really want chipotle. There are doors to the south and the east.',
        "You are in an office. There are orange mushrooms growing out of a rocking horse (don't ask why). There are "
        'legal documents on a desk about the legalization of catnip. There are doors to the west and the south.',

    ]
    norths = [5, None, 3, 3, None, None]
    easts = [1, 2, None, None, 3, 4]
    souths = [None, None, None, 2, None, 2]
    wests = [None, 0, 1, 4, 5, 4]
    ups = [None, None, None, None, None, None]
    downs = [None, None, None, None, None, None]
    for i in range(len(names)):
        room = Room(names[i], descriptions[i], norths[i], easts[i], souths[i], wests[i], ups[i], downs[i])
        room_list.append(room)

    # this code sets the game
    current_room = 1
    done = False
    while not done:
        print(room_list[current_room].description)
        answer = input('move quickly chop chop. clickies n for north, e for east, s for south, w for west, and '
                       'q to quit: ')
        print()
        low_answer = answer.lower()
        move = low_answer[0]

        if move == 'n':
            new_room = room_list[current_room].north
            if new_room is None:
                print("womp womp you can't go that way")
            else:
                current_room = new_room
        elif move == 'e':
            new_room = room_list[current_room].east
            if new_room is None:
                print("womp womp you can't go that way")
            else:
                current_room = new_room
        elif move == 'w':
            new_room = room_list[current_room].west
            if new_room is None:
                print("womp womp you can't go that way")
            else:
                current_room = new_room
        elif move == 's':
            new_room = room_list[current_room].south
            if new_room is None:
                print("womp womp you can't go that way")
            else:
                current_room = new_room
        elif move == 'u':
            new_room = room_list[current_room].up
            if new_room is None:
                print("womp womp you can't go that way")
            else:
                current_room = new_room
        elif move == 'd':
            new_room = room_list[current_room].down
            if new_room is None:
                print("womp womp you can't go that way")
            else:
                current_room = new_room
        elif move == 'q':
            print('toodle-oo mortal')
            done = True
        else:
            print("i don't understand your question so do ten push-ups")


main()
