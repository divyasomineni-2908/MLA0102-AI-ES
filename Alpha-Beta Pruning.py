def alphabeta(depth, node, alpha, beta, isMax, values):
    if depth == 3:
        return values[node]

    if isMax:
        best = -1000
        for i in range(2):
            val = alphabeta(depth + 1, node * 2 + i, alpha, beta, False, values)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 1000
        for i in range(2):
            val = alphabeta(depth + 1, node * 2 + i, alpha, beta, True, values)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best


values = [2, 3, 5, 9, 0, 1, 7, 5]

print("Optimal value:", alphabeta(0, 0, -1000, 1000, True, values))
