import os
from dotenv import load_dotenv

from langchain_openai import AzureChatOpenAI
from langchain.chains import LLMChain
from langchain_core.documents import Document
from langchain_openai import AzureChatOpenAI

class openai:
    def __init__(self):
        self.llm = AzureChatOpenAI(
            azure_endpoint=os.getenv("AZURE_ENDPOINT"),
            deployment_name=os.getenv("DEPLPOYMENT_NAME"),
            temperature=0.5,
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            openai_api_version=os.getenv("OPENAI_API_VER"),
        )

    def get_chain(self, prompt):
        return LLMChain(llm=self.llm, prompt=prompt)

    def invoke_req(self, chain, text):
        return chain.invoke({'text': text}).get('text')
        