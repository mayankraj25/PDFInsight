from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
load_dotenv()

def load_pdf(file_path):
    loader=PyPDFLoader(file_path)
    documents=loader.load()
    print(f"Total number of documents loaded: {len(documents)}")
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunk=text_splitter.split_documents(documents)
    return chunk

def build_qa_chain(chunk):
    embeddings=OpenAIEmbeddings()
    vector_store=FAISS.from_documents(chunk,embeddings)
    retriever=vector_store.as_retriever()
    qa_chain=RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model_name="gpt-4o-mini",temperature=0.2),
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain


