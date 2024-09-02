def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    # messages_list = []
    # for name in names:
    #     messages_list.append(f"Hello, my name is {name}.")

    # return messages_list
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    return [f"Hello, {name}! You'll be assigned to room {names.index(name) + 1}!" for name in names]

def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)
    for badge in badges:
       print(badge)
    for room in rooms:
       print(room)

