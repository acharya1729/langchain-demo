# app/utils.py
import os
import json
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
