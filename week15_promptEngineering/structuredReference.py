import os
from dotenv import load_dotenv
import sys

from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

load_dotenv()

# os.environ["API_KEY"] = Constants.APIKEY

query = sys.argv[1]

loader = TextLoader("data.json")
#loader = DirectoryLoader(".", glob="*.txt")
index = VectorstoreIndexCreator().from_loaders([loader])

# print(index.query(query))
print(index.query(query, llm=ChatOpenAI()) )