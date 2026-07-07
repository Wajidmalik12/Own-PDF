# Own-PDF

# 📄 PDF ChatBot with RAG

A Retrieval-Augmented Generation (RAG) application that allows users to upload their own PDF documents and ask natural language questions. The application retrieves the most relevant document chunks using semantic search and generates context-aware answers with Groq's Llama 3.3 model.

## 🚀 Features

* Upload your own PDF documents
* Automatic text cleaning and preprocessing
* Intelligent text chunking
* Semantic search using Hugging Face embeddings
* Fast vector retrieval with ChromaDB
* Context-aware responses powered by Groq Llama 3.3
* Simple and interactive Gradio interface

## 🛠️ Tech Stack

* Python
* LangChain
* ChromaDB
* Hugging Face Embeddings (`all-MiniLM-L6-v2`)
* Groq API
* Llama 3.3 70B Versatile
* Gradio

## 📂 Project Structure

```text
├── app.py
├── rag.py
├── requirements.txt
└── README.md
```
## 🔑 Environment Variable

Create a `.env` file for local development:

```text
GROQ_API_KEY=your_groq_api_key
```

For Hugging Face Spaces, add the API key under **Settings → Repository Secrets** with the name:

```text
GROQ_API_KEY
```

## ▶️ Run the Application

```bash
python app.py
```

The Gradio interface will launch locally, allowing you to upload a PDF and begin asking questions.

## 📖 How It Works

1. Upload a PDF document.
2. The document is cleaned and split into overlapping chunks.
3. Hugging Face embeddings convert each chunk into vector representations.
4. ChromaDB stores the vectors for semantic retrieval.
5. The user's question retrieves the most relevant chunks.
6. The retrieved context is sent to Groq's Llama 3.3 model.
7. The model generates an answer based only on the retrieved document content.

## 📌 Future Improvements

* Multiple PDF support
* Persistent vector database
* Conversation memory
* Source page citations
* Streaming responses
* Hybrid search (keyword + semantic search)

## 👨‍💻 Author

**Abdul Wajid Malik**


