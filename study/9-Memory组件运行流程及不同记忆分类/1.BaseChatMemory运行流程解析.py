#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/7/7 1:28
@Author :xiaobo
@File   :1.BaseChatMemory运行流程解析.py
"""
from langchain.memory.chat_memory import BaseChatMemory

"""
BaseChatMemory组件中，不同的属性与方法有不同的作用
1. chat_memory：用于管理记忆中的历史对话消息
2. output_key：定义AI内容输出key
3. input_key；定义human内容输入key
4. return_messages：load_memory_variables函数是否返回消息列表，默认为False代表返回字符串
5. save_context：存储上下文到记忆组件中（存储消息对话）
6. load_memory_variables：生成加载链的记忆字典信息
7. clear：清除记忆中的对话历史消息
"""
memory = BaseChatMemory(
    input_key="query",
    output_key="output",
    return_messages=True,
    # chat_history 假设
)

memory_variable = memory.load_memory_variables({})

# content = chain.invoke({"query": "你好，我是小博你是谁", "chat_history": memory_variable.get("chat_history")})
# memory.save_context({"query": "你好，我是小博你是谁"}, {"output": "你好，我是ChatGPT,有什么可以帮到您的"})
memory_variable = memory.load_memory_variables({})
# content = chain.invoke({"query": "你好，我是小博你是谁", "chat_history": memory_variable.get("chat_history")})
