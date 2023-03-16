def threshold(values, goal):
    compare = 0
    for a in range(len(values)):
        compare += values[a]
        if compare > goal:
            return 1+a
    return 0