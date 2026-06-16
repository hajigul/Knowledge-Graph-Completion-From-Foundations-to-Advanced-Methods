# Module 11 — Text, Multimodal, and LLM-Based KGC

## 11.1 Using entity descriptions

Entities often have textual descriptions. **DKRL** and **KG-BERT** encode these
with text encoders so that even rarely-connected entities get informative
embeddings — a route to **inductive** prediction (handling entities unseen at
training time).

**KG-BERT** reframes triple classification as a sentence-pair task: feed the
concatenated textual forms of `h`, `r`, `t` into BERT and predict plausibility.

```
[CLS] Albert Einstein [SEP] place of birth [SEP] Ulm [SEP]  → P(true)
```

## 11.2 Multimodal KGC

- Incorporate **images**, **numeric attributes**, and **types** alongside
  structure.
- Fuse modalities by concatenation, attention, or separate scoring channels.
- Useful in domains like e-commerce (product images) and biomedicine (molecular
  structures).

## 11.3 LLMs for KGC

Large language models contribute in several ways:

- **Triple completion by prompting** — ask the LLM to predict the missing
  entity, optionally constrained to a candidate set retrieved from the KG.
- **KG construction / extraction** — LLMs extract triples from raw text to grow
  the KG.
- **Verification & re-ranking** — use an LLM to filter or re-score candidate
  triples produced by an embedding model.
- **Retrieval-augmented reasoning** — combine KG retrieval with LLM generation
  for multi-hop question answering.

A common, robust pattern is a **hybrid pipeline**:

```
embedding model → top-k candidates → LLM verifies/re-ranks → final prediction
```

The embedding model provides cheap recall; the LLM provides semantic precision.

## 11.4 Caution with LLM-based KGC

- LLMs can **hallucinate** plausible-sounding but false facts.
- They may **leak benchmark data** seen during pretraining, inflating scores.
- Always validate against held-out, **leakage-controlled** splits, and prefer
  hybrid designs where the KG **grounds** the model.

## Takeaways

- Text / multimodal signals help rare and unseen entities (inductive KGC).
- LLMs assist with extraction, completion, and verification — but need
  grounding and careful evaluation.

---

Prev: [Module 10](10_neuro_symbolic.md) · Next: [Module 12 — Advanced Topics](12_advanced_topics.md)
