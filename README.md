# Langchain demo: Question-Answering Bot

## Introduction

This project implements a backend API for a Question-Answering bot using the Langchain framework. The bot leverages the capabilities of the OpenAI GPT-3.5-turbo model to answer questions based on the content of a document. The API supports input in JSON and PDF formats and provides structured JSON output pairing each question with its corresponding answer.

## Technologies Used

- **Python 3.x:** The programming language used for the backend development.
- **Langchain (Python):** Langchain framework for implementing the Question-Answering functionality.
- **OpenAI (gpt-3.5-turbo model):** Utilized for generating answers to the questions.
- **VectorDB:** Used for storing and retrieving vector embeddings.
- **FastAPI:** The web framework chosen to build the API.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/acharya1729/langchain-demo.git
    cd langchain-demo
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the FastAPI Application:**

    ```bash
    uvicorn app.main:app --reload
    ```

    This will start the FastAPI application on `http://127.0.0.1:8000`. Visit this URL in your browser or use a tool like `curl` for API requests.

2. **API Endpoints:**

    - **Question Answering:**
        - Endpoint: `http://127.0.0.1:8000/qa/`
        - Method: `POST`
        - Request:
            - Upload a PDF document file and a JSON file containing questions.
            - Example using `curl`:
                ```bash
                curl -X POST -F "document_file=@/path/to/document.pdf" -F "questions_file=@/path/to/questions.json" http://127.0.0.1:8000/qa/
                ```

## Project Structure

- **app/**
  - **__init__.py:** Initialization file for the `app` package.
  - **main.py:** Script to run the FastAPI application.
  - **utils.py:** Utility functions for file handling.
  - **langchain_init.py:** Initialization of Langchain components.
  - **fastapi_app.py:** FastAPI application and endpoint logic.
  - **tests/**
    - **__init__.py:** Initialization file for the `tests` package.
    - **test_main.py:** Tests for the main application logic.
  
- **requirements.txt:** List of project dependencies.
- **README.md:** Project documentation.

## Configuration

- **Langchain Configuration:**
    - The Langchain components are initialized in `langchain_init.py`.

- **FastAPI Configuration:**
    - FastAPI settings, endpoints, and logic are in `fastapi_app.py`. 

## Testing

- Run tests using your preferred test runner. For example, with `pytest`:

    ```bash
    pip install pytest
    pytest
    ```