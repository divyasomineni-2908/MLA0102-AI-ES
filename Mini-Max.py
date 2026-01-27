def minimax(depth, node, isMax, values):
    if depth == 3:
        return values[node]

    if isMax:
        best = -1000
        for i in range(2):
            val = minimax(depth + 1, node * 2 + i, False, values)
            best = max(best, val)
        return best
    else:
        best = 1000
        for i in range(2):
            val = minimax(depth + 1, node * 2 + i, True, values)
            best = min(best, val)
        return best


values = [2, 3, 5, 9, 0, 1, 7, 5]

print("Optimal value:", minimax(0, 0, True, values))
