from foundry_local_sdk import Configuration, FoundryLocalManager
	
FoundryLocalManager.initialize(Configuration(app_name="my-app"))
model = FoundryLocalManager.instance.catalog.get_model("qwen2.5-0.5b")
model.download(); model.load()
client = model.get_chat_client()
response = client.complete_chat([
    {"role": "user", "content": "Hello!"}
])
print(response.choices[0].message.content)
