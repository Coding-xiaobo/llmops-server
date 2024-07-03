#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/6/30 12:34
@Author :xiaobo
@File   :3.消息提示模版拼接.py
"""
from langchain_core.prompts import ChatPromptTemplate

system_chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请根据用户的提问进行回复，我叫{username}"),
])
human_chat_prompt = ChatPromptTemplate.from_messages([
    ("human", "{query}")
])
# ChatPromptTemplate类型可以+
chat_prompt = system_chat_prompt + human_chat_prompt
"""
input_variables=['query', 'username'] messages=[SystemMessagePromptTemplate(prompt=PromptTemplate(input_variables=['username'], template='你是OpenAI开发的聊天机器人，请根据用户的提问进行回复，我叫{username}')), HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['query'], template='{query}'))]
"""
print(chat_prompt)
"""
messages=[SystemMessage(content='你是OpenAI开发的聊天机器人，请根据用户的提问进行回复，我叫xiaobo'), HumanMessage(content='你好，你是?')]
"""
print(chat_prompt.invoke({
    "username": "xiaobo",
    "query": "你好，你是?"
}))
"""
System: 你是OpenAI开发的聊天机器人，请根据用户的提问进行回复，我叫xiaobo
Human: 你好，你是?
"""
print(chat_prompt.invoke({
    "username": "xiaobo",
    "query": "你好，你是?"
}).to_string())
