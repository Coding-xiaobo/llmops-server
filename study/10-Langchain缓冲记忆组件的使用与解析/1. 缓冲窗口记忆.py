#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/7/7 11:15
@Author :xiaobo
@File   :1. 缓冲窗口记忆.py
"""

import dotenv
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

dotenv.load_dotenv()

# 1. 创建提示模版
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请根据对应的上下人回复用户问题"),
    MessagesPlaceholder("history"),
    ("human", "{query}")
])

# 2. 创建大语言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
# 在这里调整记忆模型
memory = ConversationBufferWindowMemory(
    k=2,
    return_messages=True,
    input_key="query"
)
# load_memory_variables返回的是字典，key是memory_key，值是buffer
# RunnableLambda(memory.load_memory_variables)将传递的函数编程可运行协议Runnable
# | itemgetter("history")  提取history 等价于 (lambda x : x.get("history")) 传入x字典，提取字典中的history
# 第一部分做的就是将传递的query添加上history的key value 返回的是一个字段，含有query和history两个key
chain = RunnablePassthrough.assign(
    history=RunnableLambda(memory.load_memory_variables) | itemgetter("history")
) | prompt | llm | StrOutputParser()

# 4. 对话
while True:
    query = input("Human: ")
    if query == 'q':
        exit(0)
    chain_input = {"query": query}

    response = chain.stream(chain_input)
    print("AI: ", flush=True, end="")
    output = ""
    for chunk in response:
        output += chunk
        print(chunk, flush=True, end="")
    memory.save_context(chain_input, {"output": output})
    print("")
    print("history: ", memory.load_memory_variables({}))
