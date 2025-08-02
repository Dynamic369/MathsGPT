# MathsGPT
# MathsGPT: Text to Math Problem Solver and Data Search Assistant

This Streamlit app is an intelligent chatbot that can solve mathematical problems and search for information using Wikipedia. It leverages the Groq LLM (Google Gemma 2) and LangChain tools to provide logical, step-by-step solutions and relevant data for user queries.

---

## Features

- **Math Problem Solving:**  
  Enter any math question and get a detailed, point-wise solution using the Groq LLM and LangChain's math tools.

- **Wikipedia Search:**  
  Ask for information on any topic, and the bot will fetch and summarize relevant data from Wikipedia.

- **Logic & Reasoning:**  
  The agent can handle logic-based reasoning questions and provide structured answers.

- **Conversational Chatbot:**  
  Maintains chat history and responds interactively to user queries.

---

## How It Works

1. **Groq API Key:**  
   Enter your Groq API key in the sidebar to activate the app.

2. **Tools Initialization:**  
   - **Calculator:** Uses LangChain's `LLMMathChain` for math problems.
   - **Wikipedia:** Uses `WikipediaAPIWrapper` to fetch information.
   - **Reasoning:** Uses a custom prompt and LLMChain for logic questions.

3. **Agent Setup:**  
   All tools are combined into a LangChain agent (`initialize_agent`) that decides which tool to use based on the user's question.

4. **Chat Interface:**  
   - The assistant greets the user.
   - Users enter questions in a text area.
   - The agent processes the question and returns a detailed, point-wise answer.

---

## Usage

### 1. Install Dependencies

```bash
pip install streamlit langchain langchain_groq langchain_community
```

### 2. Run the App

Open a terminal and navigate to the project directory:

```bash
cd "c:\Users\Pradum Gupta\OneDrive\Desktop\udemy\Langchain Projects 2\3.MathsGPT"
streamlit run app.py
```

### 3. Enter Your Groq API Key

- Paste your Groq API key in the sidebar input.
- Start asking math or information questions!

---

## Example Questions

- `What is the derivative of x^2 + 3x + 5?`
- `Who is Albert Einstein?`
- `Solve: 2x + 3 = 7`
- `What is the capital of France?`
- `Explain the Pythagorean theorem.`

---

## Code Structure

- **app.py:** Main Streamlit app file.
- **LangChain Tools:** Calculator, Wikipedia, Reasoning.
- **Agent:** Combines all tools and handles user queries.
- **Prompt:** Custom prompt for logical, point-wise answers.

---

## Notes

- You must have a valid Groq API key to use the app.
- The app uses Google Gemma 2 (`gemma2-9b-it`) as the LLM.
- All logic, math, and search queries are handled via LangChain agent tools.

---

## License

This project is for educational purposes and follows Udemy
