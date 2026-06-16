# Module 2 — The Knowledge Graph Completion Problem

## 2.1 The core problem: incompleteness

Real KGs are massively **incomplete**. Studies of Freebase found that a large
majority of person entities were missing facts such as place of birth or
nationality. Crucially, the *absence* of a triple does not mean it is false — it
may simply be unknown.

**Knowledge Graph Completion (KGC)**, also called **link prediction**, is the
task of inferring missing true triples from the triples we already observe.

## 2.2 Task formulations

**Triple classification** — given a candidate `(h, r, t)`, decide if it is true.

**Entity (link) prediction** — the dominant formulation. Given two of the three
slots, predict the missing one:

```
Tail prediction:  (h, r, ?)   e.g. (Einstein, bornIn, ?)
Head prediction:  (?, r, t)   e.g. (?, capitalOf, France)
Relation pred.:   (h, ?, t)   e.g. (Paris, ?, France)
```

In practice we **score every candidate entity** and produce a ranked list. A
good model ranks the correct answer near the top.

> **In code:** ranking every candidate is implemented by
> `score_all_tails` / `score_all_heads` in
> [`kgc/models/base.py`](../kgc/models/base.py), and the ranking itself in
> [`kgc/evaluation/evaluator.py`](../kgc/evaluation/evaluator.py).

## 2.3 Open-world vs closed-world assumption

| Assumption          | Meaning                                              | Implication for KGC                          |
|---------------------|------------------------------------------------------|----------------------------------------------|
| Closed-world (CWA)  | Anything not in the KG is false.                     | Too strict: penalizes true-but-missing facts.|
| Open-world (OWA)    | Missing facts are simply unknown.                    | Realistic, but complicates negatives.        |
| Local CWA           | Missing facts treated as false only for training negatives. | Practical compromise used by most models. |

## 2.4 The negative example problem

KGs store only **positive** facts. To train discriminative models we must
generate **negative** triples. The standard method is **corruption**: take a
true triple and replace its head or tail with a random entity.

```
True:      (Einstein, bornIn, Ulm)
Corrupt h: (Newton,   bornIn, Ulm)   ← likely false
Corrupt t: (Einstein, bornIn, Mars)  ← likely false
```

**Risk:** a "corrupted" triple might accidentally be true (a *false negative*).
Filtered evaluation (Module 4) and Bernoulli corruption reduce this.

> **In code:** `TripleBatcher._corrupt` in
> [`kgc/data/dataset.py`](../kgc/data/dataset.py) implements uniform
> head/tail corruption.

## Takeaways

- KGC infers missing true triples; the canonical form is link prediction via
  ranking.
- KGs follow the open-world assumption, so generating negatives requires care.

---

Prev: [Module 1](01_what_is_a_kg.md) · Next: [Module 3 — Representing a Graph for ML](03_representing_graphs.md)
