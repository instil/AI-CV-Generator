import json

def save_chat_history(memory, filename):
    history = [{"role": "human" if isinstance(m, HumanMessage) else "ai", "content": m.content} 
               for m in memory.chat_memory.messages]
    with open(filename, 'w') as f:
        json.dump(history, f)

def load_chat_history(memory, filename):
    with open(filename, 'r') as f:
        history = json.load(f)
    for message in history:
        if message["role"] == "human":
            memory.chat_memory.add_user_message(message["content"])
        else:
            memory.chat_memory.add_ai_message(message["content"])

# Usage
save_chat_history(memory, "chat_history.json")
# Later or in a new session
load_chat_history(memory, "chat_history.json")