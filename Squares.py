
# move towards (dx, dy), but wrap to the size of arr
def add_and_normalize(arr, x, y, dx, dy):

    new_x = (x + dx) % len(arr[0])
    new_y = (y + dy) % len(arr)

    return new_x, new_y


# test squares in the giving array, starting at start_x, start_y
def test_array(arr, start_x, start_y):

    # find our target colour
    target = arr[start_y][start_x]

    # visited set starts with the starting cell
    visited = set()

    # and the matching set is also that starting cell
    matching = set()

    to_visit = set()
    to_visit.add((start_x, start_y))

    while len(to_visit) > 0:

        # pop a cell to visit
        check_x, check_y = to_visit.pop()
        visited.add((check_x, check_y))

        # if it's not a match, don't do anything
        if arr[check_y][check_x] != target:
            continue

        # it's a match!
        matching.add((check_x, check_y))

        # look in each direction
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:

            # move in that direction, wrapping as we go
            temp_x, temp_y = add_and_normalize(arr, check_x, check_y, dx, dy)

            # if haven't visited and not alrady a match, visit it next
            if (temp_x, temp_y) not in matching and (temp_x, temp_y) not in visited:
                to_visit.add((temp_x, temp_y))

    return len(matching)


# read a file and test it, starting at the given coords
def test_squares(file_name, start_x, start_y):
    with open(file_name) as f:
        content = f.readlines()
    arr = [lin.strip() for lin in content]

    result = test_array(arr, start_x, start_y)
    print(f'test_squares("{file_name}", {start_x}, {start_y}) = {result}')


def main():
    test_squares("TopLeft.txt", 0, 0)
    test_squares("TopLeft.txt", 3, 3)

    test_squares("TopRight.txt", 0, 0)
    test_squares("TopRight.txt", 3, 3)

    test_squares("BottomLeft.txt", 0, 0)
    test_squares("BottomLeft.txt", 1, 1)
    test_squares("BottomLeft.txt", 2, 2)
    test_squares("BottomLeft.txt", 3, 3)

    test_squares("BottomRight.txt", 0, 0)
    test_squares("BottomRight.txt", 1, 1)
    test_squares("BottomRight.txt", 3, 3)

main()