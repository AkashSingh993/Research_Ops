import os

from rag.retriever import Retriever


class RetrievalAgent:

    def __init__(self):

        self.retriever = Retriever()

        index_exists = os.path.exists(
            "storage/vector_db/faiss.index"
        )

        docs_exist = os.path.exists(
            "storage/vector_db/documents.pkl"
        )

        if index_exists and docs_exist:

            self.retriever.load_vector_store()

            print(
                "[LOADED] Vector Store"
            )

        else:

            print(
                "[INFO] No vector database found yet."
            )

    def run(
        self,
        query,
        top_k=5
    ):

        if self.retriever.vector_store is None:

            raise Exception(
                "No corpus has been uploaded yet. Please upload PDFs first."
            )

        results = self.retriever.retrieve(
            query=query,
            top_k=top_k
        )

        return {
            "query": query,
            "retrieved_contexts": results
        }