from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import google.generativeai as genai
import requests

# Your API Keys
GOOGLE_API_KEY = "AIzaSyAbmG3Dq4aD5GGgZSFKLVXFlaF87ym07YY"  # Replace with your Google API key
TAVILY_API_KEY = "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"  # Replace with your Tavily API key

# Configure Google Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the chat model
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

# Create a simple prompt template
prompt = ChatPromptTemplate.from_messages([
    ("human", "{input}")
])

# Create the chain
chain = prompt | llm | StrOutputParser()

# Function to call Tavily Search API (Updated with POST request)
def search_online(query):
    url = "https://api.tavily.com/search"
    headers = {
        "Authorization": f"Bearer {TAVILY_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"query": query, "num_results": 3}  # Tavily requires a POST request

    try:
        response = requests.post(url, headers=headers, json=payload)  # Changed to POST
        if response.status_code == 200:
            results = response.json()
            if results and "results" in results and len(results["results"]) > 0:
                return "\n".join([f"- {item['title']}: {item['url']}" for item in results["results"]])
            else:
                return "⚠️ No relevant results found. Try rephrasing your question."
        else:
            return f"⚠️ Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"⚠️ Error fetching search results: {str(e)}"

# Function to check if a query needs real-time data
def needs_real_time_search(user_input):
    real_time_keywords = ["price", "stock", "today", "latest", "current", "update", "news"]
    return any(word in user_input.lower() for word in real_time_keywords)

# Function to handle chat
def chat_with_bot(user_input):
    if needs_real_time_search(user_input):  
        # If the question needs real-time data, use Tavily directly
        search_results = search_online(user_input)
        return f"🔍 Here are the latest results from the web:\n{search_results}"

    # Otherwise, use Gemini AI
    response = chain.invoke({"input": user_input})
    
    # If Gemini response is vague, use Tavily as backup
    if "I don't know" in response or "I do not have real-time access" in response:
        search_results = search_online(user_input)
        return f"{response}\n\n🔍 Here are some online results:\n{search_results}"

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
