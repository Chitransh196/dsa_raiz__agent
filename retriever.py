# # import os

# # def retrieve_context(query: str) -> str:
# #     try:
# #         BASE_DIR = os.path.dirname(__file__)
# #         file_path = os.path.join(BASE_DIR, "dsa_patterns_knowledge_base.txt")

# #         with open(file_path, "r", encoding="utf-8") as f:
# #             return f.read()

# #     except Exception as e:
# #         return f"Error loading knowledge base: {e}"

# # import os


# # def retrieve_context(query: str) -> str:
# #     try:
# #         # 🔍 Get absolute directory of this file
# #         BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# #         # 📂 Build full file path
# #         file_path = os.path.join(BASE_DIR, "dsa_patterns_knowledge_base.txt")

# #         # 🧪 Debug logs (helps in deployment)
# #         print("BASE_DIR:", BASE_DIR)
# #         print("Looking for file at:", file_path)

# #         # ❌ If file missing
# #         if not os.path.exists(file_path):
# #             return "⚠️ Knowledge base file not found. Make sure 'dsa_patterns_knowledge_base.txt' is in the same folder."

# #         # ✅ Read file
# #         with open(file_path, "r", encoding="utf-8") as f:
# #             content = f.read()

# #         # ❗ Optional: return partial content (avoid huge prompts)
# #         return content[:3000]

# #     except Exception as e:
# #         return f"❌ Error loading knowledge base: {str(e)}"

# import os


# def retrieve_context(query: str) -> str:
#     try:
#         # 🔍 Debug: show current working directory
#         cwd = os.getcwd()
#         files = os.listdir(cwd)

#         print("CWD:", cwd)
#         print("FILES:", files)

#         file_path = os.path.join(cwd, "dsa_patterns_knowledge_base.txt")

#         if not os.path.exists(file_path):
#             return f"❌ File NOT found.\nCurrent dir: {cwd}\nFiles: {files}"

#         with open(file_path, "r", encoding="utf-8") as f:
#             return f.read()[:3000]

#     except Exception as e:
#         return f"❌ Error: {e}"
import os


def retrieve_context(query: str) -> str:
    try:
        # ✅ Always correct path (file-based)
        base_dir = os.path.dirname(os.path.abspath(__file__))

        file_path = os.path.join(base_dir, "dsa_patterns_knowledge_base.txt")

        print("BASE_DIR:", base_dir)
        print("FILES:", os.listdir(base_dir))

        if not os.path.exists(file_path):
            return f"❌ File NOT found in: {base_dir}"

        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()[:3000]

    except Exception as e:
        return f"❌ Error: {e}"