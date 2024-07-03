#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/6/30 11:06
@Author :xiaobo
@File   :1.Prompt组件基础用法.py
"""
from datetime import datetime

from langchain_core.messages import AIMessage
from langchain_core.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)

# 从模版字符串创建提示词模版
prompt = PromptTemplate.from_template("请讲一个关于{subject}的冷笑话")
print(prompt)  # input_variables=['subject'] template='请讲一个关于{subject}的冷笑话'
# 返回类型PromptValue 是一个提示词，既可以转换成string，也可以转换成人类消息
prompt_value = prompt.invoke({"subject": "程序员"})
print(prompt_value)  # text='请讲一个关于程序员的冷笑话'
print(prompt.format(subject="喜剧演员"))  # 请讲一个关于喜剧演员的冷笑话
print(prompt_value.to_string())  # 请讲一个关于程序员的冷笑话
print(prompt_value.to_messages())  # [HumanMessage(content='请讲一个关于程序员的冷笑话')]

print("==================")

# 也提供from_template方法，用法和PromptTemplate一样
chat_prompt = ChatPromptTemplate.from_messages([
    # 传入一个元组
    ("system", "你是OpenAI开发的聊天机器人，请根据用户的提问进行回复，当前的时间为:{now}"),
    # 有时候可能还有其他的消息，但是不确定，如历史消息
    MessagesPlaceholder("chat_history"),
    # 传入HumanMessagePromptTemplate类，人类消息提示模版
    HumanMessagePromptTemplate.from_template("请讲一个关于{subject}的冷笑话"),
]).partial(now=datetime.now())  # partial先将模版中的变量赋值，然后返回的仍然是模版

# 使用消息占位符，添加多条消息，把变量传递给模版进行格式化
chat_prompt_value = chat_prompt.invoke({
    "chat_history": [
        ("human", "我叫xiaobo"),
        AIMessage("你好，我是ChatGPT，有什么可以帮到您"),
    ],
    "subject": "程序员",
})
"""
messages=[SystemMessage(content='你是OpenAI开发的聊天机器人，请根据用户的提问进行回复，当前的时间为:2024-06-30 12:10:27.527808'), HumanMessage(content='我叫xiaobo'), AIMessage(content='你好，我是ChatGPT，有什么可以帮到您'), HumanMessage(content='请讲一个关于程序员的冷笑话')]
"""
print(chat_prompt_value)
"""
System: 你是OpenAI开发的聊天机器人，请根据用户的提问进行回复，当前的时间为:2024-06-30 12:10:27.527808
Human: 我叫xiaobo
AI: 你好，我是ChatGPT，有什么可以帮到您
Human: 请讲一个关于程序员的冷笑话
"""
print(chat_prompt_value.to_string())
