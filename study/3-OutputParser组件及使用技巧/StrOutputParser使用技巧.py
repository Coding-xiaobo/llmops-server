#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/6/30 16:13
@Author :xiaobo
@File   :StrOutputParser使用技巧.py
"""
import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 1.编排提示模板
prompt = ChatPromptTemplate.from_template("{query}")

# 2.构建大语言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

# 3.创建字符串输出解析器
parser = StrOutputParser()

# 4.调用大语言模型生成结果并解析
content = parser.invoke(llm.invoke(prompt.invoke({"query": "你好，你是?"})))
# 你好！我是ChatGPT，一个基于人工智能的语言模型。有什么我可以帮助你的吗？
print(content)
