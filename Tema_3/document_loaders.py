from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("C:\\Users\\ASUS\\Documents\\PROGRAMACION\\INTELIGENCIA ARTIFICIAL 2\\analisis_hoja_vida\\Tema_3\\Currículum Vitae Minimalista Blanco y Negro.pdf")

pages = loader.load()

for i, page in enumerate(pages):
    print(f"=== Pagina {i+1} ===")
    print(f"Contenido: {page.page_content}")
    print(f"Metadatos: {page.metadata}")