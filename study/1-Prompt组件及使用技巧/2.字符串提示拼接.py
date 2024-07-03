#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/6/30 12:25
@Author :xiaobo
@File   :2.字符串提示拼接.py
"""
from langchain_core.prompts import PromptTemplate

# PromptTemplate.from_template返回的是PromptTemplate类实例，但内部重写了魔术方法__add__
# 但是 使用+这种形式，第一个值必须是PromptTemplate类实例，不能是字符串
prompt = (
        PromptTemplate.from_template("请讲一个关于{subject}的冷笑话")
        + ",让我开心下" +
        "\n使用{language}语言"
)
"""
text='请讲一个关于程序员的冷笑话,让我开心下\n使用中文语言'
"""
print(prompt.invoke({"subject": "程序员", "language": "中文"}))
"""
请讲一个关于程序员的冷笑话,让我开心下
使用中文语言
"""
print(prompt.invoke({"subject": "程序员", "language": "中文"}).to_string())
