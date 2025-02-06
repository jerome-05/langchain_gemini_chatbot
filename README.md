# 🤖 AI Chatbot with Google Gemini & Tavily Search  

This project is an AI-powered chatbot using **Google Gemini (Gemini Pro)** for conversational AI and **Tavily Search API** for real-time web search. The chatbot determines whether a query requires real-time data and intelligently selects between the Gemini AI model or Tavily search.  

## ✨ Features  
- **Conversational AI**: Uses Google Gemini (Gemini Pro) for natural language understanding.  
- **Real-Time Search**: Integrates Tavily Search API for fetching live web data.  
- **Smart Query Handling**: Determines whether to use AI-generated responses or real-time search results.  
- **Fallback Mechanism**: If Gemini's response is vague, Tavily search is used as a backup.  

## 📌 Installation  

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/yourusername/ai-chatbot.git  
cd ai-chatbot
```  

2️⃣ **Install dependencies**  
```bash
pip install -r requirements.txt  
```  

3️⃣ **Set up API keys**  
Replace the placeholders in the code with your **Google Gemini API Key** and **Tavily API Key**.  

## 🚀 Usage  
Run the chatbot in your terminal:  
```bash
python chatbot.py
```  
Then, type your queries:  
- **General queries** → Answered by Google Gemini AI  
- **Real-time queries** (e.g., news, stock prices) → Fetched using Tavily Search API  

To exit, type `quit`.  

## 🏗️ Project Structure  
```
├── chatbot.py           # Main chatbot script
├── requirements.txt     # Required Python packages
└── README.md            # Project documentation
```

## 🔍 Example  
```plaintext
You: What's the latest news on AI?  
Bot: 🔍 Here are the latest results from the web:  
- "AI Breakthrough in 2025" - example.com/news1  
- "How AI is Changing the World" - example.com/news2  
```

## 📜 License  
MIT License  

---
## OUTPUT
