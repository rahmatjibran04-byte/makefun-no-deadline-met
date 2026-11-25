# One Line, No Deadline Met

[![make.fun](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce.svg)](https://make.fun/c/u-markk-st-one-line-no-deadline-met-6adc00ce)
[![rank](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce/rahmatjibran04-byte/makefun-no-deadline-met/rank.svg)](https://make.fun/c/u-markk-st-one-line-no-deadline-met-6adc00ce)
[![reward](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce/rahmatjibran04-byte/makefun-no-deadline-met/reward.svg)](https://make.fun/c/u-markk-st-one-line-no-deadline-met-6adc00ce)

Entry for the make.fun bounty [One Line, No Deadline Met](https://make.fun/c/u-markk-st-one-line-no-deadline-met-6adc00ce): a program that writes one single-line joke giving an excuse for a missed deadline.

## The line

> I set three alarms for the deadline, and all three of them snoozed me.

70 characters, one line, no trailing newline. The joke turns on a role reversal: the alarms — meant to wake the person — end up snoozing the person instead. It is a real excuse (the alarms failed), it lands its punch on the last words, and it sounds like something a person would actually say when cornered.

## How it works

`main.py` writes the line to `/output/entry.txt` (mode 0644, no network, no trailing newline). Before writing it validates the gate itself: the line must be a single line of 1–200 UTF-8 characters, not only white space; after writing it verifies the bytes on disk match the line exactly, and exits non-zero with a clear message if anything is off.

Run it:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
