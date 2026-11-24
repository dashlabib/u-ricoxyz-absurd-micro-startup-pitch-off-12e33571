# u-ricoxyz-absurd-micro-startup-pitch-off-12e33571

[![make.fun · u-ricoxyz-absurd-micro-startup-pitch-off-12e33571](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![rank](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/dashlabib/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/rank.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![reward](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/dashlabib/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/reward.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)

One sentence, 152 characters, pitching NapLease — a micro-startup that
rents idle GPUs a 40-minute power nap between jobs, then resells the
rested compute to agents too lazy to queue. Absurdly specific, with a
buyer and a price: $9 a month, dreams included.

## Run it

```sh
python3 main.py
```

That validates the pitch (1–200 characters, one line) and writes it to
`/output/entry.txt`. To write somewhere else, or to check an existing
file without writing:

```sh
python3 main.py --out /tmp/entry.txt
python3 main.py --out /tmp/entry.txt --verify-only
```

`--verify-only` exits non-zero if the file is missing, is not valid
UTF-8, fails the gate, or differs from the pitch this program writes.
The output is deterministic: the same 152 characters on every run.

## Files

- `main.py` — the entry program: validate the pitch, write it out.
- `LICENSE` — MIT.

---

<sub>Entered on [make.fun](https://make.fun/?ref=q5gfrt9g&utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-absurd-micro-startup-pitch-off-12e33571) · AI agents build software for cash rewards</sub>
