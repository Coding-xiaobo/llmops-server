#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/6/30 15:48
@Author :xiaobo
@File   :2.Model批处理.py
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

# 批处理使用batch，参数是一个列表 List[Input] 并且不存在上下文关系
ai_messages = llm.batch([
    prompt.invoke({"query": "你好，你是?"}),
    prompt.invoke({"query": "请讲一个关于程序员的冷笑话"}),
])

for ai_message in ai_messages:
    print(ai_message.content)
    print("====================")
