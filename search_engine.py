import faiss
import numpy as np
import os
import json

INDEX_PATH = "index/faiss.index"
META_PATH  = "index/metadata.json"
DIM = 512

def load_or_create_index():
    if os.path.exists(INDEX_PATH):
        index = faiss.read_index(INDEX_PATH)
        with open(META_PATH) as f:
            metadata = json.load(f)
    else:
        index = faiss.IndexFlatIP(DIM)
        metadata = []
    return index, metadata

def add_image(embedding, image_path):
    index, metadata = load_or_create_index()
    index.add(embedding)
    metadata.append(image_path)
    faiss.write_index(index, INDEX_PATH)
    with open(META_PATH, "w") as f:
        json.dump(metadata, f)

def search(query_embedding, top_k=5, min_score=0.18):
    index, metadata = load_or_create_index()
    if index.ntotal == 0:
        return []
    scores, indices = index.search(query_embedding, min(top_k, index.ntotal))
    results = []
    for score, idx in zip(scores[0], indices[0]):
        if idx != -1 and score >= min_score:
            # Rescale CLIP's raw score (~0.15 to ~0.35) into a more intuitive 0-100% range
            display_score = min(max((score - 0.15) / (0.35 - 0.15), 0), 1)
            results.append({
                "path": metadata[idx],
                "score": float(score),          # raw CLIP score (for sorting/debugging)
                "display_score": float(display_score)  # rescaled, for showing to user
            })
    return results