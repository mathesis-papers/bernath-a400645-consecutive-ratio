# Bounded-error asymptotics for rounded square-root recurrences

This note proves the consecutive-ratio assertion in OEIS A400645,
revision 21, COMMENTS, with the stronger conclusion
`a_n = c lambda^n + O(1)`, `c > 0`. The same conclusion holds for
nondecreasing nonnegative four-term initial data whose last term is at least 292.
It also proves the positive-norm ratio assertions in A063827 and A400644,
their stated nondecreasing initial-data extensions, and the strictly
increasing conjecture in A289916, revision 11, COMMENTS. The coverage table
identifies the known algebraic identities, their contributors, and the
written proofs of all additional consequences.

## Contents and build

- `note.tex`: complete mathematical statements, proofs and references.
- `metadata.json`: title, creators, affiliations, license and problem IDs.
- `verify.py`: Python standard-library exact finite checks.
- `checks.json`: expected deterministic output.
- `source-manifest.json`: SHA-256 and byte length of each source member.

Build with Tectonic 0.17.0:

```sh
tectonic note.tex
```

Or use `pdflatex note.tex` twice. The bibliography is contained in the TeX;
there is no external bibliography or figure dependency.

Run the finite checks with Python 3.10 or newer:

```sh
python3 verify.py > actual-checks.json
diff -u checks.json actual-checks.json
```

The output has status `ALL_CHECKS_OK`: 512 terms for each rounded sequence,
all displayed terms of A400645, A063827, A400644 and A289916, positive
entire-tail bounds, rational coefficient inequalities and exact companion
identities. These finite checks accompany, rather than replace, the infinite
proofs in the note.

## Mathematical coverage

The declaration `D5.S1.Recurrence.OEISA400645.result` in
<https://github.com/the-omega-institute/trureturing/blob/6974dba01daa1a25cc74b87a86c191e95fe2c681/D5/S1/Recurrence/OEISA400645.lean>
states existence, the consecutive-ratio limit, and the largest-real-octic-root
characterization for the exact initial data. Its private `square_asymptotic`
lemma states the positive normalized-square limit.

The declaration `D5.S1.Recurrence.OEISA400644.result` in
<https://github.com/the-omega-institute/trureturing/blob/6974dba01daa1a25cc74b87a86c191e95fe2c681/D5/S1/Recurrence/OEISA400644.lean>
states existence, uniqueness, positivity, the ratio limit and the
largest-positive-sextic-root characterization for its specified initial data.
The bounded-error refinements, two-term recurrence, initial-data extension,
fixed-lag limits and algebraic companion statements have written proofs here.

Creators: Haobo Ma (ChronoAI Pte Ltd, Singapore), then Wenlin Zhang
(National University of Singapore; ChronoAI Pte Ltd, Singapore).
License: Creative Commons Attribution 4.0 International (`cc-by-4.0`).
The cited OEIS entries and linked Lean files retain their applicable terms.
