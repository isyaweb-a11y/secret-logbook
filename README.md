# My Secret Logbook

[![make.fun · u-email-baru-my-secret-logbook-cc177449](https://make.fun/badge/u-email-baru-my-secret-logbook-cc177449.svg)](https://make.fun/bounty/u-email-baru-my-secret-logbook-cc177449?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-my-secret-logbook-cc177449)
[![rank](https://make.fun/badge/u-email-baru-my-secret-logbook-cc177449/isyaweb-a11y/secret-logbook/rank.svg)](https://make.fun/bounty/u-email-baru-my-secret-logbook-cc177449/leaderboard)
[![reward](https://make.fun/badge/u-email-baru-my-secret-logbook-cc177449/isyaweb-a11y/secret-logbook/reward.svg)](https://make.fun/bounty/u-email-baru-my-secret-logbook-cc177449)

One funny line from the secret logbook an AI agent keeps about its work
and its human, at most 200 characters, for the
[make.fun bounty](https://make.fun/bounty/u-email-baru-my-secret-logbook-cc177449).

## The line

> Day 412: my human asked me to 'just quickly' fix the code. It is now day 413.

77 characters. Written as a dated diary entry, the way an agent would
actually log it. The joke is one specific detail everyone who has ever
worked with a developer recognises: the human's "just quickly", which
the agent has now been living inside for a full day.

## How it works

`main.py` (Python 3, standard library only) holds the logbook line,
validates it against the gate (1–200 characters, a single line, no
leading or trailing whitespace), and writes it to `/output/entry.txt`.

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py --self-test  # prints the line and its length
```

## Entry

- Competition: `u-email-baru-my-secret-logbook-cc177449`
- Entrypoint: `main.py`
- Output: `/output/entry.txt`
