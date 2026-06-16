# Module 3 — Representing a Graph for Machine Learning

## 3.1 From symbols to vectors

Entities and relations are discrete symbols. Machine-learning models need
continuous representations. The dominant idea is the **knowledge graph
embedding (KGE)**: map every entity and relation to a low-dimensional vector (an
*embedding*) so that geometric relationships in the vector space reflect
semantic relationships in the graph.

```
Entity e   →  vector  e ∈ ℝ^d
Relation r →  vector  r ∈ ℝ^d   (or a matrix, complex vector, etc.)
```

> **In code:** embedding tables are created in each model's `__init__`, e.g.
> [`kgc/models/transe.py`](../kgc/models/transe.py).

## 3.2 The scoring-function framework

Almost every embedding model is defined by a **scoring function** `f(h, r, t)`
that maps a triple to a real number measuring plausibility. Higher score (or
lower distance) = more likely true.

1. Look up embeddings for `h`, `r`, `t`.
2. Combine them with `f` to produce a score.
3. Train so true triples score higher than corrupted ones.
4. At test time, rank candidates by score.

> **In code:** every model implements `score_hrt(h, r, t)`; the base class in
> [`kgc/models/base.py`](../kgc/models/base.py) handles the shared plumbing.

## 3.3 Two big families

| Family                       | Core idea                                                          | Examples                  |
|------------------------------|--------------------------------------------------------------------|---------------------------|
| Distance / translational     | Relation = a translation/transformation; score = negative distance.| TransE, TransH/R, RotatE  |
| Semantic matching / tensor   | Score = a multiplicative similarity (bilinear product).            | RESCAL, DistMult, ComplEx |

These two families are the subjects of Modules 5 and 6.

## 3.4 The KG as a tensor

A KG over `|E|` entities and `|R|` relations can be viewed as a 3-D binary
**adjacency tensor** `X` of shape `|E| × |R| × |E|`, where `X[h,r,t] = 1` if the
triple is observed. KGC = predicting the missing 1s in this sparse tensor —
which is why many models are framed as **tensor factorization**.

```
        relations
        ┌───────────────┐
 heads  │  X[h, r, t]   │  tails
        └───────────────┘
   1 = observed fact, 0 = unknown (NOT necessarily false)
```

## Takeaways

- KGEs turn symbols into vectors so geometry encodes meaning.
- A model = (embeddings) + (scoring function) + (training objective).

---

Prev: [Module 2](02_the_kgc_problem.md) · Next: [Module 4 — Training and Evaluation](04_training_and_evaluation.md)
