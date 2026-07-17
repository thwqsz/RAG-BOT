def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    """
    Разбивает текст на куски (чанки) фиксированного размера в словах,
    с перехлёстом между соседними чанками.

    chunk_size — сколько слов в одном чанке
    overlap — сколько слов повторяется в начале следующего чанка
    """
    words = text.split()  # разбиваем весь текст на список слов
    chunks = []

    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk_words = words[start:end]  # берём срез слов для одного чанка
        chunk = " ".join(chunk_words)   # склеиваем обратно в текст
        chunks.append(chunk)

        start += chunk_size - overlap  # сдвигаемся вперёд, но с учётом перехлёста

    return chunks

if __name__ == "__main__":
    sample_text = "слово " * 1200  # имитация длинного текста
    result = chunk_text(sample_text)
    print(f"Получилось чанков: {len(result)}")
    print(f"Длина первого чанка (слов): {len(result[2].split())}")