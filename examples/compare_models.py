"""End-to-end example: train all four models on the toy KG and compare them.

This mirrors the workflow described in the lecture notes (Modules 4-8):
load data -> build model -> train with negative sampling -> filtered eval.

Run:
    python examples/compare_models.py
"""

from __future__ import annotations

import os
import subprocess
import sys

# Make `kgc` importable when run from the repo root without installation.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kgc.data.dataset import KGDataset
from kgc.models import build_model
from kgc.training.trainer import Trainer, TrainConfig


def ensure_toy_dataset(path: str = "data/toy") -> str:
    if not os.path.exists(os.path.join(path, "train.txt")):
        subprocess.run(
            [sys.executable, "scripts/make_toy_dataset.py", "--out", path],
            check=True,
        )
    return path


def main():
    data_dir = ensure_toy_dataset()
    ds = KGDataset.load(data_dir)
    print(f"Dataset: {ds.num_entities} entities, {ds.num_relations} relations, "
          f"{len(ds.train)} train triples.\n")

    configs = {
        "transe":   dict(loss="margin", lr=0.05, margin=1.0, normalize_entities=True),
        "distmult": dict(loss="bce",    lr=0.05, l2=1e-5,    normalize_entities=False),
        "complex":  dict(loss="bce",    lr=0.05, l2=1e-5,    normalize_entities=False),
        "rotate":   dict(loss="margin", lr=0.05, margin=6.0, normalize_entities=False),
    }

    results = {}
    for name, extra in configs.items():
        print(f"=== Training {name} ===")
        model = build_model(name, ds.num_entities, ds.num_relations, dim=64)
        cfg = TrainConfig(
            epochs=80, batch_size=512, num_negatives=8,
            eval_every=80, patience=10, verbose=False, **extra,
        )
        trainer = Trainer(model, ds, cfg)
        trainer.train()
        results[name] = trainer.test()
        print()

    print("\n==== Summary (test set, filtered) ====")
    header = f"{'model':<10}{'MRR':>8}{'H@1':>8}{'H@3':>8}{'H@10':>8}"
    print(header)
    print("-" * len(header))
    for name, m in results.items():
        print(f"{name:<10}{m['MRR']:>8.3f}{m['Hits@1']:>8.3f}"
              f"{m['Hits@3']:>8.3f}{m['Hits@10']:>8.3f}")


if __name__ == "__main__":
    main()
