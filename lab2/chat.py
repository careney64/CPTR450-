import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from util import chat_ollama

def run_conversation():
    """A football conversation."""
    
    messages = [
        {
            'role': 'system',
            'content': 'You are a friendly football coach.'
        },
        {
            'role': 'user',
            'content': 'What is offside in football?'
        }
    ]
    
    # First response
    response = chat_ollama(messages, temperature=0.3)
    print("Coach:", response)
    
    # Second question
    messages.append({'role': 'assistant', 'content': response})
    messages.append({'role': 'user', 'content': 'How many players in a team?'})
    
    response = chat_ollama(messages, temperature=0.3)
    print("\nCoach:", response)
    
    # Third question  
    messages.append({'role': 'assistant', 'content': response})
    messages.append({'role': 'user', 'content': 'What is a penalty kick?'})
    
    response = chat_ollama(messages, temperature=0.3)
    print("\nCoach:", response)
    
    # Fourth question
    messages.append({'role': 'assistant', 'content': response})
    messages.append({'role': 'user', 'content': 'How long is a match?'})
    
    response = chat_ollama(messages, temperature=0.3)
    print("\nCoach:", response)

if __name__ == "__main__":
    run_conversation()