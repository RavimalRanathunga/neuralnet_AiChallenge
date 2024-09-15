from vectorstore.documentLoader import document_loading,sorted_manifestoes
from vectorstore.textSplitters import chunking_files,chunked_manifestoes
from vectorstore.retrivers import Retriver
from main import main
#load the documents
document_loading()
# for candidate in sorted_manifestoes:
#     print(len(sorted_manifestoes[candidate]))

#chunks the all documents
chunking_files()
# for candidate in chunked_manifestoes:
#     print(candidate,len(chunked_manifestoes[candidate]))

#initializing the embedding model
retriver_object=Retriver()
embedding_model=retriver_object.initilize_embedding_model()
# print(embedding_model)

for candidate in chunked_manifestoes:
    retriver_object.add_documents(candidate,embedding_model,chunked_manifestoes[candidate])

main(retriver_object.retrivers)





