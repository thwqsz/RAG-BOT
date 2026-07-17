from embeddings import get_embedding
from store import query_chunks


def retrieve_relevant_chunks(question: str, top_k: int = 5) -> list[str]:
    """
    Берёт вопрос пользователя, превращает в вектор,
    ищет топ-k похожих чанков в базе.
    """
    question_embedding = get_embedding(question)
    chunks = query_chunks(question_embedding, top_k=top_k)
    return chunks

if __name__ == "__main__":
    result = retrieve_relevant_chunks("Расскажи про кодинг", top_k=1)
    print(result)