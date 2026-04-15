# RAG-Based Hybrid Search Engine

A hybrid search system that combines semantic search (Pinecone embeddings) with BM25 keyword search to improve answer relevance.

## Features
- Hybrid retrieval: semantic + lexical (BM25)
- Context-aware Q&A system
- FastAPI backend with React frontend
- Document ingestion and chunking pipeline

## Tech Stack
- FastAPI, React
- Pinecone (Vector DB)
- BM25
- RAG pipeline
- Python

## How It Works
1. Documents are ingested and split into chunks  
2. Embeddings are generated and stored in Pinecone  
3. Query runs through both semantic search and BM25  
4. Results are combined and used to generate answers  

## Highlights
- ~35% improvement in answer relevance  
- Handles concurrent requests efficiently  
- Designed for scalable AI-based search systems  

## Setup
```bash
git clone <repo-link>
cd backend && pip install -r requirements.txt
uvicorn main:app --reload
