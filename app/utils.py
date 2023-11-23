# app/utils.py
import os
import json
from langchain.document_loaders import JSONLoader, PyPDFLoader, UnstructuredPDFLoader

from fastapi import UploadFile

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def save_uploaded_files(document_file, questions_file):
    # Save the uploaded document file
    document_file_path = os.path.join(UPLOAD_DIR, document_file.filename)
    with open(document_file_path, 'wb') as f:
        f.write(document_file.file.read())

    # Save the uploaded questions JSON file
    questions_file_path = os.path.join(UPLOAD_DIR, questions_file.filename)
    with open(questions_file_path, 'wb') as f:
        f.write(questions_file.file.read())

    return document_file_path, questions_file_path


def load_questions(questions_file_path):
    with open(questions_file_path, 'r') as json_file:
        return json.load(json_file)


def load_document(document_file_path):
    if document_file_path.endswith('.json'):
        # Load JSON file
        data = JSONLoader(document_file_path, jq_schema='.',text_content=False)
        return data.load()
    elif document_file_path.endswith('.pdf'):
        # Load PDF file
        loader = PyPDFLoader(document_file_path)
        return loader.load()

    else:
        raise ValueError("Unsupported file format. Only JSON and PDF files are supported.")
