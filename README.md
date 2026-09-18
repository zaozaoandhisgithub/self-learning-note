# self-learning-note
Microsoft courses：generative-ai-for-beginners and ai-agent-for-beginners;learning note<br>
课程笔记，主要采用本地模型进行，部分课程由于一些限制没有进行演示代码复刻，如image-generation course，因为foundry-local并未提供对应的图像生成程序。

一些疑问与解答：

Q1：为什么选用本地模型而非云端模型？<br>
A1：课程演示选用Microsoft foundry云，而25年新规后，由于区域限制，无法在中国大陆地区以个人用户的身份进行模型部署，而例如deepseek-v4.1-flash之类的模型，由于配额限制，也无法完成部署，因此难以获得部署模型与其api，endpoint

Q2：示例代码能直接跑通吗？如何进行修改使之适配用户使用的模型？<br>
A2：如Q1所答，课程演示使用foundry云，对应代码包括配置部署模型与其api，endpoint，因此改用本地模型后，由于本地模型动态获取api，无需导入dotenv库来配置环境，可以直接下载对应模型并获取接口，模型会自动选择使用GPU加速或者其他功能。<br>
  同样由于这些原因，代码中输入输出的格式也需要进行一定变化，详情参考foundry文档或利用可访问模型如deepseek网页版进行查询。

其他问题可以留言我进行交流，ty

在本地安装foundry-local-sdk<br>
需要：vscode and python 3.12及以上版本(建议3.12版本，过新的版本未必适配ai库，这也是笔者在学习过程中遇到过的问题)<br>

建议：使用虚拟环境进行隔离，以免各类库发生冲突，建议每个工程都做一个单独的虚拟环境，操作实例在下方具体说明。<br>

第一步（创建虚拟环境）：<br>
打开vscode terminal （终端），输入<br>
cd 你的路径\文件夹名称\  <br>
python -m venv .venv   <br>
.\.venv\Scripts\activate  #window环境激活<br>

此时应该进入（.venv）环境<br>

第二步：<br>
在终端输入：<br>
pip intall foundry-local-sdk <br> 

第三步：<br>
创建一个py文件，输入（我的文件中men.py文件）<br>

from foundry_local_sdk import Configuration, FoundryLocalManager<br>
	
FoundryLocalManager.initialize(Configuration(app_name="my-app"))<br>
model = FoundryLocalManager.instance.catalog.get_model("qwen3-0.6b")  #模型名称<br>
model.download(); model.load()<br>
client = model.get_chat_client()    #装载模型并进行初始化<br>

response = client.complete_chat([<br>
    {"role": "user", "content": "Hello!"}<br>
])<br>
print(response.choices[0].message.content)    #测试输出<br>

如正确，应当出现类似：<br>
HI！How can i assitant you？<br>



说明：<br>
1.如需要为不同工程创建虚拟环境，只需在第一步修改路径，如果创建成功，可在文件资源管理器对应路径下发现.venv文件夹<br>
2.部分课程需要安装不同的包，例如pandas等，可以在进入虚拟环境后，运行pip install pandas指令来进行安装，此时该包不影响全局环境<br>
3.如在本地学习对应两门课程，请先克隆原课程仓库，并在第一次创建虚拟环境时带入requirements.txt，具体方法可以访问原课程指导文档<br>
4.提示，对于本地设备性能受限的对象，个人建议尝试使用国内模型api和endpoint来进行课程，笔者的设备为laptop RTX 4050 6gb，运行本地模型时有显著的性能壁垒，相比而言使用云模型的速度会快得多。<br>
5.对于foundry-local的部分语法，请访问foundry文档进行查看，有一个快速开始指南，讲解了基本的功能，其余语法可以通过各种途径进行学习，个人建议使用国内模型来辅助学习，同时也是对prompt engineering很好的工程实践<br>
