import os
from cryptography.fernet import Fernet
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

def load_api_key():
    
    key_path = "./secret.key"
    encrypted_key_path = "./encrypted_api_key.txt"
    
    # Load the encryption key
    with open("secret.key", "rb") as key_file:
        key = key_file.read()

    # Initialize the Fernet instance
    cipher_suite = Fernet(key)

    # Load and decrypt the API key
    with open("encrypted_api_key.txt", "rb") as encrypted_file:
        encrypted_api_key = encrypted_file.read()

    decrypted_api_key = cipher_suite.decrypt(encrypted_api_key).decode()
    return decrypted_api_key

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = load_api_key()

# Define paths
pdf_path = "./docs/TESLALLCUS.pdf"

# Load documents
loader = PyMuPDFLoader(pdf_path)
documents = loader.load()

# Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=10)
texts = text_splitter.split_documents(documents)

# Create embeddings
embeddings = OpenAIEmbeddings()

# Create Chroma vector store (automatic persistence)
vectordb = Chroma.from_documents(documents=texts, embedding=embeddings)

# Create retriever
retriever = vectordb.as_retriever(search_kwargs={"k": 3})

# Initialize ChatOpenAI model
llm = ChatOpenAI(model_name='gpt-4o')

# Create RetrievalQA chain
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

# Main loop to process user queries
while True:
    user_input = input("Enter a query: ")
    if user_input.lower() == "exit":
        break

    query = f"###Prompt {user_input}"
    try:
        llm_response = qa.invoke(query)  # Use invoke instead of __call__
        print(llm_response["result"])
    except Exception as err:
        print('Exception occurred. Please try again', str(err))
