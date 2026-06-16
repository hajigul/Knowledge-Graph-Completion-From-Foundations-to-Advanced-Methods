# Appendix B — Exercises

## Conceptual

1. Explain why the open-world assumption complicates negative sampling.
2. Show, using `h + r ≈ t`, why TransE cannot model a symmetric relation without
   losing information.
3. The correct tail of a test query is ranked 5th. Compute its reciprocal rank
   and state its contribution to Hits@1, Hits@3, and Hits@10.

## Analytical

4. Prove that DistMult assigns the same score to `(h, r, t)` and `(t, r, h)`,
   and explain the practical consequence.
5. Starting from `Re(h · r · conj(t))`, derive the four-term real-valued formula
   used in `ComplEx.score_hrt` and explain which term breaks symmetry.
6. For each of the four relation patterns (symmetry, antisymmetry, inversion,
   composition), name one model that captures it and one that does not.

## Applied (with this repo)

7. Run `python examples/compare_models.py`. Which model wins on the toy KG's
   composition chain (`bornIn ∘ locatedIn ⇒ nationalityOf`)? Does the result
   match the pattern table in Module 7? Explain.
8. Modify `TripleBatcher` to implement **Bernoulli** corruption (choose
   head-vs-tail corruption based on each relation's average head/tail
   cardinality). Measure the effect on filtered MRR.
9. Add an **N3 regularizer** to `ComplEx` and compare against L2 on the toy KG.
10. Implement an `RGCNEncoder` (Module 9) that outputs entity embeddings and feed
    them to the existing `DistMult` decoder. Keep the `score_hrt` interface
    unchanged.
11. Build a **filtered vs raw** comparison: temporarily disable filtering in the
    evaluator and quantify how much the metrics inflate. Why does this happen?
12. Design a hybrid pipeline (Module 11) that takes the top-10 candidates from
    `score_all_tails` and re-ranks them with an external verifier. List the
    failure modes you must guard against.

## Solutions

Short solution sketches:

- **(3)** Reciprocal rank `= 1/5 = 0.2`; counts toward Hits@10 only.
- **(4)** Swapping `h` and `t` leaves `Σ_i h_i r_i t_i` unchanged → identical
  score → cannot represent any relation that should hold in one direction only.
- **(5)** The `−⟨b, d, e⟩` term (imag·imag·real) flips sign under `h↔t`, which is
  what lets ComplEx distinguish a relation from its inverse.
