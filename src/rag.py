import ollama
from retrieval import retrieve_relevant_chunks


def answer_question(question: str, top_k: int = 3) -> str:
    """
    Полный цикл: находит релевантные чанки, собирает промпт,
    отправляет в LLM, возвращает ответ.
    """

    # 1. Находим релевантные куски текста
    chunks = retrieve_relevant_chunks(question, top_k=top_k)

    print("=== НАЙДЕННЫЕ ЧАНКИ ===")
    for i, c in enumerate(chunks):
        print(f"[{i}] {c[:200]}")
    print("=======================")

    # 2. Склеиваем их в один блок контекста
    context = "\n\n".join(chunks)


    # 3. Собираем промпт: инструкция + контекст + вопрос
    prompt = f"""Ответь на вопрос, используя ТОЛЬКО информацию из контекста ниже.
Если в контексте нет ответа — так и скажи, не придумывай.

Контекст:
{context}

Вопрос: {question}

Ответ:"""

    # 4. Отправляем в локальную LLM через Ollama
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]

if __name__ == "__main__":
    answer = answer_question("Расскажи про животных")
    print(answer)