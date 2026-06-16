# Knowledge Graph Completion — Lecture Notes

A complete course on Knowledge Graph Completion (KGC), from foundations to the
research frontier. These notes are designed to be read alongside the code in
this repository: wherever a concept maps to an implementation, the relevant file
is linked.

## Suggested track

- **Beginner (Modules 1–4):** what a knowledge graph is, how completion is
  framed, how we represent graphs for ML, and how we train and evaluate.
- **Intermediate (Modules 5–8):** the two great families of embedding models
  and how to assemble a working pipeline.
- **Advanced (Modules 9–12):** graph neural networks, neuro-symbolic methods,
  text/LLM-based KGC, and open problems.

## Contents

1. [What Is a Knowledge Graph?](01_what_is_a_kg.md)
2. [The Knowledge Graph Completion Problem](02_the_kgc_problem.md)
3. [Representing a Graph for Machine Learning](03_representing_graphs.md)
4. [Training and Evaluation](04_training_and_evaluation.md)
5. [Translational Models](05_translational_models.md)
6. [Tensor-Factorization Models](06_tensor_factorization_models.md)
7. [Relation Patterns and Expressiveness](07_relation_patterns.md)
8. [Practical KGC Pipeline](08_practical_pipeline.md)
9. [Graph Neural Networks for KGC](09_gnns_for_kgc.md)
10. [Rules, Paths, and Neuro-Symbolic KGC](10_neuro_symbolic.md)
11. [Text, Multimodal, and LLM-Based KGC](11_text_and_llms.md)
12. [Advanced Topics and Open Problems](12_advanced_topics.md)

### Appendices

- [Model Cheat Sheet](APPENDIX_cheatsheet.md)
- [Exercises](APPENDIX_exercises.md)
- [Glossary](GLOSSARY.md)
- [References](REFERENCES.md)

## Notation

| Symbol | Meaning |
|--------|---------|
| `E`, `R` | sets of entities and relations |
| `(h, r, t)` | a triple: head, relation, tail |
| `h, r, t` (bold) | embedding vectors of `h`, `r`, `t` |
| `d` | embedding dimension |
| `f(h, r, t)` | scoring function (higher = more plausible) |
| `‖·‖` | a vector norm (L1 or L2) |
| `∘` | elementwise (Hadamard / complex) product |
| `⟨a, b, c⟩` | trilinear dot product `Σ_i a_i b_i c_i` |
