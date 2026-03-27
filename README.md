# 🧠 Critical Mass AI Engine

**Hybrid Game AI for Chain Reaction / Critical Mass**

An advanced AI agent designed for competitive gameplay in **Chain Reaction–style Critical Mass environments**, combining deterministic search, probabilistic simulation, and domain-specific heuristics.

---

# 🚀 Overview

This project implements a **high-performance decision-making engine** capable of:

* Strategic planning via **Minimax with Alpha-Beta pruning**
* Handling uncertainty using **Monte Carlo rollouts**
* Maintaining board dominance with **heuristic evaluation**
* Operating under **strict time constraints (competition-ready)**

> Designed for **AI competitions, game simulators, and research experimentation**

---

# 🧠 Core AI Architecture

The bot uses a **hybrid intelligence pipeline**:

### 🔍 1. Deterministic Search

* Minimax with Alpha-Beta pruning
* Depth-limited for performance
* Prioritized move ordering

### 🎲 2. Probabilistic Simulation

* Monte Carlo rollouts for stochastic evaluation
* Captures long-term chain reaction potential

### ⚖️ 3. Heuristic Evaluation

Custom scoring based on:

* Cell stability (critical mass proximity)
* Chain reaction potential
* Board control and dominance
* Risk minimization (explosion vulnerability)

---

# ⚡ Why This Project Stands Out

✔ Hybrid AI (Search + Simulation)
✔ Competition-ready architecture
✔ Modular & extensible design
✔ Zero external dependencies
✔ Fully testable game engine

---

# 📁 Project Structure

```bash
critical-mass-engine/
│
├── teamname_bot.py          # Competition entry point
├── strategy.md              # Strategy explanation
├── README.md
├── requirements.txt
│
├── test_cases/
│   └── sample_board.txt
│
├── tests/
│   ├── test_board.py
│   └── test_bot.py
│
└── critical_mass_engine/
    ├── __init__.py
    ├── constants.py         # Tunable AI parameters
    ├── board.py             # Game state + rules
    ├── heuristics.py        # Evaluation logic
    ├── search.py            # Minimax + Alpha-Beta
    ├── simulation.py        # Monte Carlo rollouts
    ├── io_utils.py
    └── bot.py               # Core decision engine
```

---

# ⚙️ Quick Start

### 1️⃣ Clone Repository

```bash
git clone https://github.com/SaloniSingh20/critical-mass-engine.git
cd critical-mass-engine
```

---

### 2️⃣ Run the Bot

```bash
python teamname_bot.py
```

➡ Output: Best move for Player 1 as `(row, col)`

---

### 3️⃣ Run Tests

```bash
python -m unittest discover -s tests -v
```

---

# 🧩 Integration API

### Entry Function:

```python
choose_move(board, player)
```

* 📍 Located in: `teamname_bot.py`
* 🧠 Internally uses: `critical_mass_engine/bot.py`

---

# 🧱 Board Specification

* Grid Size: **12 x 8**
* Cell Format: `[orb_count, owner]`

| Owner | Meaning  |
| ----- | -------- |
| 0     | Empty    |
| 1     | Player 1 |
| 2     | Player 2 |

### Example:

```python
[[0,0],[1,1],[0,0],[2,2],[0,0],[0,0],[0,0],[0,0]]
```

---

# 🔄 Decision Pipeline

1. Generate all valid moves
2. Rank using heuristic scoring
3. Select top candidates
4. Run Monte Carlo simulations
5. Apply Minimax + Alpha-Beta
6. Return highest scoring move

> Includes controlled randomness for exploration

---

# 🎛️ Tunable Parameters

All AI knobs are centralized in:

```bash
critical_mass_engine/constants.py
```

Key parameters:

* `TIME_LIMIT`
* `SEARCH_DEPTH`
* `ROLLOUTS_PER_MOVE`
* `ROLLOUT_DEPTH`
* `TOP_CANDIDATES`
* `MAX_ORDERED_MOVES`
* `RANDOM_MOVE_PROBABILITY`

---

# 🧪 Test Coverage

✔ Move legality
✔ Board immutability
✔ Chain reaction propagation
✔ Explosion correctness
✔ Capture mechanics
✔ Bot output validity

---

# ⚡ Performance Characteristics

* Optimized for **low-latency decisions**
* Efficient pruning reduces search complexity
* Scales well under **tight competition constraints**

---

# 🧠 Advanced Features (Competition Edge)

* Heuristic-guided move ordering
* Hybrid evaluation (search + simulation)
* Controlled stochastic exploration
* Modular AI pipeline for rapid experimentation

---

# 🛣️ Roadmap (Next-Level Enhancements)

* 🔥 Iterative deepening with time allocation
* 📊 Benchmarking (win-rate + move latency)
* 📚 Opening-book strategies
* 🧠 Reinforcement learning integration
* ⚡ Parallel Monte Carlo rollouts

---

# 🏆 Use Cases

* AI competitions (game agents)
* Algorithm benchmarking
* Game theory experimentation
* Educational AI projects

---
