import streamlit as st
import tempfile
from main import load_pdf, build_qa_chain
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="PDF QnA", page_icon="📕", layout="wide")
st.title("PDF QnA App")
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    with st.spinner("Processing PDF..."):
        with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name
        
        chunk = load_pdf(temp_file_path)
        qa_chain = build_qa_chain(chunk)
        st.success("PDF processed successfully! Ask your question below")

    query = st.text_input("Ask a question about the PDF:")
    if query:
        with st.spinner("Fetching answer.."):
            response=qa_chain({"query": query})
            st.subheader("💬 Answer")
            st.write(response["result"])
            with st.expander("📚 Source Chunks"):
                    for i, doc in enumerate(response["source_documents"]):
                        st.markdown(f"**Chunk {i+1}:**")
                        st.write(doc.page_content[:500])

