from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import google.generativeai as genai

# Your Google API key setup
GOOGLE_API_KEY = "AIzaSyAbmG3Dq4aD5GGgZSFKLVXFlaF87ym07YY"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the chat model
llm = ChatGoogleGenerativeAI(model="gemini-pro", 
                            google_api_key=GOOGLE_API_KEY)

# Create a simple prompt template without system message
prompt = ChatPromptTemplate.from_messages([
    ("human", "{input}")
])

# Create the chain
chain = prompt | llm | StrOutputParser()

# Function to handle chat
def chat_with_bot(user_input):
    response = chain.invoke({"input": user_input})
    return response

# Main chat loop
if __name__ == "__main__":
    print("Chat with the bot (type 'quit' to exit)")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'quit':
            break
        
        response = chat_with_bot(user_input)
        print(f"\nBot: {response}")