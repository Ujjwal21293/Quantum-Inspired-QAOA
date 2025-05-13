# Quantum-Inspired Traffic Routing Optimization

This project demonstrates a simulation of the **Quantum Approximate Optimization Algorithm (QAOA)** to solve **urban traffic routing problems**, comparing it with classical algorithms such as Dijkstra.

##  Problem
Urban traffic congestion leads to economic losses, CO₂ emissions, and commuter delays. We aim to solve dynamic routing using QAOA principles, simulated classically.

##  Algorithm
- **Quantum-Inspired QAOA** simulated classically.
- **Cost Function**: penalizes congestion and distance.
- **Mixer**: introduces exploration to escape local minima.

##  Features
- Graph-based city map with dynamic edge weights.
- QAOA simulation with tunable parameters.
- Classical heuristics comparison (Dijkstra).
- Performance evaluation and visualization.

##  Structure
- `src/`: Core modules.
- `notebooks/`: Interactive demo.
- `data/`: Sample graphs.
- `results/`: Plots and results.
- `tests/`: Unit tests.