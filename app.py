import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMChain,LLMMathChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
# from dotenv import load_dotenv
# import os   
from langchain.callbacks import StreamlitCallbackHandler

## Set up the streamlit app
st.set_page_config(page_title="Text to Math Problem Solver and Data Search Assistant",page_icon=":books:")
st.title("Text to Math Problem Solver and Data Search Assistant Using Google Gemma 2")

groq_api_key = st.sidebar.text_input(label="Enter your Groq API Key", type="password")

if not groq_api_key:
    st.info("Please enter your Groq API Key in the sidebar to use the app.")
    st.stop()

elif groq_api_key:
    st.info("Groq API Key is set. You can now use the app.")
    

llm = ChatGroq(model='gemma2-9b-it',groq_api_key=groq_api_key)

## Initializing the tools
wikipedia_wrapper=WikipediaAPIWrapper()
wekepidia_tool = Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description='A tool for searching the Internet to find the vatious information to the topic'
    )

## Initialize the Math tool
math_chain = LLMMathChain.from_llm(llm=llm)
calculator = Tool(name='Calculator',
                  func=math_chain.run,
                  description='A tool for solving math problems. Input should be a math problem in text form, e.g., "What is 2 + 2?"')


prompt = """ 
You are a agent tasked for solving users mathematical problems and searching the Internet for information.
Logically arriveat the solution and display it point wise for the giestion below.
Question:{question}
Answer:
"""

prompt_template = PromptTemplate(
    input_variables=["question"],
    template=prompt)

## Combine all the tools into chains
chain =LLMChain(llm=llm, prompt=prompt_template)

reasoning_tool = Tool(name="Reasoning",
                      func=chain.run,
                      description="A tool for solving logic based resoning questions"
                      )

## Initialize the agent with the tools
assistant_agent = initialize_agent(
                tools=[calculator, wekepidia_tool, reasoning_tool],
                agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                llm=llm,
                verbose=False,
                handle_parsing_errors=True,
                )

if "messages" not in st.session_state:
    st.session_state['messages'] = [
        {'role':'assistant', 'content': 'Hi, I am a ChatBot who can answer your problems.'}

    ]
for msg in st.session_state['messages']:
    st.chat_message(msg['role']).write(msg['content'])

#lets start the chat

question = st.text_area('Enter your question here:', placeholder='Type your question here...')

if st.button('Find the Solution'):
    if question:
        with st.spinner('Finding the solution...'):
            st.session_state.messages.append({'role':'user', 'content': question})
            st.chat_message('user').write(question)

            st_cb = StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
            response = assistant_agent.run(question, callbacks=[st_cb])
            
            st.session_state.messages.append({'role':'assistant', 'content': response})
            st.write('### Response:')
            st.success(response)

    else:
        st.warning('Please enter a question to get an answer.')