# AI Pathfinding Agent — FAST NUCES

An interactive Python application that visualizes **Informed Search algorithms** on a 2D grid. Built with **Pygame**, this project compares the efficiency and optimality of A\* Search and Greedy Best-First Search (GBFS).

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Controls](#controls)
- [Technical Analysis](#technical-analysis)
- [Algorithm Comparison](#algorithm-comparison)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Interactive Map Editor** — Manually place start/goal nodes and draw obstacle walls.
- **Random Map Generation** — Instantly generate mazes with 30% wall coverage.
- **Informed Search Algorithms:**
  - **A\* Search** — Guaranteed shortest path using `f(n) = g(n) + h(n)`.
  - **Greedy Best-First Search (GBFS)** — Fast, goal-oriented approach using `f(n) = h(n)`.
- **Dynamic Obstacle Mode** — Real-time obstacle spawning with automatic path re-planning.
- **Performance Metrics** — Console output for Nodes Visited, Path Cost, and Execution Time.

---

## Installation

**1. Clone the repository:**
```bash
git clone https://github.com/Saleha-Asghar/Dynamic-Pathfinding-Agent.git
cd ai-pathfinding-agent
```

**2. Install the required dependency:**
```bash
pip install pygame
```

**3. Run the application:**
```bash
python pathfinder.py
```

---

## Controls

| Key / Action | Function |
|---|---|
| `Left Click` | Place Start (Orange) → Goal (Turquoise) → Walls (Black) |
| `Right Click` | Erase / Reset a cell |
| `R` | Generate a random map (30% wall density) |
| `C` | Clear the entire grid |
| `D` | Toggle Dynamic Obstacle Mode |
| `Space` | Run A\* Search |
| `G` | Run Greedy Best-First Search |

---

## Technical Analysis

Both algorithms operate on a 2D grid and use the **Manhattan Distance** as their heuristic:

```
h(n) = |x₁ - x₂| + |y₁ - y₂|
```

This heuristic is **admissible** (never overestimates the true cost) and **consistent**, which guarantees that A\* always finds the optimal path.

### A\* Search

A\* evaluates nodes using:

```
f(n) = g(n) + h(n)
```

where `g(n)` is the exact cost from the start node and `h(n)` is the estimated cost to the goal. By balancing both values, A\* explores the grid thoroughly and guarantees the **shortest possible path**.

### Greedy Best-First Search (GBFS)

GBFS ignores `g(n)` and only uses:

```
f(n) = h(n)
```

This makes it faster in practice — it "sprints" directly toward the goal — but it offers **no optimality guarantee** and can find longer, suboptimal paths.

---

## Algorithm Comparison

| Metric | A\* Search | Greedy Best-First Search |
|---|---|---|
| **Optimality** | ✅ Guaranteed shortest path | ❌ Not guaranteed; often suboptimal |
| **Nodes Visited** | Higher — explores more to ensure quality | Lower — rushes toward the goal |
| **Execution Time** | Slightly slower | Faster due to simpler evaluation |
| **Formula** | `f(n) = g(n) + h(n)` | `f(n) = h(n)` |
| **Behavior** | Balanced and thorough exploration | Aggressive, goal-oriented movement |

---

## Project Structure

```
ai-pathfinding-agent/
├── pathfinder.py       # Main application entry point
├── README.md           # Project documentation
└── assets/             # (Optional) Screenshots or demo GIFs
```

---

## Requirements

- Python 3.8+
- pygame

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is open-source. Add a license file (e.g., MIT) before publishing publicly.

---

*Developed as part of the Artificial Intelligence course at FAST NUCES.*
