# Module 9 — Graph Neural Networks for KGC

## 9.1 Why go beyond shallow embeddings

Shallow embeddings (Modules 5–6) treat each entity independently. **Graph neural
networks (GNNs)** instead compute an entity's representation from its
**neighborhood**, letting structural context flow into the embedding through
**message passing**.

## 9.2 Message passing in one equation

```
h_v^{(l+1)} = σ ( Σ_{u ∈ N(v)} W · h_u^{(l)}  +  W_self · h_v^{(l)} )

N(v) = neighbors of node v
W    = learnable weight,  σ = nonlinearity
```

Stacking `L` such layers lets information travel `L` hops across the graph.

## 9.3 R-GCN — relational GCN

Standard GCNs ignore edge types. **R-GCN** (Schlichtkrull et al., 2018) uses a
**separate weight matrix per relation**, aggregating neighbors grouped by
relation:

```
h_v^{(l+1)} = σ ( Σ_{r∈R} Σ_{u∈N_r(v)} (1/c_{v,r}) W_r h_u^{(l)} + W_0 h_v^{(l)} )
```

To avoid a parameter explosion with many relations, R-GCN uses **basis
decomposition** — each `W_r` is a learned combination of shared basis matrices.

## 9.4 The encoder–decoder view

Modern GNN-based KGC follows an **encoder–decoder** design:

- **Encoder** (the GNN) produces context-aware entity embeddings.
- **Decoder** (a classic scoring function like DistMult or ComplEx) scores
  triples from those embeddings.

This means the models you built in Modules 5–6 are reusable as decoders.

- **CompGCN** — jointly embeds nodes *and* relations using composition operators
  (subtraction, multiplication, circular correlation).
- **Attention-based (KBGAT, etc.)** — learn per-neighbor attention weights
  instead of fixed normalization.

## 9.5 Trade-offs

| Aspect                          | Shallow KGE                  | GNN-based            |
|---------------------------------|------------------------------|----------------------|
| Uses neighborhood structure     | No                           | Yes                  |
| Inductive (unseen entities)     | Hard                         | More natural         |
| Compute cost                    | Lower                        | Higher               |
| Standard-benchmark performance  | Surprisingly competitive     | Strong, not always SOTA |

> A recurring research finding: well-tuned shallow models (ComplEx, RotatE)
> often match or beat heavier GNNs on FB15k-237 / WN18RR. GNNs shine most when
> structure or inductiveness is essential.

## 9.6 How you would extend this repo

The encoder–decoder split means you could add an `RGCNEncoder` that outputs
entity embeddings, then feed them to the existing `DistMult.score_hrt`. The base
class in [`kgc/models/base.py`](../kgc/models/base.py) is intentionally small to
make that straightforward as an exercise.

## Takeaways

- GNNs build embeddings from neighborhoods via relation-aware message passing.
- R-GCN / CompGCN encoders pair with bilinear decoders; powerful but
  compute-heavy.

---

Prev: [Module 8](08_practical_pipeline.md) · Next: [Module 10 — Neuro-Symbolic KGC](10_neuro_symbolic.md)
