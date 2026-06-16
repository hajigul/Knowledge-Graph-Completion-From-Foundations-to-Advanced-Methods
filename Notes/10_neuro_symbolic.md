# Module 10 — Rules, Paths, and Neuro-Symbolic KGC

## 10.1 Why add logic?

Embeddings are powerful but opaque, and they can silently violate logical
constraints. Combining them with **symbolic rules** yields interpretable,
constraint-respecting predictions.

## 10.2 Rule mining

Systems like **AMIE** mine **Horn rules** directly from the KG, for example:

```
livesIn(x, y) ∧ capitalOf(z, y)  ⇒  citizenOf(x, z)
```

Each rule has a **confidence**:

```
confidence = support(body ∧ head) / support(body)
```

High-confidence rules can be applied to *predict* new triples or to *filter*
embedding-model predictions.

## 10.3 Path-based reasoning

- **Path Ranking Algorithm (PRA)** — uses random-walk path features between
  entities as predictors of a relation.
- **DeepPath / MINERVA** — reinforcement-learning agents that walk the graph to
  reach the answer, producing explainable paths.

```
Query:  (Einstein, nationalityOf, ?)
Path:   Einstein --bornIn--> Ulm --locatedIn--> Germany
Answer: Germany   (with a human-readable justification)
```

## 10.4 Differentiable rule learning

- **NeuralLP / DRUM** — learn logical rules end-to-end via differentiable matrix
  operations over the adjacency tensors, so rules and their confidences are
  trained by gradient descent.
- **Neural Theorem Provers** — soft-unify symbols using embeddings, blending
  proving with learning.

## 10.5 Injecting rules into embeddings

Approaches like **KALE** and **RUGE** add rule-satisfaction terms to the training
loss, so learned embeddings respect known logical regularities. Conceptually:

```
L_total = L_data  +  λ · L_rules
```

where `L_rules` penalizes embeddings that violate mined rules.

## 10.6 Trade-offs

| Approach              | Interpretable | Scalable | Learns from data |
|-----------------------|---------------|----------|------------------|
| Pure embeddings       | ✗             | ✓        | ✓                |
| Pure symbolic rules   | ✓             | ✗ (combinatorial) | partly  |
| Neuro-symbolic hybrid | ✓ (partly)    | moderate | ✓                |

## Takeaways

- Rules add interpretability and enforce logical consistency.
- Neuro-symbolic methods range from post-hoc rules to fully differentiable
  learning.

---

Prev: [Module 9](09_gnns_for_kgc.md) · Next: [Module 11 — Text, Multimodal, LLMs](11_text_and_llms.md)
