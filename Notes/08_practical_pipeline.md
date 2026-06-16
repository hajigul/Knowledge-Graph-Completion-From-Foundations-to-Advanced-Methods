# Module 8 — Practical KGC Pipeline

This module turns theory into a working system. Every step below maps to code in
this repository.

## 8.1 End-to-end steps

1. Ingest triples; build entity/relation index (string → integer id).
2. Split into train/validation/test, ensuring no leakage of inverse triples.
3. Initialize embeddings (e.g., Xavier/uniform).
4. For each batch: sample positives, generate corrupted negatives.
5. Compute scores and loss; backpropagate; update embeddings.
6. Periodically evaluate filtered MRR on validation; early-stop.
7. Report test MRR and Hits@{1,3,10}.

| Step | Code |
|------|------|
| 1–2  | [`kgc/data/dataset.py`](../kgc/data/dataset.py) (`KGDataset.load`) |
| 3    | model `__init__` + `_init_embedding` in [`base.py`](../kgc/models/base.py) |
| 4    | `TripleBatcher` in [`dataset.py`](../kgc/data/dataset.py) |
| 5    | `Trainer._step` in [`trainer.py`](../kgc/training/trainer.py) |
| 6    | `Trainer.train` + `LinkPredictionEvaluator` |
| 7    | `Trainer.test` |

## 8.2 Minimal training loop (pseudocode)

```python
for epoch in range(E):
    for (h, r, t) in batches(train):
        t_neg = sample_corrupt(h, r)          # negative tail
        s_pos = score(h, r, t)
        s_neg = score(h, r, t_neg)
        loss  = max(0, margin + s_neg - s_pos)  # TransE-style
        loss.backward(); optim.step()
        normalize(entity_embeddings)           # constrain ‖e‖ = 1
    if epoch % eval_every == 0:
        mrr = filtered_mrr(model, valid, all_known_triples)
```

The real implementation in `Trainer._step` is only slightly longer (it supports
multiple negatives, the BCE loss, and optional L2 regularization).

## 8.3 Hyperparameters that matter

- **Embedding dimension `d`** — typically 100–1000; larger = more capacity and
  compute.
- **Margin `γ` / loss type** — tune jointly with the learning rate.
- **Negatives per positive** — more usually helps (e.g., 50–1000 on real data).
- **Regularization** — L2 or N3 curbs overfitting in bilinear models.

```bash
# A reasonable ComplEx config on a real benchmark
python scripts/train.py --data data/FB15k-237 --model complex \
    --dim 200 --loss bce --l2 1e-5 --negatives 64 --epochs 300 --lr 0.01
```

## 8.4 Common pitfalls

- Reporting **raw** instead of **filtered** metrics (inflates everything).
- Using FB15k/WN18 and mistaking inverse-leakage for real performance.
- Forgetting to **normalize** entity embeddings in translational models.
- Too few negatives, or a learning rate that diverges early.

## 8.5 Reproducibility checklist

- Fix all random seeds (`TrainConfig.seed`).
- Log the exact config alongside results.
- Report filtered MRR + Hits@{1,3,10}, averaged over head and tail prediction.
- State the dataset version (e.g. FB15k-**237**, not FB15k).

## Takeaways

- A KGC system = indexing + sampling + scoring + filtered evaluation.
- Most failures are evaluation bugs, not model bugs.

---

Prev: [Module 7](07_relation_patterns.md) · Next: [Module 9 — GNNs for KGC](09_gnns_for_kgc.md)
