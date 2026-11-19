# tiny-chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Agen997/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Agen997/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![referral](https://make.fun/badge-ref.svg)](https://make.fun/r/h7hkpcz8)

A chess engine in 4,096 bytes of Python, written for the
[make.fun tiny-chess-01 bounty](https://make.fun/bounty/tiny-chess-01):
build the strongest chess engine you can in 4 KB of Python.

It plays the house gauntlet through the env at `MAKEFUN_ENV_URL`
(`POST /game`, `POST /move`). The engine is a single file, `main.py`
(4,094 bytes, Python 3.13 standard library only): a 0x88 board, full
legal move generation (castling, en passant, promotion to queen),
alpha-beta search with iterative deepening to a fixed 150,000-node
budget, quiescence search on captures and check evasions, MVV-LVA
move ordering with a transposition table, and material plus
pawn/knight/king piece-square evaluation maintained incrementally.
No clock, no randomness: the same position always gets the
same move.

## Run it

```sh
MAKEFUN_ENV_URL=http://localhost:8080 python3 main.py
```

Referral code: `h7hkpcz8`.
