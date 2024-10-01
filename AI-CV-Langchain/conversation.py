from typing import Dict

from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_aws import ChatBedrock
from langchain_community.chat_message_histories import ChatMessageHistory

from prompts import PROMPT

chat_history_store: Dict[str, BaseChatMessageHistory] = {}


class Conversation:
    def __init__(self):
        self.conversation = self.setup_conversation(PROMPT)

    @staticmethod
    def get_session_history(session_id: str) -> BaseChatMessageHistory:
        return chat_history_store.setdefault(session_id, ChatMessageHistory())

    @staticmethod
    def create_bedrock_llm():
        return ChatBedrock(
            model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
            model_kwargs=dict(temperature=0),
            region_name="us-east-1",
            credentials_profile_name="admin"
        )

    def create_runnable_with_history(self, prompt: ChatPromptTemplate, output_parser=None):
        bedrock_llm = self.create_bedrock_llm()
        chain = prompt | (bedrock_llm.with_structured_output(output_parser) if output_parser else bedrock_llm)
        return RunnableWithMessageHistory(
            chain,
            self.get_session_history,
            input_messages_key="input",
            history_messages_key="history",
        )

    def setup_conversation(self, system_prompt=None):
        messages = []
        if system_prompt:
            messages.append(("system", system_prompt))
        messages.extend([
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ])
        prompt = ChatPromptTemplate.from_messages(messages)
        return self.create_runnable_with_history(prompt)

    def invoke_conversation(self, formatted_prompt: str, session_id: str, conversation=None):
        chat_history = self.get_session_history(session_id)
        chat_history.add_user_message(formatted_prompt)

        conversation = conversation or self.conversation
        response = conversation.invoke(
            {"input": formatted_prompt},
            config={"configurable": {"session_id": session_id}}
        )

        chat_history.add_ai_message(str(response))
        return response

    def convert_to_rego(self, session_id: str):
        return self.invoke_conversation(PROMPT, session_id)
