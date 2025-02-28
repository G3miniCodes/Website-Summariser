import os
import streamlit as st
import pickle
import time
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.2-11b-vision-preview")

# Streamlit UI
st.title("The Website Summariser")
st.subheader("Please enter the URL in the sidebar and click on submit to get your summarized content.\n You can even ask questions related to the websites content and get your answers.")
st.sidebar.title("Enter your URL")

# User input for URL
urls = st.sidebar.text_input("Enter your URL: ")
clicked = st.sidebar.button("Submit")

show_text = st.empty()

file_path = "FAISS_data.pkl"  # Path for storing FAISS index

if clicked:
    if not urls.strip():
        st.error("Please enter a valid URL!")
        st.stop()
    
    show_text.subheader("Loading data from URL... ⏳")
    loader = UnstructuredURLLoader(urls=[urls])  # Fix: Pass URL as a list
    data = loader.load()
    
    if not data:
        st.error("No content was extracted from the URL. Please check the URL and try again.")
        st.stop()

    show_text.subheader("Splitting text... 📄")
    splitter = RecursiveCharacterTextSplitter(separators=['\n\n', '\n', '.'], chunk_size=500)
    doc = splitter.split_documents(data)

    if not doc:
        st.error("No valid text was extracted after splitting. Try another URL.")
        st.stop()

    show_text.subheader("Generating embeddings... 🧠")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # doc_texts = [d.page_content for d in doc if d.page_content.strip()]
    doc_texts =FAISS.from_documents(doc, embeddings) 
    if not doc_texts:
        st.error("No valid text found for embeddings. Try a different URL.")
        st.stop()

    # faiss_load = FAISS.from_texts(doc_texts, embeddings)

    show_text.subheader("Storing FAISS data... 📂")
    with open(file_path, "wb") as f:
        pickle.dump(doc_texts, f)

    time.sleep(2)

    # Summarize content
    def split_text(documents, chunk_size=5000):
        full_text = " ".join([doc.page_content for doc in documents])  # Extract text
        words = full_text.split()  # Now split properly
        return [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

    chunks = split_text(data, chunk_size=5000)


    summaries = []
    for chunk in chunks:
        summary_prompt = f"Summarize the following content:\n\n{chunk}"
        summary = llm.invoke(summary_prompt)
        summaries.append(summary.content)

    final_summary = " ".join(summaries)  # Combine chunked summaries
    st.header("Website Summary 📃")
    st.write(final_summary)
# Query input for Q&A
query = st.text_input("Ask a question about the content...")

if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            faiss_data = pickle.load(f)
        
        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=faiss_data.as_retriever())
        result = chain({"question": query}, return_only_outputs=True)

        st.header("Answer 🧐")
        st.write(result["answer"])
    else:
        st.error("No FAISS data found. Please enter a URL and submit first.")
