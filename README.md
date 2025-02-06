# langchain_gemini_chatbot

### **Explanation of the Code**  

This script sets up a chatbot using **LangChain** and **Google Gemini AI (gemini-pro)**. Below is a breakdown of how it works:

1. **Import Necessary Modules**  
   - `ChatGoogleGenerativeAI` (from `langchain_google_genai`) is used to interact with Google's **Gemini AI**.
   - `StrOutputParser` (from `langchain_core.output_parsers`) converts the model’s output into a string format.
   - `ChatPromptTemplate` (from `langchain_core.prompts`) is used to define how user input is structured before being sent to the AI model.
   - `google.generativeai` is the official Google AI library for configuring and using **Gemini AI**.

2. **Set Up Google Gemini AI API Key**  
   - The `GOOGLE_API_KEY` is needed to authenticate requests to Google's AI service.
   - The script initializes `genai.configure(api_key=GOOGLE_API_KEY)` to set up the API key for communication with **Gemini AI**.

3. **Initialize the Language Model (LLM)**  
   - The `ChatGoogleGenerativeAI` model is initialized with `"gemini-pro"` as the selected AI model.
   - The API key is passed to ensure authentication.

4. **Define the Chat Prompt**  
   - A `ChatPromptTemplate` is created to format user input.
   - It takes `{input}` as a placeholder for user messages.

5. **Create a Processing Chain**  
   - The `chain` variable is created by connecting (`|` operator) the **prompt**, **LLM model**, and **output parser**.
   - This ensures that user input is processed, passed to the AI model, and the response is formatted correctly.

6. **Function to Handle Chat (`chat_with_bot`)**  
   - This function takes user input, processes it through the `chain`, and returns the chatbot's response.

7. **Main Loop for Chat Interaction**  
   - The script runs an interactive chat session.
   - It continuously takes user input and provides responses from Gemini AI.
   - If the user types `"quit"`, the script exits the chat.

---

### **Dependencies to Install**  
Before running this script, install the required dependencies using **pip**:

```bash
pip install langchain langchain-google-genai google-generativeai
```

If you face issues, also install:

```bash
pip install langchain-core
```

This will ensure you have all the necessary packages to run the chatbot.

Let me know if you need further assistance! 🚀
