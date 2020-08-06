from datetime import datetime

from pyvue import Component


messages = [
    {"sender": "John Doe", "content": "lol hi", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "what are you up to?", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "Jane Doe", "content": "nothing much. eating some ramen lol", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "thats cool", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
    {"sender": "John Doe", "content": "oh. brb", "time": datetime.now().strftime("%B %d, %Y , %H:%M")},
]


class Messages(Component):
    data = {
        'messages': messages,
        'current_user': 'Jane Doe',
    }

    template = "#messages-template"

    # template = "#messages"