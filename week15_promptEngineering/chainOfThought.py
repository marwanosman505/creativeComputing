from dotenv import load_dotenv
import os
import sys

from operator import itemgetter

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

# get api key from environment variable
load_dotenv()
API_KEY = os.getenv("API_KEY")

# initialize model
model = ChatOpenAI(api_key=API_KEY)

# unstructured prompt
unstructuredPrompt = "You are a project delivery team lead and want to achieve 3 out of the 4 credits in the manual:\n" +open(os.path.join(sys.path[0], "./data.json"), "r").read()



print(unstructuredPrompt)

#print(model.invoke(unstructuredPrompt))

# structured prompt
prompt1 = ChatPromptTemplate.from_template("You are a project delivery team lead and want to achieve 3 out of the 4 credits in the manual:\n" +open(os.path.join(sys.path[0], "./data.json"), "r").read()+"\n\nReturn the pros and cons for each credit and nothing else:")

prompt2 = ChatPromptTemplate.from_template("Here are the pros and cons for each credit:{pros_and_cons}Return the credits that you will achieve and why:")


# sentiment = model.invoke(prompt1)   
chain1 = prompt1 | model | StrOutputParser()
chain2 = {"pros_and_cons": chain1} | prompt2 | model | StrOutputParser()

print(chain1.invoke({"None": "None"}))
# print(chain2.invoke({"None": "None"}))

