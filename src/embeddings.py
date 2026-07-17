from sentence_transformers import SentenceTransformer

# Загружаем модель один раз при импорте файла, а не при каждом вызове функции —
# иначе каждый раз будет заново грузиться с диска
model = SentenceTransformer('all-MiniLM-L6-v2')


def get_embedding(text: str) -> list[float]:
    """
    Превращает текст в вектор (список из 384 чисел).
    Похожие по смыслу тексты дадут похожие вектора.
    """
    embedding = model.encode(text)
    return embedding.tolist()

if __name__ == "__main__":
    vector = get_embedding("Привет, как дела?")
    print(f"Длина вектора: {len(vector)}")
    print(f"Первые 5 чисел: {vector[:5]}")