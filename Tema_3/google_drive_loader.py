from langchain_community.document_loaders import GoogleDriveLoader

credentials_path = "C:\\Users\\ASUS\\Documents\\PROGRAMACION\\INTELIGENCIA ARTIFICIAL 2\\analisis_hoja_vida\\Tema_3\\credentials.json"
token_path = "C:\\Users\\ASUS\\Documents\\PROGRAMACION\\INTELIGENCIA ARTIFICIAL 2\\analisis_hoja_vida\\Tema_3\\token.json"

loader = GoogleDriveLoader(
    folder_id="1-oFS81zRSo7mFjGMcVaLxAqfBGEFXSEB",
    credentials_path=credentials_path,
    token_path=token_path,
    recursive=True
)


documents = loader.load()

print(f"Metadatos: {documents[0].metadata}")
print(f"Contenido: {documents[0].page_content}")