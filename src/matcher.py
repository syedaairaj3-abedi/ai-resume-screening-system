from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_similarity_score(job_description, resume_text):

    embeddings = model.encode([job_description, resume_text])

    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]

    return score
