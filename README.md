# 📄 PDF QnA — Chat with Any PDF using LangChain and OpenAI
PDF QnA is a full-stack AI-powered application that lets you interact with the contents of a PDF document using natural language. Built using LangChain, OpenAI’s language models, and FAISS for vector search, this project combines powerful LLM-based retrieval with a user-friendly Streamlit interface for seamless PDF question-answering.

Whether you’re a student reviewing lecture slides, a researcher exploring academic papers, or a professional analyzing lengthy reports, PDF QnA allows you to ask questions and receive accurate answers—along with the exact chunks of text the answer came from.

⸻

🔧 Features
	•	PDF Ingestion: Upload any PDF and extract its content using PyPDFLoader.
	•	Intelligent Chunking: Documents are split into overlapping chunks using RecursiveCharacterTextSplitter to retain semantic context.
	•	Embeddings: Each chunk is embedded using OpenAI’s OpenAIEmbeddings.
	•	Vector Search: FAISS is used to store and search document vectors for relevant context during Q&A.
	•	Retrieval-Augmented QA: Uses RetrievalQA chain to answer user queries based on document context.
	•	Frontend UI: Built with Streamlit for a simple and interactive experience:
	•	Upload your own PDFs.
	•	Ask any question.
	•	Get the answer along with source chunks.

⸻

📚 Tech Stack
	•	LangChain — Framework for LLM-powered apps.
	•	OpenAI (GPT-4o-mini) — For question answering.
	•	FAISS — Efficient vector similarity search.
	•	Streamlit — Frontend for real-time interaction.
	•	Python-dotenv — Secure API key management.
	•	PyPDFLoader — PDF parsing and content extraction.

⸻

⚠️ Note: The .env file containing your OpenAI API key is not included in this repo. Make sure to create one locally to run the application.
