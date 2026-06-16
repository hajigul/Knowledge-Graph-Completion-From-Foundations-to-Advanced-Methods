# Module 1 — What Is a Knowledge Graph?

## 1.1 Intuition

A **knowledge graph (KG)** is a structured way of representing facts about the
world as a network. Each fact is a relationship between two things. The fact
"Paris is the capital of France" connects the entity *Paris* to the entity
*France* through the relation *capitalOf*.

Drawn as a graph, entities are **nodes** and relations are **directed, typed
edges**:

```
 (Paris) ──capitalOf──▶ (France) ──locatedIn──▶ (Europe)
```

## 1.2 Formal definition

A knowledge graph is a set of **triples**. A triple is written:

```
(h, r, t)

h = head entity   (subject)
r = relation      (predicate)
t = tail entity   (object)
```

Formally, given a set of entities `E` and a set of relations `R`:

```
G ⊆ E × R × E
```

Each element of `G` is an observed (assumed-true) fact. Example triples:

```
(Paris,    capitalOf, France)
(France,   locatedIn, Europe)
(Einstein, bornIn,    Ulm)
(Einstein, fieldOf,   Physics)
```

> **In code:** the loader in
> [`kgc/data/dataset.py`](../kgc/data/dataset.py) reads exactly this
> tab-separated triple format and maps each string symbol to an integer id.

## 1.3 Why graphs?

- **Compositionality** — facts chain together (`Paris → France → Europe`),
  enabling multi-hop reasoning.
- **Heterogeneity** — many entity and relation types coexist in one structure.
- **Machine-readability** — triples power search, recommendation, and question
  answering.

## 1.4 Real-world knowledge graphs

| KG        | Origin                       | Scale (approx.)     | Typical use                 |
|-----------|------------------------------|---------------------|-----------------------------|
| Freebase  | Metaweb / Google             | ~1.9B triples       | Historical research benchmark |
| Wikidata  | Wikimedia                    | 100M+ entities      | Open collaborative KG       |
| DBpedia   | Wikipedia infoboxes          | Billions of triples | Linked Open Data            |
| YAGO      | Wikipedia + WordNet          | Millions of facts   | Typed, temporal facts       |
| Google KG | Google (proprietary)         | Tens of billions    | Search panels               |

## 1.5 Key terms

- **Entity** — a real-world object or concept (a node).
- **Relation** — a typed, directed edge connecting two entities.
- **Triple / fact** — an edge instance `(h, r, t)`.
- **Schema / ontology** — optional rules about valid entity and relation types.

## Takeaways

- A KG = a set of `(head, relation, tail)` triples over entities `E` and
  relations `R`.
- Graphs enable multi-hop, compositional reasoning across heterogeneous facts.

---

Next: [Module 2 — The Knowledge Graph Completion Problem](02_the_kgc_problem.md)
