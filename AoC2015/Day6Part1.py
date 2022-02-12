import re

grid = [[0 for x in range(1000)] for y in range(1000)]
directions = open('day6input')


def change_lights(operation, x, y):
    for row in range(x[0], x[1]):
        for col in range(y[0], y[1]):
            if operation == 'turnon':
                grid[row][col] = 1
            elif operation == 'turnof':
                grid[row][col] = 0
            else:
                # XOR current value in grid for "toggle"
                grid[row][col] = grid[row][col] ^ 1


def count_lights():
    print(sum(x.count(1) for x in grid))


def day6():
    for line in directions:
        command = line[0:7].replace(" ", "")
        numbers = re.split("[^0-9]+", line)

        x_coord = [int(numbers[1]), int(numbers[3]) + 1]
        y_coord = [int(numbers[2]), int(numbers[4]) + 1]

        change_lights(command, x_coord, y_coord)

    count_lights()


day6()
