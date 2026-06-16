# Appendix A — Model Cheat Sheet

## Scoring functions

| Model    | Scoring function `f(h, r, t)`              | Family                | Code |
|----------|--------------------------------------------|-----------------------|------|
| TransE   | `−‖h + r − t‖`                             | Translational         | [transe.py](../kgc/models/transe.py) |
| TransR   | `−‖Mᵣh + r − Mᵣt‖`                         | Translational         | — |
| RotatE   | `−‖h ∘ r − t‖`, `\|r_i\|=1`                | Translational (complex)| [rotate.py](../kgc/models/rotate.py) |
| RESCAL   | `hᵀ Mᵣ t`                                  | Bilinear              | — |
| DistMult | `⟨h, r, t⟩`                                | Bilinear (diagonal)   | [distmult.py](../kgc/models/distmult.py) |
| ComplEx  | `Re(⟨h, r, conj(t)⟩)`                      | Bilinear (complex)    | [complex_model.py](../kgc/models/complex_model.py) |
| ConvE    | `g(vec(g([h;r] ∗ ω)) W) · t`               | Neural                | — |
| R-GCN    | GNN encoder + DistMult decoder             | GNN                   | — |

(Dashes mark models discussed in the notes but left as extension exercises.)

## Pattern coverage

| Model    | Symmetry | Antisymmetry | Inversion | Composition |
|----------|----------|--------------|-----------|-------------|
| TransE   | ✗        | ✓            | ✓         | ✓           |
| DistMult | ✓        | ✗            | ✗         | ✗           |
| ComplEx  | ✓        | ✓            | ✓         | ✗           |
| RotatE   | ✓        | ✓            | ✓         | ✓           |

## Typical hyperparameters (real benchmarks)

| Hyperparameter      | Typical range     |
|---------------------|-------------------|
| Embedding dim `d`   | 100–1000          |
| Learning rate       | 1e-3 – 1e-1       |
| Negatives/positive  | 50–1000           |
| Margin `γ` (TransE) | 1–12              |
| L2 / N3 reg         | 1e-6 – 1e-4       |
| Epochs              | 100–1000          |

## Default loss pairing

| Model    | Common loss            |
|----------|------------------------|
| TransE   | margin ranking         |
| RotatE   | self-adversarial margin|
| DistMult | binary cross-entropy   |
| ComplEx  | binary cross-entropy   |
