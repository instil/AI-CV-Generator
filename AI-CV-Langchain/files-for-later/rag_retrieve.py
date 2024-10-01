from langchain.chains import RetrievalQA
from policy_to_convert import policy

def add_rag_embeddings_to_context(llm, retriever):
    # QA_train = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

    # # Use the RAG system to enhance the response
    # enhanced_response = QA_train({"query": policy})
    # return f"{policy}\n\nAdditional context: {enhanced_response['result']}"
    return policy