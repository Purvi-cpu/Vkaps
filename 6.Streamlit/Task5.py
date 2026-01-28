import streamlit as st
import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
from docx import Document
from PyPDF2 import PdfReader
from pinecone import Pinecone

load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = "semantic-search-384"

pc = Pinecone(api_key=PINECONE_API_KEY)

if "indexed" not in st.session_state:
    st.session_state.indexed = False

if "model" not in st.session_state:
    st.session_state.model = SentenceTransformer("all-MiniLM-L6-v2")

if not pc.has_index(INDEX_NAME):
    pc.create_index(
        name=INDEX_NAME,
        dimension=384,
        metric="cosine",
        spec={
            "serverless": {
                "cloud": "aws",
                "region": "us-east-1"
            }
        }
    )

index = pc.Index(INDEX_NAME)


def load_pdf(file):
    reader = PdfReader(file)
    return "".join(page.extract_text() or "" for page in reader.pages)

def load_docx(file):
    doc = Document(file)
    return "\n".join(p.text for p in doc.paragraphs)


st.title("Document RAG App")

uploaded_files = st.sidebar.file_uploader(
    "Upload PDF / DOCX",
    type=["pdf", "docx"],
    accept_multiple_files=True
)


if uploaded_files and not st.session_state.indexed:
    with st.spinner("Processing & indexing documents..."):
        text = ""
        for file in uploaded_files:
            if file.name.endswith(".pdf"):
                text += load_pdf(file)
            else:
                text += load_docx(file)

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = splitter.split_text(text)

        embeddings = st.session_state.model.encode(chunks).tolist()

        vectors = [
            (str(i), embeddings[i], {"text": chunks[i]})
            for i in range(len(chunks))
        ]

        index.upsert(vectors=vectors)
        st.session_state.indexed = True

    st.success("Documents indexed successfully!")

# ------------------ QUERY ------------------
query = st.text_input("Ask a question from the document")

if query and st.session_state.indexed:
    query_embedding = st.session_state.model.encode(query).tolist()

    results = index.query(
        vector=query_embedding,
        top_k=1,
        include_metadata=True
    )

    st.subheader(" Retrieved Context")
    for match in results["matches"]:
        st.write(match["metadata"]["text"])
