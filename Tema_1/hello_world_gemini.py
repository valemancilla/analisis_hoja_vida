from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.7)

pregunta = "En que año llego el ser humano a la luna por primera vez?"

respuesta = llm.invoke(pregunta)
print("Rewspuestas", respuesta.content)