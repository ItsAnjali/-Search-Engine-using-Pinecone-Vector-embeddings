# rag_pipeline.py

# import your libraries (HuggingFace, Pinecone, etc.)
from sentence_transformers import SentenceTransformer
import pinecone

# init your model + pinecone connection here
model = SentenceTransformer("all-MiniLM-L6-v2")
pc = pinecone.Pinecone(api_key="pcsk_VM5Mr_Rj2DSWHQtifPXCTWUrfDMg436KtvaFvsnpW4AzRywe3BMDtLeqX35BCQG3KguP2")
index = pc.Index("bhagavad-gita-hybrid")

def ask_gita(question: str) -> str:
    # 1. embed the question
    embedding = model.encode(question).tolist()

    # 2. query pinecone
    res = index.query(vector=embedding, top_k=3, include_metadata=True)

    # 3. build an answer from the results
    if res and res.matches:
        return res.matches[0].metadata["text"]
    else:
        return "Sorry, I could not find an answer."
