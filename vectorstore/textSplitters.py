from langchain_text_splitters import RecursiveCharacterTextSplitter
from vectorstore.documentLoader import sorted_manifestoes

chunked_manifestoes={}
def chunking_files():
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 150,
        chunk_overlap = 0,
        length_function = len,
        separators=['\n\n', '\n', ' ', '']
    )

    for candidate in sorted_manifestoes:
        chunks=text_splitter.split_documents(sorted_manifestoes[candidate])

        chunked_manifestoes[candidate] = chunks

