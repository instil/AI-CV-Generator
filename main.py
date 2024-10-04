import uuid
from typing import Dict

from langchain_core.chat_history import BaseChatMessageHistory
from conversation import Conversation

chat_history_store: Dict[str, BaseChatMessageHistory] = {}


def main():
    print("Welcome to the Instil CV Converter!")
    session_id = str(uuid.uuid4())
    conversation = Conversation()
    conversation.setup_conversation()
    response = conversation.convert_to_cv(session_id=session_id)
    print(response)

if __name__ == "__main__":
    main()
