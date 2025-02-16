import typer
from rich.prompt import Prompt
from typing import Optional, List
from phi.assistant import Assistant
from phi.storage.assistant.postgres import PgAssistantStorage
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector2
import gradio as gr
import os
from dotenv import load_dotenv

load_dotenv()

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def create_assistant(pdf_url: str, user: str = "user"):
    knowledge_base = PDFUrlKnowledgeBase(
        urls=[pdf_url],
        vector_db=PgVector2(collection="recipes", db_url=db_url),
    )
    # Comment out after first run
    knowledge_base.load()

    storage = PgAssistantStorage(table_name="pdf_assistant", db_url=db_url)

    assistant = Assistant(
        user_id=user,
        knowledge_base=knowledge_base,
        storage=storage,
        show_tool_calls=True,
        search_knowledge=True,
        read_chat_history=True,
    )

    return assistant

def ask_question(pdf_url: str, question: str):
    assistant = create_assistant(pdf_url)
    
    # Consume the generator and collect the response
    response_generator = assistant.run(question)
    response = "".join([chunk for chunk in response_generator])
    
    return response

iface = gr.Interface(
    fn=ask_question,
    inputs=[
        gr.Textbox(label="PDF URL"),
        gr.Textbox(label="Question")
    ],
    outputs=gr.Textbox(label="Answer"),
    title="PDF Question Answering",
    description="Upload a PDF URL and ask questions about its content."
)

if __name__ == "__main__":
    iface.launch()