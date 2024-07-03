#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/6/30 15:58
@Author :xiaobo
@File   :3.Model流式输出.py
"""
from datetime import datetime

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 1.编排prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请回答用户的问题，现在的时间是{now}"),
    ("human", "{query}"),
]).partial(now=datetime.now())

# 2.创建大语言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

response = llm.stream(prompt.invoke({"query": "你能简单介绍下LLM和LLMOps吗?"}))

# chunk是BaseMessageChunk 继承自BaseMessage
# flush=True参数确保每次输出后，数据都会立即被刷新到标准输出（通常是控制台或终端），而不是留在缓冲区中
for chunk in response:
    print(chunk.content, flush=True, end="")
