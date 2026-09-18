# self-learning-note
Microsoft courses：generative-ai-for-beginners and ai-agent-for-beginners;learning note
课程笔记，主要采用本地模型进行，部分课程由于一些限制没有进行演示代码复刻，如image-generation course，因为foundry-local并未提供对应的图像生成程序。

一些疑问与解答：

Q1：为什么选用本地模型而非云端模型？
A1：课程演示选用Microsoft foundry云，而25年新规后，由于区域限制，无法在中国大陆地区以个人用户的身份进行模型部署，而例如deepseek-v4.1-flash之类的模型，由于配额限制，也无法完成部署，因此难以获得部署模型与其api，endpoint

Q2：示例代码能直接跑通吗？如何进行修改使之适配用户使用的模型？
A2：如Q1所答，课程演示使用foundry云，对应代码包括配置部署模型与其api，endpoint，因此改用本地模型后，由于本地模型动态获取api，无需导入dotenv库来配置环境，可以直接下载对应模型并获取接口，模型会自动选择使用GPU加速或者其他功能。
同样由于这些原因，代码中输入输出的格式也需要进行一定变化，详情参考foundry文档或利用可访问模型如deepseek网页版进行查询。

Q3：
