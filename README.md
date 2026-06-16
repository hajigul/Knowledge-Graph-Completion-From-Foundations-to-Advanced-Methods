# Knowledge Graph Completion — Code + Lecture Notes

A **teaching-oriented** repository for learning Knowledge Graph Completion (KGC),
also known as link prediction. It pairs clean, readable PyTorch implementations
of classic knowledge graph embedding models with a full set of markdown lecture
notes that build the subject from first principles to advanced research topics.

> If you want the theory, start in [`notes/`](notes/README.md).
> If you want to run code, jump to [Quickstart](#quickstart).

---

## What's inside

```
kgc-repo/
├── kgc/                      # the library
│   ├── data/                 # dataset loading + negative sampling
│   ├── models/               # TransE, DistMult, ComplEx, RotatE
│   ├── training/             # losses + trainer
│   └── evaluation/           # filtered link-prediction metrics
├── notes/                    # 12 markdown lecture modules + appendices
├── scripts/                  # CLI: make_toy_dataset.py, train.py
├── examples/                 # compare_models.py walkthrough
├── tests/                    # pytest unit tests
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Implemented models

| Model    | Scoring function                         | Captures (S / A / Inv / Comp) |
|----------|------------------------------------------|-------------------------------|
| TransE   | `-‖h + r − t‖`                           | ✗ / ✓ / ✓ / ✓                 |
| DistMult | `⟨h, r, t⟩`                              | ✓ / ✗ / ✗ / ✗                 |
| ComplEx  | `Re(⟨h, r, conj(t)⟩)`                    | ✓ / ✓ / ✓ / ✗                 |
| RotatE   | `-‖h ∘ r − t‖`, `\|r_i\|=1`              | ✓ / ✓ / ✓ / ✓                 |

(S = symmetry, A = antisymmetry, Inv = inversion, Comp = composition. See
[Module 7](notes/07_relation_patterns.md).)

---

## Quickstart

### 1. Install

```bash
git clone https://github.com/<your-username>/kgc-repo.git
cd kgc-repo
python -m venv .venv && source .venv/bin/activate    # optional
pip install -r requirements.txt
pip install -e .                                       # editable install
```

> For a CPU-only PyTorch build, see https://pytorch.org/get-started/locally/.

### 2. Make a toy dataset

```bash
python scripts/make_toy_dataset.py --out data/toy
```

This writes a small synthetic family/geography KG with clear logical patterns
(symmetry, inversion, composition) so you can sanity-check models instantly.

### 3. Train a model

```bash
python scripts/train.py --data data/toy --model rotate \
    --dim 64 --epochs 100 --lr 0.05 --negatives 8
```

You should see the training loss fall and validation MRR/Hits@k rise, followed
by a final filtered test report.

### 4. Compare all four models

```bash
python examples/compare_models.py
```

---

## Using your own data

Point `--data` at any directory containing three tab-separated files:

```
train.txt
valid.txt
test.txt
```

Each line is a triple:

```
head_entity <TAB> relation <TAB> tail_entity
```

To use a standard benchmark such as **FB15k-237** or **WN18RR**, download it
(e.g. from the OpenKE or KGE-benchmark repositories), place the three files in
`data/FB15k-237/`, and run:

```bash
python scripts/train.py --data data/FB15k-237 --model complex \
    --dim 200 --epochs 300 --loss bce --l2 1e-5 --negatives 64
```

> These benchmarks are not bundled here to keep the repo small and avoid
> redistributing third-party data. See [Module 4](notes/04_training_and_evaluation.md)
> for why FB15k-237 / WN18RR are preferred over the leaky FB15k / WN18.

---

## The library in 20 lines

```python
from kgc.data.dataset import KGDataset
from kgc.models import build_model
from kgc.training.trainer import Trainer, TrainConfig

ds = KGDataset.load("data/toy")
model = build_model("complex", ds.num_entities, ds.num_relations, dim=128)

cfg = TrainConfig(epochs=100, loss="bce", lr=0.05, l2=1e-5)
trainer = Trainer(model, ds, cfg)
trainer.train()          # trains with early stopping on filtered valid MRR
metrics = trainer.test() # filtered MRR / Hits@{1,3,10} on the test split
print(metrics)
```

---

## Evaluation protocol

All metrics use **filtered ranking**: when ranking the true tail of `(h, r, t)`,
every *other* known-true tail is masked out first, so the model is not penalized
for ranking a different correct answer highly. We report:

- **MR** — mean rank (lower is better)
- **MRR** — mean reciprocal rank (higher is better)
- **Hits@1 / Hits@3 / Hits@10** — fraction of correct answers in the top-k

See [Module 4](notes/04_training_and_evaluation.md) for the full derivation.

---

## Lecture notes

The [`notes/`](notes/README.md) directory contains a complete, self-contained
course (also available as a single Word document via the original notes export):

| Module | Topic |
|--------|-------|
| 1  | What is a knowledge graph? |
| 2  | The KGC problem |
| 3  | Representing a graph for ML |
| 4  | Training and evaluation |
| 5  | Translational models (TransE → RotatE) |
| 6  | Tensor-factorization models (RESCAL → ComplEx) |
| 7  | Relation patterns and expressiveness |
| 8  | Practical KGC pipeline |
| 9  | Graph neural networks for KGC |
| 10 | Rules, paths, neuro-symbolic KGC |
| 11 | Text, multimodal, and LLM-based KGC |
| 12 | Advanced topics and open problems |

---

## Running the tests

```bash
pytest -q
```

---

## Contributing

This is an educational codebase: clarity beats micro-optimization. PRs that add
models, datasets, or notes modules in the same readable style are welcome.

## License

[MIT](LICENSE).

## Citation / acknowledgements

The models implemented here are from their original papers: TransE (Bordes et al.,
2013), DistMult (Yang et al., 2015), ComplEx (Trouillon et al., 2016), and RotatE
(Sun et al., 2019). Full references are in [`notes/REFERENCES.md`](notes/REFERENCES.md).
