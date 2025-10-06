# Conversational AI Example for dspy

This project demonstrates simple usage of the `dspy` library with different language models for text-based conversation.

## Dependencies

- Python 3.13+
- [dspy](https://pypi.org/project/dspy/) >= 3.0.3
- [python-dotenv](https://pypi.org/project/python-dotenv/) (for loading API keys from `.env`)

You will also need API keys for a model here are some potentially free options:
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

2. Create a `.env` file in the project directory with your API keys:
    ```
    google_ai_studio_key=YOUR_GOOGLE_AI_STUDIO_KEY
    open_router_key=YOUR_OPENROUTER_KEY
    ```

3. Run the script:
    ```bash
    python conversational_ai.py
    ```

## What it does

- Prompts the user for input in a loop.
- Sends the input to a language model (Longcat via OpenRouter) to generate a response.
- Prints the model's response.
- Includes utility functions for summarization and explanation using different models.