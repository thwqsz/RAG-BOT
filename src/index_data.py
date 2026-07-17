import os
from pypdf import PdfReader
from chunking import chunk_text
from embeddings import get_embedding
from store import add_chunks

DATA_DIR = "../data"


def read_file(filepath: str) -> str:
    """Читает текст из .md или .pdf файла."""
    if filepath.endswith(".pdf"):
        reader = PdfReader(filepath)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    else:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()


def index_all_files():
    all_chunks = []

    for filename in os.listdir(DATA_DIR):
        if not (filename.endswith(".md") or filename.endswith(".pdf")):
            continue

        filepath = os.path.join(DATA_DIR, filename)
        text = read_file(filepath)

        chunks = chunk_text(text, chunk_size=300, overlap=50)
        print(f"{filename}: получилось {len(chunks)} чанков")
        all_chunks.extend(chunks)

    print("Считаю эмбеддинги...")
    embeddings = [get_embedding(chunk) for chunk in all_chunks]

    print("Кладу в базу...")
    add_chunks(all_chunks, embeddings)

    print(f"Готово. Проиндексировано {len(all_chunks)} чанков.")


if __name__ == "__main__":
    index_all_files()