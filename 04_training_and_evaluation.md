# Module 4 — Training and Evaluation

## 4.1 Loss functions

**Margin-based ranking (pairwise) loss** — used by early translational models.
Pushes positive scores above negatives by a margin `γ`:

```
L = Σ  max(0, γ + f(h',r,t') − f(h,r,t))

(h,r,t)   = positive triple
(h',r,t') = corrupted negative
γ         = margin hyperparameter (> 0)
```

**Logistic / binary cross-entropy loss** — treats each triple as a binary label;
common for tensor models like ComplEx.

**Self-adversarial negative sampling** — weights harder negatives more
(introduced with RotatE), improving the training signal.

> **In code:** both losses live in
> [`kgc/training/losses.py`](../kgc/training/losses.py).

## 4.2 Negative sampling strategies

- **Uniform** — replace head or tail with a uniformly random entity.
- **Bernoulli** — choose head vs tail corruption based on relation cardinality
  (1-to-N vs N-to-1) to reduce false negatives.
- **Self-adversarial** — sample negatives proportional to current model scores.

## 4.3 Evaluation protocol

For each test triple `(h, r, t)`, corrupt the tail to form all candidates
`(h, r, e)` for every `e ∈ E`, score them, and find the rank of the true `t`.
Repeat for the head. The crucial refinement is **filtered** ranking: remove
other *known true* triples from the candidate list before ranking, so the model
is not penalized for ranking another correct answer highly.

```
rank(t) = 1 + #{ e ≠ known-true : f(h, r, e) > f(h, r, t) }
```

> **In code:** `_filtered_rank` in
> [`kgc/evaluation/evaluator.py`](../kgc/evaluation/evaluator.py) masks the
> other known-true entities with `−inf` before counting how many score higher.

## 4.4 Metrics

| Metric                     | Definition                                   | Better |
|----------------------------|----------------------------------------------|--------|
| MR (Mean Rank)             | Average rank of the correct entity.          | lower  |
| MRR (Mean Reciprocal Rank) | Average of `1/rank`; robust to outliers.     | higher |
| Hits@1                     | Fraction where correct answer is rank 1.     | higher |
| Hits@3                     | Fraction where correct answer is in top 3.   | higher |
| Hits@10                    | Fraction where correct answer is in top 10.  | higher |

**Worked example.** If the correct tail is ranked 4th, its reciprocal rank is
`1/4 = 0.25`; it does not count toward Hits@1 or Hits@3, but it does count
toward Hits@10. MRR averages such reciprocal ranks over all test queries.

## 4.5 Benchmark datasets

| Dataset    | Source              | Note                                        |
|------------|---------------------|---------------------------------------------|
| FB15k      | Freebase subset     | Classic; suffers from inverse-relation leakage. |
| FB15k-237  | Freebase, cleaned   | Inverse relations removed; standard.        |
| WN18       | WordNet             | Lexical relations; also has leakage.        |
| WN18RR     | WordNet, cleaned    | Leakage removed; standard.                  |
| YAGO3-10   | YAGO                | Larger, high in-degree entities.            |

### Why FB15k-237 and WN18RR matter

The original FB15k and WN18 contain many *inverse* relations (if `(a, r, b)`
holds then `(b, r⁻¹, a)` holds). A model can score test triples simply by
memorizing inverses, inflating results. The `-237` / `RR` versions remove these,
giving a fairer measure of genuine inference.

## Takeaways

- Always use filtered ranking; report MRR and Hits@{1,3,10}.
- Prefer FB15k-237 / WN18RR over the leaky originals.

---

Prev: [Module 3](03_representing_graphs.md) · Next: [Module 5 — Translational Models](05_translational_models.md)
