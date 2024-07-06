#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/7/7 0:26
@Author :xiaobo
@File   :1.对话消息历史组件基础.py
"""
from langchain_core.chat_history import InMemoryChatMessageHistory

chat_history = InMemoryChatMessageHistory()  # 将对话消息存储到临时内存中

chat_history.add_user_message("你好，我是小博，你是谁？")
chat_history.add_ai_message("你好，我是ChatGPT，有什么可以帮到您的？")
chat_history.add_user_message("你好，我是小博，你是谁？")
chat_history.add_ai_message("你好，我是ChatGPT，有什么可以帮到您的？")

print(chat_history.messages)
