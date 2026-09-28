<!--
This file belongs at .github/copilot-instructions.md in YOUR repository — copy it there and fill
in the placeholders below with conventions your team actually follows. Copilot reads a file at
that path automatically, on every request, in every mode (Chat, Agent Mode, the coding agent,
code review) — nothing here needs to be restated in a prompt once it's saved.

What belongs in THIS file: conventions that are genuinely repository-wide and stable — true for
every file, every task, every day (a logging style, a testing convention, a safety rule). If a
convention only applies to one service, one language, or one directory, it belongs in a
path-specific file instead, at .github/instructions/<name>.instructions.md, with a required
`applyTo` front-matter glob (e.g. `applyTo: "dashboard/**/*.ts"`) scoping it to just those paths —
see references/example.instructions.md for a worked example. A file that matches both a
repository-wide and a path-specific instruction file gets both, together — one doesn't override
the other.

Ordinary Markdown formatting is all this file needs — whitespace between instructions is ignored,
so one instruction per line or grouped with blank lines both work; pick whichever reads most
maintainably for your team. Delete this comment block once the real conventions below are filled
in.
-->

# [Your repository name] — repository-wide Copilot instructions

- [Placeholder — a logging or error-handling convention your repo actually follows, e.g. "Log
  recoverable failures at `warning`, not `error`; reserve `error` for failures that stop the
  service entirely."]
- [Placeholder — a testing convention, e.g. "Tests live alongside the module they test
  (`foo.py` → `test_foo.py` in the same directory), not in a separate top-level `tests/` tree."]
- [Placeholder — a style or safety convention, e.g. "Prefer explicit exception types over a bare
  `except:` when handling untrusted input."]
- [Placeholder — add one instruction per line for anything else genuinely repository-wide: naming
  conventions, required error handling, a documentation format, a review expectation.]
