# Critical Mass Bot Strategy

## Overview
This bot uses a hybrid approach that combines deterministic search with stochastic simulation.

## Core Techniques
- Minimax with alpha-beta pruning for tactical foresight
- Monte Carlo rollouts for position quality estimation
- Heuristic evaluation for board control and risk handling

## Heuristic Priorities
- Prefer corners and edges for stability
- Reward cells near critical mass to enable chain reactions
- Penalize vulnerable opponent-near-critical threats
- Favor positions that reduce opponent move freedom

## Move Pipeline
1. Generate valid moves and apply heuristic ordering
2. Run quick Monte Carlo rollouts on top candidates
3. Run minimax on the strongest shortlist
4. Apply small randomization to avoid deterministic traps

## Time Constraint
The search is capped to stay within a sub-second practical time budget for each turn.
