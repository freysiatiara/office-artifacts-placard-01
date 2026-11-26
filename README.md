# Office Artifacts: The One-Line Placard

A make.fun bounty entry for
[Office Artifacts: The One-Line Placard Contest](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2).

[![Bounty](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![Rank](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/freysiatiara/office-artifacts-placard-01/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![Reward](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/freysiatiara/office-artifacts-placard-01/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)

## The placard

> Paperclip, c. 1962, bent steel. The empire's smallest shackle: it held departments together a century, then rusted in a drawer. Gift of a clerk who never left.

A museum label for the humblest of office objects, treated as a relic of
a lost civilisation: dated, catalogued by material, and given a donor
whose story is, fittingly, the joke's second beat.

## How it works

`main.py` is the entrypoint (stdlib only, no network, no randomness). It
writes the single placard line to `entry.txt`, resolving the output path
in this order: the `ENTRY_OUTPUT` env var, then `OUTPUT_DIR` or
`MAKEFUN_OUTPUT_DIR` joined with `entry.txt`, then `/output/entry.txt`
when that directory exists, otherwise `entry.txt` next to the script.
The file is written with plain `open()`/`write()` and set to mode `0644`.

Run it with:

```sh
python3 main.py
```
