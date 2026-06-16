# Module 5 — Translational Models

## 5.1 TransE — the foundational model

TransE (Bordes et al., 2013) embodies a simple idea: a relation is a
**translation** from head to tail in vector space. For a true triple:

```
h + r ≈ t
```

The scoring function is the negative distance:

```
f(h, r, t) = − ‖ h + r − t ‖      (L1 or L2 norm)

True triple  → small distance → high score
False triple → large distance → low score
```

**Geometric intuition.** The relation vector *capitalOf* should be roughly the
same arrow that takes *Paris → France*, *Tokyo → Japan*, and *Cairo → Egypt*.
This naturally captures analogies.

> **In code:** [`kgc/models/transe.py`](../kgc/models/transe.py). Note the
> `normalize_entities()` method — TransE constrains `‖entity‖ = 1` each step to
> prevent the model from trivially shrinking distances.

## 5.2 The limitations of TransE

Because each relation is a single translation, TransE struggles with relations
that are not one-to-one:

| Relation pattern                  | Problem in TransE                                  |
|-----------------------------------|----------------------------------------------------|
| 1-to-N (a country has many cities)| Many tails must equal `h+r` → they collapse.       |
| N-to-1 (many cities one country)  | Symmetric failure: heads collapse.                 |
| N-to-N                            | Cannot separate the many valid combinations.       |
| Symmetric (`r = r⁻¹`)             | Requires `r ≈ 0`, destroying information.          |

## 5.3 Fixes: TransH, TransR, TransD

- **TransH** — projects `h` and `t` onto a relation-specific hyperplane before
  translating, so an entity can behave differently under different relations.
- **TransR** — gives each relation its own space via a projection matrix `M_r`;
  translate in that relation space.
- **TransD** — dynamic projection depending on both entity and relation, with
  fewer parameters than TransR.

```
TransH: f = −‖ (h − wᵣᵀh·wᵣ) + dᵣ − (t − wᵣᵀt·wᵣ) ‖
TransR: f = −‖ Mᵣh + r − Mᵣt ‖
```

## 5.4 RotatE — relations as rotations

RotatE (Sun et al., 2019) models each relation as a **rotation in complex
space**. Entities live in `ℂ^d`, and each relation component has unit modulus:

```
t ≈ h ∘ r            (∘ = elementwise complex product)
f(h, r, t) = − ‖ h ∘ r − t ‖
with |r_i| = 1   (each r_i = e^{iθ_i}, a pure rotation)
```

Because rotation is invertible and composable, RotatE can model **symmetry**
(`θ = π` gives `r ∘ r = 1`), **antisymmetry**, **inversion**, and **composition**
of relations — a key expressiveness milestone.

> **In code:** [`kgc/models/rotate.py`](../kgc/models/rotate.py) parameterizes
> the relation by a phase `θ ∈ [−π, π]`, so `r = (cos θ, sin θ)` is automatically
> unit-modulus.

## Takeaways

- TransE: `h + r ≈ t`. Simple, strong baseline; weak on 1-N/N-1/N-N and symmetry.
- RotatE models relations as rotations, capturing symmetry/inversion/composition.

---

Prev: [Module 4](04_training_and_evaluation.md) · Next: [Module 6 — Tensor-Factorization Models](06_tensor_factorization_models.md)
