# Website Summarizer ✨📄🌍

## Overview 🚀📝🌐

Website Summarizer is a Streamlit-based web application that extracts and summarizes content from a given URL. The application also allows users to ask questions related to the website's content and receive AI-generated answers. It leverages LangChain, FAISS for efficient text retrieval, and LLaMA-based LLM from Groq for summarization and Q&A capabilities. 🤖📊🗂️

## Features 🎯⚡📌

- Extracts content from a provided URL
- Splits text into smaller chunks for efficient processing
- Generates text embeddings using Hugging Face models
- Stores embeddings in FAISS for efficient retrieval
- Summarizes extracted content using an LLM
- Allows users to ask questions about the extracted content

## Technologies Used 🛠️📡🔍

- **Python** for backend logic
- **Streamlit** for UI
- **LangChain** for text processing and retrieval
- **FAISS** for vector-based search
- **Hugging Face Embeddings** for text vectorization
- **Groq API (LLaMA model)** for summarization and Q&A
- **Unstructured.io** for web scraping
- **Pickle** for storing FAISS data

## Installation ⚙️🖥️📥

### Prerequisites 🎓📌✅

Ensure you have Python 3.8 or later installed on your system.

### Steps 🚀📜🛠️

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/website-summarizer.git
   cd website-summarizer
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Create a `.env` file in the project directory.
   - Add the following line:
     ```bash
     GROQ_API_KEY=your_api_key_here
     ```

## Usage 💻📊📜

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Enter the website URL in the sidebar and click "Submit" to extract and summarize content.
3. Ask questions related to the content in the text input field.

## Project Structure 🏗️📂📌

```
website-summarizer/
│── app.py                 # Main application file
│── requirements.txt       # Dependencies
│── .env                   # Environment variables (not included in repo)
└── README.md              # Project documentation
```

## Known Issues & Limitations 🚧⚠️🔍

- Some websites may block scraping, preventing content extraction.
- Summarization quality depends on the extracted text and model capabilities.
- Performance may vary for large documents.

## Future Enhancements 🚀🔮📈

- Add support for multiple URLs at once
- Improve error handling for inaccessible websites
- Enhance summarization by fine-tuning the LLM
- Integrate caching for faster responses

