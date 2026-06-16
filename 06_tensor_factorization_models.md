# Module 6 — Tensor-Factorization (Semantic Matching) Models

## 6.1 RESCAL — bilinear beginnings

RESCAL represents each relation as a **full matrix** `M_r` and scores a triple
with a bilinear product:

```
f(h, r, t) = hᵀ Mᵣ t
```

Very expressive but `O(d²)` parameters per relation — prone to overfitting and
costly at scale.

## 6.2 DistMult — diagonal simplicity

DistMult restricts `M_r` to a **diagonal** matrix, i.e. a single vector `r`,
giving a cheap trilinear dot product:

```
f(h, r, t) = Σ_i  h_i · r_i · t_i  =  ⟨h, r, t⟩
```

**Critical limitation:** the score is symmetric in `h` and `t`, so DistMult
forces *every* relation to be symmetric. It cannot tell `(Einstein, bornIn, Ulm)`
apart from `(Ulm, bornIn, Einstein)`.

> **In code:** [`kgc/models/distmult.py`](../kgc/models/distmult.py). The unit
> test `test_distmult_is_symmetric` in
> [`tests/test_kgc.py`](../tests/test_kgc.py) verifies this property directly.

## 6.3 ComplEx — complex embeddings

ComplEx (Trouillon et al., 2016) moves embeddings into **complex space** `ℂ^d`
and scores with the real part of a Hermitian product:

```
f(h, r, t) = Re( ⟨ h, r, conj(t) ⟩ )
           = Re( Σ_i  h_i · r_i · t̄_i )
```

Expanding with `h = a + bi`, `r = c + di`, `t = e + fi` gives a real formula:

```
Re(h r conj(t)) = ⟨a,c,e⟩ + ⟨b,c,f⟩ + ⟨a,d,f⟩ − ⟨b,d,e⟩
```

The complex conjugate **breaks symmetry**: swapping `h` and `t` changes the
score. This lets ComplEx model both **symmetric and antisymmetric** relations —
a major reason it remains a strong baseline today.

> **In code:** [`kgc/models/complex_model.py`](../kgc/models/complex_model.py)
> stores real and imaginary parts as separate tables and implements exactly the
> four-term real formula above. `test_complex_breaks_symmetry` confirms the
> asymmetry.

## 6.4 Other notable models

- **HolE** — circular correlation of `h` and `t`; mathematically related to
  ComplEx.
- **SimplE** — learns two embeddings per entity (as head, as tail) plus relation
  inverses; fully expressive and interpretable.
- **TuckER** — Tucker decomposition of the adjacency tensor with a shared core
  tensor; generalizes many bilinear models.
- **ConvE** — reshapes `h` and `r` into a 2-D "image" and applies a CNN — a
  bridge to neural scoring functions.

## 6.5 Comparison

| Model    | Space            | Params/relation | Symmetric | Antisymmetric |
|----------|------------------|-----------------|-----------|---------------|
| RESCAL   | Real, matrix     | O(d²)           | ✓         | ✓             |
| DistMult | Real, vector     | O(d)            | ✓         | ✗             |
| ComplEx  | Complex, vector  | O(d)            | ✓         | ✓             |
| TransE   | Real, vector     | O(d)            | ✗         | ✓             |
| RotatE   | Complex, vector  | O(d)            | ✓         | ✓             |

## Takeaways

- Bilinear models score triples by multiplicative similarity.
- DistMult is symmetric-only; ComplEx fixes this via complex conjugation.

---

Prev: [Module 5](05_translational_models.md) · Next: [Module 7 — Relation Patterns](07_relation_patterns.md)
