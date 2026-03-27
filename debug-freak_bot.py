import time
import copy
import random

ROWS = 12
COLS = 8
TIME_LIMIT = 0.95

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def get_critical_mass(r, c):
    return sum(1 for dr, dc in DIRS if 0 <= r + dr < ROWS and 0 <= c + dc < COLS)


def valid_moves(board, player):
    return [(r, c) for r in range(ROWS) for c in range(COLS)
            if board[r][c][1] in [0, player]]


def explode(board):
    changed = True
    while changed:
        changed = False
        for r in range(ROWS):
            for c in range(COLS):
                count, owner = board[r][c]
                if owner != 0 and count >= get_critical_mass(r, c):
                    player = owner
                    board[r][c] = [0, 0]
                    for dr, dc in DIRS:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS:
                            board[nr][nc][0] += 1
                            board[nr][nc][1] = player
                    changed = True


def apply_move(board, move, player):
    r, c = move
    new_board = copy.deepcopy(board)
    new_board[r][c][0] += 1
    new_board[r][c][1] = player
    explode(new_board)
    return new_board


def position_weight(r, c):
    if (r in [0, ROWS - 1]) and (c in [0, COLS - 1]):
        return 5
    elif r in [0, ROWS - 1] or c in [0, COLS - 1]:
        return 3
    return 1


def is_dangerous(board, r, c, opponent):
    count, owner = board[r][c]
    return owner == opponent and count == get_critical_mass(r, c) - 1


def evaluate(board, player):
    opponent = 3 - player
    score = 0

    my_cells = 0
    opp_cells = 0

    for r in range(ROWS):
        for c in range(COLS):
            count, owner = board[r][c]
            crit = get_critical_mass(r, c)
            weight = position_weight(r, c)

            if owner == player:
                my_cells += 1
            elif owner == opponent:
                opp_cells += 1

            if owner == player:
                score += count * weight

                if (r in [0, ROWS - 1]) and (c in [0, COLS - 1]):
                    score += 15

                if count == crit - 2:
                    score += 6

                if count == crit - 1:
                    score += 10

                if count < crit - 1:
                    score += 2

            elif owner == opponent:
                score -= count * weight * 0.8

                if count == crit - 1:
                    score -= 12

                if is_dangerous(board, r, c, opponent):
                    score -= 15

    if opp_cells > 0:
        op_moves = len(valid_moves(board, opponent))
        if op_moves <= 3:
            score += 12

    score += (my_cells - opp_cells) * 3

    return score


def order_moves(board, moves, player):
    scored = []
    for move in moves:
        r, c = move
        count = board[r][c][0]
        crit = get_critical_mass(r, c)

        score = position_weight(r, c) * 10

        if count == crit - 1:
            score += 100

        if count == crit - 2:
            score += 50

        scored.append((score, move))

    scored.sort(reverse=True)
    return [m for _, m in scored]


def minimax(board, depth, alpha, beta, maximizing, player, start):
    if time.time() - start > TIME_LIMIT:
        return evaluate(board, player), None

    if depth == 0:
        return evaluate(board, player), None

    opponent = 3 - player
    current = player if maximizing else opponent

    moves = valid_moves(board, current)
    moves = order_moves(board, moves, player)[:6]

    best_move = None

    if maximizing:
        max_eval = float('-inf')
        for move in moves:
            new_board = apply_move(board, move, current)
            eval_score, _ = minimax(new_board, depth - 1, alpha, beta, False, player, start)

            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move

            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break

        return max_eval, best_move

    else:
        min_eval = float('inf')
        for move in moves:
            new_board = apply_move(board, move, current)
            eval_score, _ = minimax(new_board, depth - 1, alpha, beta, True, player, start)

            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move

            beta = min(beta, eval_score)
            if beta <= alpha:
                break

        return min_eval, best_move


def random_playout(board, player):
    sim = copy.deepcopy(board)
    current = player

    for _ in range(12):
        moves = valid_moves(sim, current)
        if not moves:
            break

        move = random.choice(moves)
        sim = apply_move(sim, move, current)
        current = 3 - current

    return evaluate(sim, player)


def monte_carlo_score(board, move, player, sims=4):
    total = 0
    for _ in range(sims):
        new_board = apply_move(board, move, player)
        total += random_playout(new_board, player)
    return total / sims


def choose_move(board, player):
    start = time.time()

    moves = valid_moves(board, player)
    moves = order_moves(board, moves, player)[:6]

    scored = []
    for move in moves:
        score = monte_carlo_score(board, move, player)
        scored.append((score, move))

    scored.sort(reverse=True)
    top_moves = [m for _, m in scored[:3]]

    best_move = None
    best_score = float('-inf')

    for move in top_moves:
        new_board = apply_move(board, move, player)
        score, _ = minimax(new_board, 3, float('-inf'), float('inf'), False, player, start)

        if score > best_score:
            best_score = score
            best_move = move

    if random.random() < 0.08:
        return random.choice(moves)

    return best_move if best_move else random.choice(moves)


# REQUIRED FUNCTION (MANDATORY FOR SUBMISSION)
def get_move(board, player):
    return choose_move(board, player)
