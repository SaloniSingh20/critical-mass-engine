# Critical Mass Engine

An AI bot for Chain Reaction style Critical Mass gameplay, built as a clean Python project and ready for competition integration.

The bot uses a hybrid strategy:
- Minimax with alpha-beta pruning for tactical calculation
- Monte Carlo rollouts for uncertainty handling
- Heuristic evaluation for board control and survival

## Why This Project

This repository is structured to be easy to:
- Plug into a game runner quickly
- Tune and experiment with strategy constants
- Test core board mechanics reliably
- Extend with stronger search and benchmarking

## Project Structure

```text
critical-mass engine/
|-- teamname_bot.py
|-- strategy.md
|-- README.md
|-- requirements.txt
|-- test_cases/
|   `-- sample_board.txt
|-- tests/
|   |-- test_board.py
|   `-- test_bot.py
`-- critical_mass_engine/
    |-- __init__.py
    |-- constants.py
    |-- board.py
    |-- heuristics.py
    |-- search.py
    |-- simulation.py
    |-- io_utils.py
    `-- bot.py
```

## Quick Start

### 1) Clone repository

```bash
git clone https://github.com/SaloniSingh20/critical-mass-engine.git
cd critical-mass-engine
```

### 2) Run the bot on sample board

```bash
python teamname_bot.py
```

Expected output is a suggested move for player 1 as a coordinate tuple.

### 3) Run tests

```bash
python -m unittest discover -s tests -v
```

## Integration API

Competition-facing entry point:
- Function: choose_move(board, player)
- File: teamname_bot.py

Internal implementation lives in critical_mass_engine/bot.py.

## Board Specification

- Board size: 12 rows x 8 columns
- Cell format: [count, owner]
- owner values:
  - 0 = empty
  - 1 = player 1
  - 2 = player 2

Example row:

```text
[[0,0],[1,1],[0,0],[2,2],[0,0],[0,0],[0,0],[0,0]]
```

## Strategy Pipeline

1. Generate valid moves for current player.
2. Rank moves with positional and critical-mass heuristics.
3. Evaluate top candidates via Monte Carlo rollouts.
4. Search shortlisted moves with minimax + alpha-beta.
5. Return highest scoring move (with small exploration probability).

## Tunable Parameters

All major behavior knobs are centralized in critical_mass_engine/constants.py:
- TIME_LIMIT
- MAX_ORDERED_MOVES
- TOP_CANDIDATES
- ROLLOUT_DEPTH
- ROLLOUTS_PER_MOVE
- SEARCH_DEPTH
- RANDOM_MOVE_PROBABILITY

## Test Coverage

Current tests validate:
- Move legality filtering
- Input board immutability on move application
- Corner explosion correctness
- Chain reaction propagation and capture behavior
- Bot interface returns valid coordinates

## Dependencies

Runtime uses Python standard library only.

requirements.txt is included for compatibility with tooling pipelines.

## Roadmap

- Add benchmark harness for move-time and win-rate tracking
- Add opening-book style priors for early-game stability
- Add optional iterative deepening with dynamic time allocation
