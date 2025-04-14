# AI-Enhanced Sudoku Solver

## Overview
This project implements an intelligent Sudoku solver using AI techniques including backtracking search, constraint propagation (AC-3 algorithm), and various heuristics for optimization. Developed as part of an Introduction to Artificial Intelligence course, this solver can efficiently handle Sudoku puzzles of varying difficulties.

## Key Features
- **Backtracking Search**: Implements a smart backtracking algorithm to systematically explore possible solutions
- **AC-3 Algorithm**: Uses constraint propagation to reduce the search space before attempting solutions
- **Intelligent Heuristics**:
  - Minimum Remaining Values (MRV) for variable selection
  - Least Constraining Value (LCV) for value ordering
- **Performance Optimization**: Includes timeout handling to manage computational resources
- **Input Validation**: Ensures solutions meet Sudoku puzzle requirements

## How It Works
1. **Input**: Reads a 9x9 Sudoku grid where 0 represents empty cells
2. **Constraint Processing**: Applies AC-3 algorithm to eliminate impossible values
3. **Smart Search**: Uses MRV and LCV heuristics to make intelligent choices during backtracking
4. **Solution Verification**: Validates the final solution against Sudoku rules

## Usage
```python
# Input format: Enter 9 rows of 9 space-separated numbers (use 0 for empty cells)
# Example:
0 0 3 0 2 0 6 0 0
9 0 0 3 0 5 0 0 1
0 0 1 8 0 6 4 0 0
0 0 8 1 0 2 9 0 0
7 0 0 0 0 0 0 0 8
0 0 6 7 0 8 2 0 0
0 0 2 6 0 9 5 0 0
8 0 0 2 0 3 0 0 9
0 0 5 0 1 0 3 0 0
```

## Technical Implementation
- **Language**: Python 3
- **Key Algorithms**:
  - AC-3 (Arc Consistency Algorithm)
  - Backtracking with forward checking
  - MRV (Minimum Remaining Values) heuristic
  - LCV (Least Constraining Value) heuristic

## Performance
- Efficiently solves most Sudoku puzzles within seconds
- Includes a 10-second timeout mechanism for particularly challenging puzzles
- Optimized through constraint propagation to reduce unnecessary backtracking

## Learning Outcomes
This project demonstrates practical implementation of:
- Constraint Satisfaction Problems (CSPs)
- Search algorithms and heuristics
- Problem space optimization
- Algorithm efficiency considerations

## Future Improvements
- GUI interface for puzzle input
- Performance metrics and statistics
- Support for different grid sizes
- Puzzle generator functionality
