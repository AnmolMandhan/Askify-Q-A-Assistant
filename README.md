# 🔍 Askify Q&A Assistant (RAG + LangChain)

This project is a Retrieval-Augmented Generation (RAG) based chatbot built using **LangChain**, **FAISS**, and **Hugging Face embeddings**. It allows users to upload `.pdf`, `.docx`, or `.txt` files and ask natural language questions based on the uploaded content.

---

## 🚀 Features

- Upload multiple document formats (`.pdf`, `.txt`, `.docx`)
- Automatically chunks and indexes document content
- Embeds text using `MiniLM` from Hugging Face
- Searches semantically relevant content using FAISS
- Clean Q&A interface using `ipywidgets` in Colab
- No internet APIs, keys, or LLMs required

---

## 🔌 Internet Requirement

- ✅ **Colab Version** needs internet to:
  - Install Python packages
  - Download the embedding model once from Hugging Face

- ✅ **Local Version** can be made fully offline by:
  - Installing dependencies once
  - Caching the embedding model locally
  - Running via Jupyter or Streamlit

---

## 🧠 How It Works

1. Upload any text-based document
2. The text is split into chunks (~500 characters)
3. Each chunk is converted into a vector
4. Vectors are stored in FAISS (vector database)
5. Your question is embedded and matched to the most relevant chunks
6. The top results are displayed as answers

---

## 🧪 Example Use Cases

- 📚 Ask questions from textbooks
- 📄 Extract info from resumes or legal docs
- 🧾 Query research papers or business reports
- 🧠 Use as a private document search engine

---

## 💻 Running in Google Colab

1. Open the Colab notebook
2. Upload your documents
3. Type a question and get answers instantly

---

## 🖥 Running Locally (Offline)

### Requirements
```txt
langchain
langchain-huggingface
faiss-cpu
sentence-transformers
PyPDF2
unstructured
python-docx
ipywidgets



💼 Author

👤 Anmol Mandhan

💻 Django | Python | Frontend Developer | AI/ML

📎 LinkedIn Profile | www.linkedin.com/in/anmol-mandhan-6a80362a8


🌟 Give a Star!

If you like this project, don’t forget to ⭐ star it on GitHub!
