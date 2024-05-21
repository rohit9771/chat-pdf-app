Here's a README.md content based on the provided code:

---

# PDF Chat Application

This Python application enables users to interact with a chatbot trained on a specific topic using PDF documents as a knowledge source. The chatbot leverages AI models provided by OpenAI for natural language understanding and generation.

## Installation

To run this application, you'll need Python installed on your system. Follow these steps to set up the environment:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/rohit9771/chat-pdf-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd chat-pdf-app
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the PDF Chat Application, follow these steps:

1. Ensure that your PDF documents are located in the `./docs/` directory.
2. Encrypt your OpenAI API key and store it in the `./encrypted_api_key.txt` file. You can use the provided `encrypt_api_key.py` script for this purpose.
3. Run the `handler.py` script:

    ```bash
    python handler.py
    ```

4. Enter a query when prompted and interact with the chatbot.

## Configuration

Before running the application, you need to configure your OpenAI API key. Follow these steps to encrypt and store your API key:

1. Create a `secret.key` file in the project directory.
2. Run the `encrypt_api_key.py` script to encrypt your API key:

    ```bash
    python encrypt_api_key.py
    ```

3. Ensure that the encrypted API key is stored in the `./encrypted_api_key.txt` file.

## Dependencies

- [cryptography](https://pypi.org/project/cryptography/): Used for encryption and decryption operations.
- [langchain](https://pypi.org/project/langchain/): A library providing various natural language processing functionalities.
- [PyMuPDF](https://pypi.org/project/PyMuPDF/): Required for loading PDF documents and extracting text.
- [tiktoken](https://pypi.org/project/tiktoken/): A library for tokenization.
- [langchain-community](https://pypi.org/project/langchain-community/): Community-contributed modules for langchain.
- [chromadb](https://pypi.org/project/chromadb/): A vector store for text documents.
- [langchain-openai](https://pypi.org/project/langchain-openai/): Provides integration with OpenAI for embeddings and chat models.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

---

This README.md provides an overview of the PDF Chat Application, including installation instructions, usage guidelines, configuration steps, dependency information, and guidelines for contributing to the project. It should help users understand how to set up and use the application effectively.