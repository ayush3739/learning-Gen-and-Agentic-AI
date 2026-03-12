> 📌 *Personal learning notes from the <a href="https://www.udemy.com/course/full-stack-ai-with-python/">Full Stack Generative and Agentic AI with Python</a> course.*

# 📘 Section 27: Graph Memory & Knowledge Graphs

This section uses **Neo4j** — a graph database — to store knowledge as a network of entities and relationships, enabling agents to reason over complex, interconnected information that flat documents cannot represent well.

---

## 📂 Files in This Section

| File | Topic |
|------|-------|
| `mem.py` | Neo4j knowledge graph implementation for agent memory |
| `graphs.excalidraw` | Graph database schema and query diagrams |

---

## ✅ What I Learned

### 🔹 What is a Knowledge Graph?
- A knowledge graph stores information as **nodes** (entities) and **edges** (relationships)
- Example: `(Alice) -[WORKS_AT]-> (Acme Corp)`, `(Acme Corp) -[LOCATED_IN]-> (New York)`
- Unlike a vector store, a knowledge graph captures **explicit relationships** between entities
- Supports complex multi-hop queries: "Who works at companies in New York?"

### 🔹 Graph Databases vs. Other Storage

| Storage | Best For |
|---------|----------|
| Relational DB (SQL) | Structured tabular data |
| Document DB (MongoDB) | Flexible JSON documents |
| Vector DB (Qdrant) | Semantic similarity search |
| Graph DB (Neo4j) | Highly connected, relationship-rich data |

### 🔹 Neo4j Fundamentals
- **Node** — an entity (person, place, concept, event)
- **Relationship** — a directed, named connection between two nodes
- **Property** — key-value attributes on nodes and relationships
- **Label** — categorises nodes (e.g., `:Person`, `:Company`, `:Topic`)
- **Cypher** — Neo4j's declarative query language (similar to SQL but for graphs)

### 🔹 Cypher Query Language
```cypher
// Create a node
CREATE (a:Person {name: "Alice", age: 30})

// Create a relationship
MATCH (a:Person {name: "Alice"}), (b:Company {name: "Acme"})
CREATE (a)-[:WORKS_AT {since: 2020}]->(b)

// Query: find all colleagues of Alice
MATCH (alice:Person {name: "Alice"})-[:WORKS_AT]->(company)<-[:WORKS_AT]-(colleague)
RETURN colleague.name

// Multi-hop: companies in New York that Alice's connections work at
MATCH (alice:Person {name: "Alice"})-[:KNOWS]->(friend)-[:WORKS_AT]->(company)-[:LOCATED_IN]->(:City {name: "New York"})
RETURN company.name
```

### 🔹 Graph Memory for AI Agents
- Agents extract entities and relationships from conversations and store them as graph nodes/edges
- Enables richer queries than flat text: "Who does the user know who works in AI?"
- The graph grows over time as the agent learns new facts
- Combine with vector search: embed node properties for semantic graph retrieval

### 🔹 Neo4j Python Driver
- `neo4j.GraphDatabase.driver(uri, auth=(user, password))`
- Execute Cypher with `session.run("QUERY", param=value)`
- Results are iterable `Record` objects
- Always close sessions and drivers properly

### 🔹 Entity Extraction for the Knowledge Graph
- Use the LLM to extract entities and relationships from user messages
- Prompt: "Extract all (subject, relationship, object) triples from this text and return as JSON"
- Parse the JSON response and write each triple to Neo4j

---

## 🛠️ Key Code Patterns

```python
import os
from neo4j import GraphDatabase
from openai import OpenAI
import json

NEO_URI = "bolt://localhost:7687"
NEO_USER = "neo4j"
NEO_PASS = os.getenv("NEO_PASSWORD")

driver = GraphDatabase.driver(NEO_URI, auth=(NEO_USER, NEO_PASS))
llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def add_triple(subject: str, relation: str, obj: str):
    with driver.session() as session:
        session.run(
            """
            MERGE (s:Entity {name: $subject})
            MERGE (o:Entity {name: $obj})
            MERGE (s)-[r:RELATION {type: $relation}]->(o)
            """,
            subject=subject, obj=obj, relation=relation,
        )

def extract_triples(text: str) -> list[dict]:
    resp = llm.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Extract (subject, relation, object) triples from the text. Return JSON array."},
            {"role": "user", "content": text},
        ],
        response_format={"type": "json_object"},
    )
    return json.loads(resp.choices[0].message.content).get("triples", [])

def query_connections(entity: str) -> list[dict]:
    with driver.session() as session:
        results = session.run(
            "MATCH (n:Entity {name: $name})-[r]->(m) RETURN r.type AS relation, m.name AS target",
            name=entity,
        )
        return [{"relation": r["relation"], "target": r["target"]} for r in results]

# Example
text = "Alice works at Acme Corp and knows Bob who lives in New York."
for triple in extract_triples(text):
    add_triple(triple["subject"], triple["relation"], triple["object"])

print(query_connections("Alice"))
# [{"relation": "works_at", "target": "Acme Corp"}, {"relation": "knows", "target": "Bob"}]
```

---

## 🐳 Docker Setup

```bash
# Start Neo4j
docker run -d \
  --name neo4j \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/your_password \
  neo4j:latest

# Neo4j Browser at http://localhost:7474
```

---

## 📌 Prerequisites
- [Section 25–26: Memory Layers in AI Agents](../section%2025-26%20%28Memory%20Latyer%20in%20AI%20Agents%29/README.md)
- Docker installed and running

## 📌 Next Section
➡️ [Section 28: Voice Agents & MCP](../section%2028%20%28Voice%20agents%20%26%20MCP%20%29/README.md)
