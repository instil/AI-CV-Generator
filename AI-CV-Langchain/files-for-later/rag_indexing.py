from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_aws import BedrockEmbeddings
from langchain_community.vectorstores import FAISS


def rag_indexing():
    document = load_document("./resources/CIS_Amazon_Web_Services_Foundations_Benchmark_v3.0.0.pdf")
    text = split_document(document)
    embeddings = create_embeddings()
    vector_store = create_vector_store(text, embeddings)
    retriever = setup_retriever(vector_store)
    return retriever


def load_document(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()
    return pages


def split_document(pages):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, add_start_index=True
    )
    all_splits = text_splitter.split_documents(pages)
    return all_splits


def create_embeddings():
    return BedrockEmbeddings(
        model_id="amazon.titan-embed-text-v1",
        region_name="us-east-1",
        credentials_profile_name="admin"
    )


def create_vector_store(texts, embeddings):
    return FAISS.from_documents(texts, embeddings)


def setup_retriever(vector_store):
    return vector_store.as_retriever(search_kwargs={"k": 3, "score_threshold": 70})
