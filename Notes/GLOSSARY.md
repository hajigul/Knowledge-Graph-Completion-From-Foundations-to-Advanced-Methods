# Glossary

| Term | Meaning |
|------|---------|
| **Triple** | An ordered fact `(head, relation, tail)`. |
| **Entity** | A node in the graph: a real-world object or concept. |
| **Relation** | A typed, directed edge connecting two entities. |
| **Embedding** | A learned dense vector representing an entity or relation. |
| **Scoring function** | Maps a triple to a plausibility score (higher = more likely true). |
| **Link prediction** | Predicting a missing head or tail entity for a query. |
| **Triple classification** | Deciding whether a given triple is true or false. |
| **Corruption** | Replacing head/tail to create a negative training example. |
| **Negative sampling** | Generating negative triples (uniform, Bernoulli, self-adversarial). |
| **Filtered ranking** | Removing other known-true triples before ranking a test triple. |
| **MR** | Mean Rank — average rank of the correct entity (lower is better). |
| **MRR** | Mean Reciprocal Rank — average of `1/rank` (higher is better). |
| **Hits@k** | Fraction of queries where the correct answer is in the top `k`. |
| **CWA / OWA** | Closed-world / Open-world assumption about missing facts. |
| **Translational model** | Treats a relation as a translation/transformation (TransE, RotatE). |
| **Bilinear model** | Scores triples by a multiplicative product (RESCAL, DistMult, ComplEx). |
| **Tensor factorization** | Viewing the KG as a 3-D tensor and factorizing it. |
| **Symmetry / antisymmetry** | Whether `r(x,y)` implies `r(y,x)` or `¬r(y,x)`. |
| **Inversion** | Two relations that are each other's reverse (`hypernym`/`hyponym`). |
| **Composition** | A relation implied by chaining two others. |
| **Transductive** | Cannot handle entities unseen during training. |
| **Inductive** | Generalizes to entities or graphs unseen during training. |
| **GNN** | Graph neural network; builds embeddings via neighborhood message passing. |
| **R-GCN** | Relational GCN with per-relation weight matrices. |
| **Encoder–decoder (KGC)** | GNN encoder produces embeddings; a scoring function decodes triples. |
| **Neuro-symbolic** | Combining neural embeddings with logical rules. |
| **Temporal KGC** | Completion where facts carry timestamps. |
| **Hyper-relational fact** | A fact with extra qualifier key–value pairs. |
| **Calibration** | Turning raw scores into meaningful probabilities. |
