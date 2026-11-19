# Bounded-error asymptotics for Bernáth's conjecture: OEIS A400645, revision 21, COMMENTS, and its rounded-norm siblings

**Authors:** Haobo Ma, Wenlin Zhang

For Bernáth's consecutive-ratio conjecture in OEIS A400645, revision 21, COMMENTS, we prove the stronger bounded-error asymptotic a_n=c lambda^n+O(1) with c>0, where lambda is the largest real root of x^8-x^6-x^4-x^2+1, namely 1.3122819079.... The squared terms satisfy a linear recurrence with a controlled rounding error. A finite seed bounds its entire normalized error tail and ensures a positive leading coefficient; a three-coordinate contraction then gives an exponential asymptotic. The same error analysis proves the ratio assertions for A063827 and A400644, and extends them to nondecreasing initial data. We also prove the increasing-sequence conjecture in A289916 and recover its limiting ratio, identified in A289917.

- PDF: [frozen public file](paper.pdf)
- License: CC-BY-4.0
- Version: 2
- Mathesis record: [bernath-a400645-consecutive-ratio](https://mathesis-omega-research.apps.chrono-ai.fun/papers/bernath-a400645-consecutive-ratio?version=2)

## How to cite

Haobo Ma, Wenlin Zhang (2026). Bounded-error asymptotics for Bernáth's conjecture: OEIS A400645, revision 21, COMMENTS, and its rounded-norm siblings. Mathesis, version 2. https://mathesis-omega-research.apps.chrono-ai.fun/papers/bernath-a400645-consecutive-ratio?version=2

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/6974dba01daa1a25cc74b87a86c191e95fe2c681/D5/S1/Recurrence/OEISA400645.lean) | No public receipt |
| Lemma (s2) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/6974dba01daa1a25cc74b87a86c191e95fe2c681/D5/S1/Recurrence/OEISA400645.lean) | No public receipt |
| Corollary (s3) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/6974dba01daa1a25cc74b87a86c191e95fe2c681/D5/S1/Recurrence/OEISA400645.lean) | No public receipt |
| Corollary (s4) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/6974dba01daa1a25cc74b87a86c191e95fe2c681/D5/S1/Recurrence/OEISA400645.lean) | No public receipt |
| Corollary (s5) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/6974dba01daa1a25cc74b87a86c191e95fe2c681/D5/S1/Recurrence/OEISA400645.lean) | No public receipt |
| Corollary (s6) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/6974dba01daa1a25cc74b87a86c191e95fe2c681/D5/S1/Recurrence/OEISA400645.lean) | No public receipt |
| Corollary (s7) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/6974dba01daa1a25cc74b87a86c191e95fe2c681/D5/S1/Recurrence/OEISA400645.lean) | No public receipt |
| Corollary (s8) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/6974dba01daa1a25cc74b87a86c191e95fe2c681/D5/S1/Recurrence/OEISA400645.lean) | No public receipt |
| Corollary (s9) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/6974dba01daa1a25cc74b87a86c191e95fe2c681/D5/S1/Recurrence/OEISA400645.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).
