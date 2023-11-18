# app/langchain_init.py
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain import hub
from chromadb.utils import embedding_functions
from langchain.schema import StrOutputParser

rag_prompt = hub.pull("rlm/rag-prompt")

# Initialize Langchain components
document_loader = WebBaseLoader("https://compliancereportszania.blob.core.windows.net/soc2-reports/safebase-short.json")

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

openai_embeddings = OpenAIEmbeddings(openai_api_key="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")

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0,
                 openai_api_key="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")


def format_docs(document):
    return "\n\n".join(doc.page_content for doc in document)
