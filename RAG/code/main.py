from langchain.vectorstores import qdrant
import qdrant_client
import os
import openai
from langchain_qdrant import QdrantVectorStore
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain.retrievers.document_compressors import FlashrankRerank
from langchain.retrievers import ContextualCompressionRetriever
from common.utils import getapi
def initialize_qdrant():
    # Create the embeddings inside the function
    embeddings = FastEmbedEmbeddings(model_name="BAAI/bge-base-en-v1.5")
    
    qdrant = QdrantVectorStore.from_existing_collection(
        collection_name="document_embeddings",
        url="https://32591c00-f7c7-4a0a-a2c1-4d55831b1795.us-west-1-0.aws.cloud.qdrant.io",
        api_key="40rd2sm16-_L2A5PWJI5wFZTU--TyKKCCEgfQYto7LbVAWwBdr9fcw",
        embedding=embeddings  # Pass the embeddings here
    )
    return qdrant


def rerank_documents(query,compression_retriever):

    reranked_docs = compression_retriever.invoke(query, num_docs=2)  # Adjusting to return only 2 documents
    reranked_docs = reranked_docs[:2]  

    return reranked_docs


def get_answer_from_openai(question, context):
    # Generate an answer from OpenAI using the retrieved context
    prompt = f"Answer the question based on the context below:\n\nContext: {context}\n\nQuestion: {question}\nAnswer:"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or any other model you want to use
        messages=[{"role": "user", "content": prompt}]
    )
    
    answer = response['choices'][0]['message']['content']
    return answer


def answer_question(query):
    # Initialize Qdrant
    qdrant = initialize_qdrant()
    retriever = qdrant.as_retriever(search_kwargs={"k": 5})
    compressor = FlashrankRerank(model="ms-marco-MiniLM-L-12-v2")
    compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor, base_retriever=retriever
    )

    # Rerank documents based on the query
    documents = rerank_documents(query,compression_retriever)

    # Extract the context from the retrieved documents
    context = "\n".join([doc.page_content for doc in documents])  # Adjust according to your document structure
    
    # Get answer from OpenAI
    answer = get_answer_from_openai(query, context)
    
    return answer

openai.api_key = getapi()

def main(query):
    answer = answer_question(query)
    return answer

# Example usage
if __name__ == "__main__":
    query = "What is the phone number of Santwana ma'am?"
    answer = main(query)
    print(answer)