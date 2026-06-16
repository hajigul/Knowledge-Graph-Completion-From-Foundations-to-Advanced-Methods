# Module 12 — Advanced Topics and Open Problems

## 12.1 Temporal KGC

Many facts are time-stamped: `(Obama, presidentOf, USA, [2009–2017])`.
**Temporal KGC** predicts facts at specific times. Models (TTransE, TA-DistMult,
TNTComplEx, TeMP) add time embeddings or make relation embeddings
time-dependent.

```
f(h, r, t, τ)   — score now depends on a timestamp τ
```

## 12.2 Inductive KGC

Standard (transductive) models cannot handle entities unseen at training time.
**Inductive** methods (GraIL, NodePiece, BERTRL) reason over local subgraph
structure or text, so they generalize to new entities and even new graphs.

## 12.3 Hyper-relational and n-ary facts

Real facts often need qualifiers:

```
(Einstein, educatedAt, ETH Zurich, {degree: BSc, year: 1900})
```

**Hyper-relational** models (StarE, HINGE) extend triples to capture these
qualifier key–value pairs, which are common in Wikidata.

## 12.4 Uncertainty and calibration

- Raw scores are **not probabilities**; calibrate before thresholding.
- Probabilistic and Bayesian KGEs quantify confidence, which matters when
  predictions feed downstream decisions.

## 12.5 Scalability

Billion-edge KGs need:

- efficient negative sampling,
- mixed-precision training,
- distributed frameworks (e.g. PyTorch-BigGraph, DGL-KE).

## 12.6 Open research problems

1. **Robust evaluation** beyond leakage-prone benchmarks.
2. **Combining symbolic guarantees with neural flexibility** at scale.
3. **Faithful, explainable multi-hop reasoning.**
4. **Continual / temporal updating** as the world changes.
5. **Fair, bias-aware completion** — avoiding amplifying social biases present
   in the underlying facts.

## 12.7 Where to go next

- Reimplement a GNN encoder (Module 9) on top of this repo's decoders.
- Add a temporal variant of ComplEx (TNTComplEx) and test on ICEWS data.
- Build a hybrid LLM-verification stage (Module 11) over the top-k candidates
  returned by `score_all_tails`.

## Takeaways

- Frontier KGC handles time, unseen entities, n-ary facts, scale, and trust.
- The field is converging toward grounded, explainable, hybrid systems.

---

Prev: [Module 11](11_text_and_llms.md) · Back to [Notes index](README.md)
