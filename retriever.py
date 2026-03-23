import os

def retrieve_context(query: str) -> str:
    try:
        BASE_DIR = os.path.dirname(__file__)
        file_path = os.path.join(BASE_DIR, "dsa_patterns_knowledge_base.txt")

        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    except Exception as e:
        return f"Error loading knowledge base: {e}"