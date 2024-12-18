# 20241219 gjw Begin a chat script using ollama.

from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)

# As a stream:

# stream = chat(
#   model='mistral',
#   messages=[{'role': 'user', 'content': 'Name an engineer that passes the vibe check'}],
#   stream=True
# )

# for chunk in stream:
#   print(chunk['message']['content'], end='', flush=True)


stream = chat(
    model='llama3.2',
    messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)
