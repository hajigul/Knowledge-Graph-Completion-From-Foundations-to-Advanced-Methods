# References

The models and concepts in these notes come from the following works. Citations
are given in a lightweight format; consult the original papers for full details.

## Foundational embedding models

- **TransE** — Bordes, Usunier, Garcia-Durán, Weston, Yakhnenko. *Translating
  Embeddings for Modeling Multi-relational Data.* NeurIPS 2013.
- **RESCAL** — Nickel, Tresp, Kriegel. *A Three-Way Model for Collective
  Learning on Multi-Relational Data.* ICML 2011.
- **DistMult** — Yang, Yih, He, Gao, Deng. *Embedding Entities and Relations for
  Learning and Inference in Knowledge Bases.* ICLR 2015.
- **ComplEx** — Trouillon, Welbl, Riedel, Gaussier, Bouchard. *Complex Embeddings
  for Simple Link Prediction.* ICML 2016.
- **RotatE** — Sun, Deng, Nie, Tang. *RotatE: Knowledge Graph Embedding by
  Relational Rotation in Complex Space.* ICLR 2019.

## Translational variants

- **TransH** — Wang, Zhang, Feng, Chen. *Knowledge Graph Embedding by Translating
  on Hyperplanes.* AAAI 2014.
- **TransR** — Lin, Liu, Sun, Liu, Zhu. *Learning Entity and Relation Embeddings
  for Knowledge Graph Completion.* AAAI 2015.
- **TransD** — Ji, He, Xu, Liu, Zhao. *Knowledge Graph Embedding via Dynamic
  Mapping Matrix.* ACL 2015.

## Other tensor / neural models

- **HolE** — Nickel, Rosasco, Poggio. *Holographic Embeddings of Knowledge
  Graphs.* AAAI 2016.
- **SimplE** — Kazemi, Poole. *SimplE Embedding for Link Prediction in Knowledge
  Graphs.* NeurIPS 2018.
- **TuckER** — Balažević, Allen, Hospedales. *TuckER: Tensor Factorization for
  Knowledge Graph Completion.* EMNLP 2019.
- **ConvE** — Dettmers, Minervini, Stenetorp, Riedel. *Convolutional 2D Knowledge
  Graph Embeddings.* AAAI 2018.

## Graph neural networks

- **R-GCN** — Schlichtkrull, Kipf, Bloem, van den Berg, Titov, Welling.
  *Modeling Relational Data with Graph Convolutional Networks.* ESWC 2018.
- **CompGCN** — Vashishth, Sanyal, Nitin, Talukdar. *Composition-based
  Multi-Relational Graph Convolutional Networks.* ICLR 2020.
- **GraIL** — Teru, Denis, Hamilton. *Inductive Relation Prediction by Subgraph
  Reasoning.* ICML 2020.

## Rules, paths, neuro-symbolic

- **AMIE** — Galárraga, Teflioudi, Hose, Suchanek. *AMIE: Association Rule Mining
  under Incomplete Evidence in Ontological Knowledge Bases.* WWW 2013.
- **PRA** — Lao, Mitchell, Cohen. *Random Walk Inference and Learning in a Large
  Scale Knowledge Base.* EMNLP 2011.
- **MINERVA** — Das et al. *Go for a Walk and Arrive at the Answer: Reasoning
  over Paths in Knowledge Bases using Reinforcement Learning.* ICLR 2018.
- **NeuralLP** — Yang, Yang, Cohen. *Differentiable Learning of Logical Rules for
  Knowledge Base Reasoning.* NeurIPS 2017.
- **DRUM** — Sadeghian, Armandpour, Ding, Wang. *DRUM: End-To-End Differentiable
  Rule Mining on Knowledge Graphs.* NeurIPS 2019.

## Text, multimodal, LLM-based

- **DKRL** — Xie, Liu, Jia, Luan, Sun. *Representation Learning of Knowledge
  Graphs with Entity Descriptions.* AAAI 2016.
- **KG-BERT** — Yao, Mao, Luo. *KG-BERT: BERT for Knowledge Graph Completion.*
  arXiv 2019.
- **StarE** — Galkin, Trivedi, Maheshwari, Usbeck, Lehmann. *Message Passing for
  Hyper-Relational Knowledge Graphs.* EMNLP 2020.

## Temporal KGC

- **TA-DistMult / TA-TransE** — García-Durán, Dumančić, Niepert. *Learning
  Sequence Encoders for Temporal Knowledge Graph Completion.* EMNLP 2018.
- **TNTComplEx** — Lacroix, Obozinski, Usunier. *Tensor Decompositions for
  Temporal Knowledge Base Completion.* ICLR 2020.

## Benchmarks & evaluation

- **FB15k / WN18** — introduced with TransE (Bordes et al., 2013).
- **FB15k-237** — Toutanova, Chen. *Observed versus Latent Features for Knowledge
  Base and Text Inference.* 2015.
- **WN18RR** — introduced with ConvE (Dettmers et al., 2018).

## Surveys (recommended further reading)

- Wang, Mao, Wang, Guo. *Knowledge Graph Embedding: A Survey of Approaches and
  Applications.* IEEE TKDE 2017.
- Ji, Pan, Cambria, Marttinen, Yu. *A Survey on Knowledge Graphs:
  Representation, Acquisition, and Applications.* IEEE TNNLS 2021.

## Libraries that inspired the structure

- OpenKE, PyKEEN, LibKGE, AmpliGraph, DGL-KE, PyTorch-BigGraph.

> These notes paraphrase and summarize ideas from the works above for teaching
> purposes. For any quotation, formal result, or experimental number, cite the
> original paper directly.
