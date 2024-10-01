import uuid
from typing import Dict

from langchain_core.chat_history import BaseChatMessageHistory
from conversation import Conversation

chat_history_store: Dict[str, BaseChatMessageHistory] = {}


def main():
    print("Welcome to the Rego Code Converter!")
    session_id = str(uuid.uuid4())
    conversation = Conversation()
    conversation.setup_conversation()
    conversation.invoke_conversation()

if __name__ == "__main__":
    main()
