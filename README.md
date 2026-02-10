# Slot Machine Project

A terminal-based slot machine game built with Python. Deposit money, place bets, and spin to win!

## Overview

This is a classic slot machine simulation that runs in the command line. Players deposit funds, choose how many lines to bet on, and spin the reels. Matching symbols across a horizontal line results in a payout based on the symbol's value.

## Features

- **Deposit system** — Add funds to your account before playing
- **Flexible betting** — Bet on 1–3 lines with $1–$100 per line
- **3×3 reels** — Symbols (A, B, C) appear on a 3-row, 3-column grid
- **Payouts** — Win multipliers: A = 10×, B = 8×, C = 3×
- **Balance tracking** — Your balance updates after each spin

## Requirements

- Python 3.x (uses only the standard library; no external dependencies)

## How to Run

```bash
python main.py
```

## How to Play

1. **Deposit** — When prompted, enter the amount you want to add to your account (any positive number).
2. **Spin** — Press Enter to spin, or type `q` and Enter to quit.
3. **Bet** — For each spin, choose:
   - **Lines** — How many horizontal lines to bet on (1–3)
   - **Bet per line** — Amount to wager on each line ($1–$100)
4. **Win** — Matching the same symbol across a full row pays out according to that symbol's multiplier.

### Symbol Payouts

| Symbol | Multiplier |
|--------|------------|
| A      | 10×        |
| B      | 8×         |
| C      | 3×         |

### Example

A bet of $5 on 2 lines with a winning row of three A's pays: **$5 × 10 = $50**

## Project Structure

```
slot_Machine_Project/
├── main.py      # Main game logic and entry point
└── README.md    # This file
```

## License

Personal project — feel free to use and modify for learning purposes.
