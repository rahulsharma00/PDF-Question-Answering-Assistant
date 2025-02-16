# PDF-Question-Answering-Assistant
This project is a PDF Question Answering Assistant that utilizes OpenAI's API, Gradio, and a Postgres-backed Vector Database. It allows users to input a PDF URL and ask questions about its content, leveraging vector search to provide accurate answers.

## Features
- Extracts knowledge from a PDF using its URL.
- Utilizes vector search with PgVector2 for efficient information retrieval.
- Stores chat history in a Postgres database.
- Provides a user-friendly web interface using Gradio.
- Integrates with OpenAI's API for natural language processing.


## Setup

### 1. Run PgVector with Docker

```bash
docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  phidata/pgvector:16
```

This sets up a PostgreSQL instance with the `pgvector` extension on port `5532`.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` File:**
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

---

## Usage

### 1. Start the Gradio Interface
```bash
python main.py
```

### 2. Access the App
Open your browser and go to: [http://127.0.0.1:7860](http://127.0.0.1:7860)  

You can:
- Enter a PDF URL
- Ask questions about the PDF content

---

## Key Features

- Extracts knowledge from a PDF URL using `PDFUrlKnowledgeBase`
- Stores and retrieves conversation history with `PgAssistantStorage`
- Uses `PgVector` for vector-based knowledge search
- Gradio interface for user interaction

---

## Configuration

- **Database URL:** 
  ```python
  db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
  ```
- **Environment Variable:**
  ```env
  OPENAI_API_KEY=your_openai_api_key
  ```

---
