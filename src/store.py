import chromadb

# Создаём клиент, который хранит базу прямо на диске в папке ./chroma_data
client = chromadb.PersistentClient(path="./chroma_data")

# Коллекция — это как таблица в обычной БД, отдельное пространство для наших чанков
collection = client.get_or_create_collection(name="documents")


def add_chunks(chunks: list[str], embeddings: list[list[float]]):
    """
    Кладёт чанки текста и их вектора в базу.
    Каждому чанку нужен уникальный id — просто нумеруем по порядку.
    """
    ids = [str(i) for i in range(len(chunks))]
    collection.add(
        ids=ids,
        documents=chunks,      # сам текст чанка (chromadb хранит и его тоже)
        embeddings=embeddings  # вектор чанка
    )


def query_chunks(query_embedding: list[float], top_k: int = 5) -> list[str]:
    """
    Ищет top_k самых похожих чанков на вектор вопроса.
    """
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    return results["documents"][0]

if __name__ == "__main__":
    from embeddings import get_embedding

    test_chunks = ["Кошки любят спать", "Собаки любят бегать", "Питон — язык программирования"]
    test_embeddings = [get_embedding(c) for c in test_chunks]
    add_chunks(test_chunks, test_embeddings)

    question_embedding = get_embedding("Расскажи про животных")
    found = query_chunks(question_embedding, top_k=2)
    print(found)