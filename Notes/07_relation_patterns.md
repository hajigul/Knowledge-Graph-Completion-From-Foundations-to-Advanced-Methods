# Module 7 — Relation Patterns and Expressiveness

A model is only as good as the logical patterns it can represent. This module
formalizes the patterns and which models capture them.

## 7.1 The key patterns

| Pattern        | Definition                          | Example                                  |
|----------------|-------------------------------------|------------------------------------------|
| Symmetry       | `r(x,y) ⇒ r(y,x)`                   | marriedTo, sibling                       |
| Antisymmetry   | `r(x,y) ⇒ ¬r(y,x)`                  | parentOf, partOf                         |
| Inversion      | `r₁(x,y) ⇔ r₂(y,x)`                 | hypernym / hyponym                       |
| Composition    | `r₁(x,y) ∧ r₂(y,z) ⇒ r₃(x,z)`       | motherOf ∘ motherOf ⇒ grandmotherOf      |

## 7.2 Which models capture what

| Model    | Symmetry | Antisymmetry | Inversion | Composition |
|----------|----------|--------------|-----------|-------------|
| TransE   | ✗        | ✓            | ✓         | ✓           |
| DistMult | ✓        | ✗            | ✗         | ✗           |
| ComplEx  | ✓        | ✓            | ✓         | ✗           |
| RotatE   | ✓        | ✓            | ✓         | ✓           |

### Why this table matters

When choosing a model for a domain, identify which relation patterns dominate:

- A taxonomy with many **inverse** pairs favors ComplEx or RotatE.
- A KG rich in **compositional** chains favors RotatE or rule-augmented methods
  (Module 10).
- If most relations are **symmetric** (e.g. co-authorship), even DistMult can be
  competitive.

### Sketch: why DistMult can't do antisymmetry

DistMult scores `⟨h, r, t⟩ = Σ_i h_i r_i t_i`, which is invariant under swapping
`h` and `t`. So `f(h, r, t) = f(t, r, h)` always. An antisymmetric relation
requires these to differ — impossible for DistMult. ComplEx repairs this by
conjugating the tail, and RotatE by using non-trivial rotations.

## 7.3 The toy dataset as a test bed

The synthetic KG produced by
[`scripts/make_toy_dataset.py`](../scripts/make_toy_dataset.py) deliberately
includes:

- a **symmetric** relation (`sibling`),
- an **inverse** pair (`parentOf` / `childOf`),
- a **composition** chain (`bornIn` ∘ `locatedIn` ⇒ `nationalityOf`).

Run [`examples/compare_models.py`](../examples/compare_models.py) and watch how
RotatE tends to handle the composition chain better than DistMult — exactly what
the table predicts.

## Takeaways

- Expressiveness = which logical patterns the scoring function can satisfy.
- RotatE captures all four core patterns; pick models by domain structure.

---

Prev: [Module 6](06_tensor_factorization_models.md) · Next: [Module 8 — Practical Pipeline](08_practical_pipeline.md)
