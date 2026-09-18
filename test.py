response = client.complete_chat([
    {"role": "user", "content": "Hello!"}
])
print(response.choices[0].message.content)