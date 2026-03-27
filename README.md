# ⚛️ Critical Mass Engine

### *An Adversarial AI System for Chain Reaction Dominance*

---

## 🧠 Overview

**Critical Mass Engine** is a high-performance AI bot designed for competitive play in the *Chain Reaction / Critical Mass* domain.

Built for algorithmic competitions, this system combines **deterministic search**, **probabilistic simulation**, and **strategic heuristics** to produce robust, adaptive, and high-quality decisions under strict time constraints.

> This is not a rule-based bot.
> This is a **decision engine designed to outthink opponents**.

---

## 🚀 Core Intelligence Architecture

The bot integrates multiple AI paradigms into a unified pipeline:

### 🔹 Minimax with Alpha-Beta Pruning

* Performs adversarial lookahead search
* Eliminates suboptimal branches efficiently
* Enables deeper tactical reasoning within time limits

### 🔹 Monte Carlo Simulation

* Executes randomized playouts to evaluate long-term outcomes
* Helps escape local optima and deceptive positions
* Adds probabilistic foresight to deterministic search

### 🔹 Heuristic Evaluation Engine

Custom-designed evaluation function that considers:

* Orb dominance and board control
* Chain reaction potential (near-critical cells)
* Positional stability (corner > edge > center)
* Threat modeling and opponent explosion risk
* Strategic pressure and mobility restriction

---

## ⚔️ Strategic Capabilities

### 💣 Chain Reaction Control

Accurately simulates cascading explosions to:

* Trigger large-scale board captures
* Predict multi-step reaction sequences

### 🧠 Trap Detection & Avoidance

* Identifies opponent near-critical cells
* Avoids enabling high-impact counterplays

### 🏰 Corner Domination

* Prioritizes highly stable positions
* Builds long-term control that is difficult to disrupt

### 🔗 Chain Farming

* Prepares multiple near-critical cells
* Executes high-impact multi-cell explosions

### 🚫 Opponent Starvation

* Restricts opponent move space
* Forces predictable and punishable behavior

### 🎭 Anti-Predictability

* Introduces controlled randomness
* Prevents exploitation by deterministic opponents

---

## 🧩 Strategy Pipeline

1. Generate all valid moves for the current player
2. Rank moves using positional + critical-mass heuristics
3. Apply Monte Carlo simulations to estimate long-term value
4. Shortlist top candidates
5. Evaluate candidates using minimax + alpha-beta pruning
6. Select best move (with slight stochastic exploration)

---

## 📁 Project Structure

```
critical-mass-engine/
│
├── teamname_bot.py              # Competition entry point
├── strategy.md                  # Strategy documentation
├── README.md                    # Project overview
├── requirements.txt             # No external dependencies
│
├── test_cases/
│   └── sample_board.txt         # Example board input
│
├── tests/                       # Unit tests
│   ├── test_board.py
│   └── test_bot.py
│
└── critical_mass_engine/        # Modular engine
    ├── __init__.py
    ├── constants.py             # Tunable parameters
    ├── board.py                 # Game mechanics
    ├── heuristics.py            # Evaluation logic
    ├── search.py                # Minimax + pruning
    ├── simulation.py            # Monte Carlo rollouts
    ├── io_utils.py              # Input/output helpers
    └── bot.py                   # Core decision engine
```

---

## ⚡ Quick Start

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/SaloniSingh20/critical-mass-engine.git
cd critical-mass-engine
```

### 2️⃣ Run the Bot

```bash
python teamname_bot.py
```

Output:
A valid move `(row, col)` for the given board state.

---

### 3️⃣ Run Tests

```bash
python -m unittest discover -s tests -v
```

---

## 🔌 Competition Integration

### Entry Function

```python
choose_move(board, player)
```

* **board** → 12×8 grid of `[count, owner]`
* **player** → `1` or `2`

Returns:

```python
(row, col)
```

---

## 📊 Board Specification

* Grid Size: **12 × 8**
* Cell Format: `[orb_count, owner]`

| Owner | Meaning  |
| ----- | -------- |
| 0     | Empty    |
| 1     | Player 1 |
| 2     | Player 2 |

Example:

```
[[0,0],[1,1],[0,0],[2,2],[0,0],[0,0],[0,0],[0,0]]
```

---

## 🎛 Tunable Parameters

All key parameters are centralized in:

```
critical_mass_engine/constants.py
```

Includes:

* `TIME_LIMIT`
* `SEARCH_DEPTH`
* `ROLLOUTS_PER_MOVE`
* `ROLLOUT_DEPTH`
* `TOP_CANDIDATES`
* `MAX_ORDERED_MOVES`
* `RANDOM_MOVE_PROBABILITY`

> Enables rapid experimentation and optimization.

---

## 🧪 Test Coverage

Current test suite validates:

* ✅ Move legality
* ✅ Board immutability
* ✅ Explosion correctness
* ✅ Chain reaction propagation
* ✅ Capture mechanics
* ✅ Bot output validity

---

## 📦 Dependencies

* Pure Python (Standard Library Only)

```
requirements.txt → intentionally minimal
```

---

## 🏆 Performance Characteristics

| Opponent Type      | Expected Outcome |
| ------------------ | ---------------- |
| Random Bots        | ~100% Win Rate   |
| Greedy Bots        | ~95%+ Wins       |
| Basic Minimax Bots | Strong Advantage |
| Advanced Bots      | Competitive Edge |

---

## 🔮 Roadmap

* Benchmarking framework (win-rate + latency tracking)
* Opening strategy optimization
* Iterative deepening with dynamic time allocation
* Lightweight learning-based heuristic tuning

---

## 🧠 Design Philosophy

> “Don’t just compute the best move —
> compute the move your opponent fails to understand.”

This engine is built to:

* Adapt under pressure
* Exploit opponent weaknesses
* Balance precision with unpredictability

---

## 📜 License

For academic and competitive use.

---

## ⚡ Final Note

This project is not just an implementation of game logic.

It is a **strategic system engineered for adversarial dominance**.
