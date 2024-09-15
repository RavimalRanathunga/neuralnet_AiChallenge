from langchain_community.document_loaders import PyPDFLoader

class DocumentLoader:

    def __init__(self,file_path) -> None:
        self.filepath=file_path
        self.sorted_pdf=[]

    def load_documents(self):
        loader = PyPDFLoader(self.filepath)
        pdf_data = loader.load()
        return pdf_data
    
    def sort_pdf_documents(self,pdf_data):
        for data in pdf_data:
            if data.page_content == "":
                pass
            else:
                self.sorted_pdf.append(data)

        return self.sorted_pdf

cadidate_manifesto_file_paths={"namal rajapaksha":"docs\manifesto-namal.pdf","sajith premadasa":"docs\manifesto-sajith.pdf","anura kumara":"docs\manifesto-anura.pdf","ranil wikramasimghe":"docs\manifesto-ranil.pdf"}
sorted_manifestoes={}

def document_loading():
    for candidate in cadidate_manifesto_file_paths:
        document=DocumentLoader(cadidate_manifesto_file_paths[candidate])
        pdf_data=document.load_documents()

        sorted_pdf=document.sort_pdf_documents(pdf_data)
        sorted_manifestoes[candidate] = sorted_pdf






















