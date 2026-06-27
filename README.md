# Agentic AI — Learners' Space 2026
### Mudil Goel | 24B3932 | Department of Electrical Engineering, IIT Bombay

A 4-week intensive bootcamp covering the full stack of modern AI agent development —
from foundational LLM concepts to autonomous multi-agent systems.

---

## Overview

This repository documents my complete journey through the Agentic AI Learners' Space
2026 at IIT Bombay. Each week builds on the last, starting from how LLMs work and
ending with the orchestration of fully autonomous multi-agent workflows.

---

## Repository Structure
Agentic-AI/

├── Week 1 - studyBuddy.py          # Study Buddy bot using Anthropic API

├── LLMs, Prompting and LLM.pdf     # Week 1 assignment submission

├── RAG pipeline.ipynb              # Week 2: Full RAG pipeline from scratch

├── Chunking Strategies.ipynb       # Week 2: Chunking strategy comparison

├── RAG vs Fine Tuning.ipynb        # Week 2: Decision framework + hallucination test

├── Leadership and Management...    # Source document used for RAG

└── README.md

---

## Week 1: Understanding LLMs, Prompting, and APIs

**Concepts Covered:**
- How Large Language Models process and generate text
- Context windows — what they are, why they matter, what happens when you exceed them
- Prompt engineering techniques: zero-shot, few-shot, chain-of-thought, system prompts
- OpenAI and Anthropic API — authentication, messages format, parsing responses

**Built:**
- **Study Buddy Bot** (`Week 1 - studyBuddy.py`) — A CLI chatbot powered by
  `claude-haiku-4-5-20251001` via the Anthropic API. Takes a topic as input,
  validates it, and returns a simple explanation in under 100 words.

**Key Takeaway:**
The way you phrase a prompt fundamentally changes the output. Few-shot prompting
outperforms zero-shot by constraining the model's output format and reducing
hallucination — the model pattern-matches against the examples you provide.

---

## Week 2: Retrieval Augmented Generation (RAG) and Fine-Tuning

**Concepts Covered:**
- RAG vs Fine-Tuning — when to use which (facts vs behaviour)
- The 5-stage RAG pipeline: Document Loading → Chunking → Embedding → Vector Store → Retrieval → Generation
- Embeddings and semantic similarity (all-MiniLM-L6-v2, 384 dimensions)
- Cosine similarity — implemented from scratch
- Chunking strategies and their effect on retrieval quality
- Hallucination guards using cosine similarity thresholds
- Fine-tuning concepts: when model weights need to change

**Built:**

**1. Minimal RAG Pipeline from Scratch** (`RAG pipeline.ipynb`)
- Fixed-size chunking with overlap (chunk_size=200, overlap=40)
- Sentence embeddings using `sentence-transformers`
- Cosine similarity retrieval implemented manually (no sklearn)
- Generation using `google/flan-t5-base` via HuggingFace Transformers
- Hallucination guard: out-of-scope queries correctly return "I don't know"

**2. Chunking Strategy Showdown** (`Chunking Strategies.ipynb`)
- Implemented three chunking strategies from scratch:
  - Fixed-size chunking
  - Sentence-based chunking (regex sentence splitting, 5-sentence groups)
  - Sliding window chunking (window=400, step=100)
- Built a benchmark of 5 QA pairs and measured Hit Rate for each strategy
- Result: all three achieved 4/5 hit rate on this document

| Strategy | Chunks | Mean Length | Hit Rate |
|---|---|---|---|
| Fixed-size | 17 | 282 words | 4/5 |
| Sentence-based | 61 | 82 words | 4/5 |
| Sliding window | 41 | 378 words | 4/5 |

**3. RAG vs Fine-Tuning Decision Framework** (`RAG vs Fine Tuning.ipynb`)
- Decision tree function mapping 5 scenario parameters to one of:
  RAG / Fine-Tuning / RAG + Fine-Tuning / Prompt Engineering only
- Hallucination stress test: 6 queries (3 answerable, 3 out-of-scope)
- Bar chart showing cosine similarity scores color-coded by query type
- Clear pattern: answerable queries score 0.64–0.79, out-of-scope score 0.08–0.11

**Key Takeaway:**
Cosine similarity scores are a reliable hallucination guard. A threshold of ~0.3
cleanly separates queries the document can answer from those it cannot.

---

## Week 3: MCP, LangChain, and LangGraph *(In Progress)*

**Concepts Covered:**
- Model Context Protocol (MCP) — solving the N×M integration problem
- LangChain building blocks: Models, Prompt Templates, Chains (LCEL),
  Memory, Tools, Agents
- ReAct pattern (Reason + Act) — the foundation of practical agent implementations
- LangGraph — graph-based agent workflows with nodes, edges, and shared state
- Checkpointing, human-in-the-loop, streaming in LangGraph
- LangSmith — observability and debugging for LLM applications

**Coming Soon:** Assignment 3 implementation

---

## Week 4: Multi-Agent Workflows and Capstone Project *(Upcoming)*

Design and ship a fully autonomous multi-agent system where specialized agents
collaborate under an orchestration layer that routes tasks, manages state, and
handles failures.

**Coming Soon:** Capstone project

---

## Tech Stack

| Tool | Purpose |
|---|---|
| `anthropic` | Claude API (Week 1) |
| `sentence-transformers` | Text embeddings |
| `transformers` | flan-t5-base generation |
| `numpy` | Vector operations |
| `matplotlib` | Visualization |
| `re` | Text processing |
| Python 3.10+ | Core language |

---

## Key Learnings

- **RAG > Fine-Tuning** for frequently changing factual data. Fine-Tuning is for
  behavioural change, not knowledge updates.
- **Chunk size is a critical RAG decision** — too small loses context, too large
  wastes the context window.
- **Cosine similarity measures angle, not distance** — two vectors far apart in
  space can still be semantically identical.
- **LangGraph extends LangChain** with cycles and conditional branching —
  essential for non-linear agent workflows.
- **MCP collapses N×M integrations to N+M** — a universal protocol for
  connecting any model to any tool.
