# You have an 8-wind compass, like this:
# You receive the direction you are facing (one of the 8 directions: N, NE, E, SE, S, SW, W, NW) and a certain degree to turn (a multiple of 45, between -1080 and 1080);
# positive means clockwise, and negative means counter-clockwise.
# Return the direction you will face after the turn.
# Examples
# "S",  180  -->  "N"
# "SE", -45  -->  "E"
# "W",  495  -->  "NE"


def direction(facing, turn):
    direction = 0
    if facing == 'NE':
        direction = 45 + turn
    elif facing == 'E':
        direction = 90 + turn
    elif facing == 'SE':
        direction = 135 + turn
    elif facing == 'S':
        direction = 180 + turn
    elif facing == 'SW':
        direction = 225 + turn
    elif facing == 'W':
        direction = 270 + turn
    elif facing == 'NW':
        direction = 315 + turn
    else:
        direction = 0 + turn
    while direction >= 360:
        direction -= 360

    if direction == 0 or direction == 360:
        return 'N'
    elif direction == 45:
        return 'NE'
    elif direction == 90:
        return 'E'
    elif direction == 135:
        return 'SE'
    elif direction == 180:
        return 'S'
    elif direction == 225:
        return 'SW'
    elif direction == 270:
        return 'W'
    elif direction == 315:
        return 'NW'
    return 0


print(direction("S", 180),  "N")
print(direction("SE", -45), "E")
print(direction("W", 495),  "NE")
