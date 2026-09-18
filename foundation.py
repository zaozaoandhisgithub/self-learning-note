from dotenv import load_dotenv
import os

# 从.env文件加载环境变量
load_dotenv(".env")

# 访问Microsoft Foundry模型变量
endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

print(endpoint)