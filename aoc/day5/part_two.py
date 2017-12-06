def steps_to_leave_part_two(maze):
    steps = 0
    from_position = 0
    while 0 <= from_position < len(maze):
        from_position = jump(maze, from_position)
        steps += 1

    return steps


def jump(maze, from_position):
    position = from_position + maze[from_position]

    if maze[from_position] < 3:
        maze[from_position] += 1
    else:
        maze[from_position] -= 1

    return position
