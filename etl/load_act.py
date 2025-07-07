
# etl/load_act.py  – minimal demo
import fitz, json, pathlib, tiktoken, os
from pymongo import MongoClient
from vertexai.preview.language_models import TextEmbeddingModel

PDF = "eu_ai_act_official.pdf"
enc = tiktoken.get_encoding("cl100k_base")
chunks = []
with fitz.open(PDF) as doc:
    text = " ".join(page.get_text() for page in doc)
    words = text.split()
    for i in range(0, len(words), 120):            # ~500-token chunks
        chunk = " ".join(words[i:i+120])
        chunks.append(chunk)

model = TextEmbeddingModel.from_pretrained("textembedding-gecko@003")
embeds = model.get_embeddings(chunks)

mc = MongoClient(os.getenv("MONGO_URI"))
col = mc.copilot.regulation_chunks
for t,e in zip(chunks, embeds):
    col.insert_one({"text": t, "embedding": e.values})

