# Marvel for Dummies — source

This is the source for the "Marvel for Dummies" MCU rewatch companion app,
published as a Claude Artifact at:

https://claude.ai/code/artifact/6e1b6831-7a82-4e7c-9508-4ec50069fac7

## Files

- `app_shell.html` — the app's HTML/CSS/JS template. Contains a `__DATA_JS__`
  placeholder (replaced with `data.js`'s contents) and a `__FONT_B64__`
  placeholder (replaced with the base64 Source Serif 4 variable font).
- `data.js` — all content: `RAW_ERAS` (connected MCU timeline, grouped by
  era), `OTHER_ERAS` (non-connected adaptations), `FRESH_THEORIES` (current,
  dated fan theories — usually about the next unreleased title) and
  `THEORIES` (evergreen fan theories), `DOOMSDAY_PATH` (curated watch order),
  and `TYPE_TAG`/`TYPE_LABEL` maps.
- `fonts/source-serif-var.b64` — the embedded font, doesn't need to change.
- `build.py` — assembles the three into `marvel_rewatch_app.html`, the file
  that actually gets published.

## To rebuild after editing data.js or app_shell.html

```
cd /Users/lucreciacubero/marvel-rewatch-app
python3 build.py
```

Then publish `marvel_rewatch_app.html` via the Artifact tool with
`url: "https://claude.ai/code/artifact/6e1b6831-7a82-4e7c-9508-4ec50069fac7"`
to update the same live app rather than creating a new one.

## Monthly update task

A scheduled task checks for newly confirmed MCU release dates/titles and
fresh fan theories once a month and updates this app automatically. See the
scheduled task itself for the exact instructions it runs from.

Conventions to follow when updating:

- An item that hasn't released yet (relative to today) should get
  `critic:null, upcoming:true, releaseDate:'Mon D, YYYY'` instead of a
  critic score — the app shows an "UPCOMING" chip instead of fake review
  scores. Once it has actually released, replace those three fields with a
  real `critic:<0-100>` score (best estimate from aggregator sites) and
  drop `upcoming`/`releaseDate`.
- New titles get appended to the correct era in `RAW_ERAS` (or a new era
  object if none fits), AND to `DOOMSDAY_PATH` if they're part of that
  curated path, AND `avengers-doomsday`-style upcoming flagging as above.
- Fan theories about a title that has since released should either be
  removed (if answered/moot) or left as historical color — use judgment.
  New theories go in `FRESH_THEORIES` (shown first, sorted "Newest") with a
  `source` field (e.g. `'r/marvelstudios'` only if actually reddit-sourced,
  otherwise `'Fan theory roundup'`).
- Never fabricate a critic/fan score for something unreleased.
- Keep synopses to one sentence, same voice as the existing entries.
