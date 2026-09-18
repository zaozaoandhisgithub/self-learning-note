from foundry_local_sdk import Configuration, FoundryLocalManager,openai
	
FoundryLocalManager.initialize(Configuration(app_name="my-app"))
model = FoundryLocalManager.instance.catalog.get_model("qwen2.5-0.5b")
model.download(); model.load()
client = model.get_chat_client()

prompt =[ 
    {"role":"user","content":"Complete the following: Once upon a time there was a"}
]

response = client.complete_chat(prompt)
print(response.choices[0].message.content)