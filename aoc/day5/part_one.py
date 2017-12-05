def steps_to_leave(maze):
    steps = 0
    from_position = 0
    while 0 <= from_position < len(maze):
        maze, from_position = jump(maze, from_position)
        steps += 1

    return steps


def jump(maze, from_position):
    return (
        [x + 1 if i == from_position else x for i, x in enumerate(maze)],
        from_position + maze[from_position]
    )
