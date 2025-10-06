# Some Examples for dspy

This project demonstrates simple usage of the `dspy` library with different language models for creating text embeddings for vectorization or possible semantics based classification.

## Dependencies

- Python 3.13+
- [dspy](https://pypi.org/project/dspy/) >= 3.0.3
- [python-dotenv](https://pypi.org/project/python-dotenv/) (for loading API keys from `.env`)

You will also need API keys for:
- Google AI Studio (for Gemini models)
- OpenRouter (for Longcat model)

## Running the script

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    or
    ```bash
    pip install dspy>=3.0.3 python-dotenv
    ```
    Ollama is an optional dependency, as I have an extra machine running a local embedding model. The example in `embedder.py` does use ollama for an embedder.

2. Create a `.env` file in the project directory with your API keys:
    ```
    google_ai_studio_key=YOUR_GOOGLE_AI_STUDIO_KEY
    open_router_key=YOUR_OPENROUTER_KEY
    ```

3. Run the script:
    ```bash
    python conversational_ai/conversational_ai.py
    ```

## What it does

- Takes any string or array of strings and returns vectorized embeddings of text.