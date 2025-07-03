# 📁 Upload files
from google.colab import files
uploaded = files.upload()
print("\n📄 Uploaded Files:")
for file in uploaded:
    print(f"✅ {file}")

# 📚 Load and process documents
import os
from langchain.document_loaders import PyPDFLoader, TextLoader, UnstructuredWordDocumentLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

from langchain.vectorstores import FAISS

def load_documents(file_list):
    all_docs = []
    for file in file_list:
        try:
            if file.endswith(".pdf"):
                loader = PyPDFLoader(file)
            elif file.endswith(".txt"):
                loader = TextLoader(file)
            elif file.endswith(".docx"):
                loader = UnstructuredWordDocumentLoader(file)
            else:
                print(f"⛔ Unsupported file skipped: {file}")
                continue
            docs = loader.load()
            all_docs.extend(docs)
            print(f"✅ Loaded: {file}")
        except Exception as e:
            print(f"⚠️ Failed to load {file}: {e}")
    return all_docs

documents = load_documents(uploaded.keys())

# 🔀 Split & Embed
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_db = FAISS.from_documents(chunks, embedding_model)

print(f"\n🧠 Vector DB ready with {len(chunks)} chunks.")

# 💬 Interactive Q&A UI
import ipywidgets as widgets
from IPython.display import display, Markdown

query_input = widgets.Text(
    placeholder="📝 Type your medical question here...",
    layout=widgets.Layout(width="100%")
)
ask_button = widgets.Button(description="🔎 Ask", button_style='success')
output_box = widgets.Output()

def ask_question_callback(b):
    output_box.clear_output()
    query = query_input.value.strip()
    if not query:
        with output_box:
            display(Markdown("⚠️ **Please enter a question.**"))
        return

    results = vector_db.similarity_search(query, k=3)

    with output_box:
        display(Markdown(f"### ❓ **You asked:** {query}"))
        if not results:
            display(Markdown("❌ No results found."))
        else:
            display(Markdown("### 📄 **Top Relevant Passages:**"))
            for i, doc in enumerate(results):
                display(Markdown(f"**{i+1}.** {doc.page_content.strip()}"))
ask_button.on_click(ask_question_callback)
display(query_input, ask_button, output_box)
