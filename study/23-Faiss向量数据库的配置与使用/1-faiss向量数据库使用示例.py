#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/7/19 22:35
@Author :xiaobo
@File   :1-faiss向量数据库使用示例.py
"""
import dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

dotenv.load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-small")

texts: list = [
    "笨笨是一只很喜欢睡觉的猫咪",
    "我喜欢在夜晚听音乐，这让我感到放松。",
    "猫咪在窗台上打盹，看起来非常可爱。",
    "学习新技能是每个人都应该追求的目标。",
    "我最喜欢的食物是意大利面，尤其是番茄酱的那种。",
    "昨晚我做了一个奇怪的梦，梦见自己在太空飞行。",
    "我的手机突然关机了，让我有些焦虑。",
    "阅读是我每天都会做的事情，我觉得很充实。",
    "他们一起计划了一次周末的野餐，希望天气能好。",
    "我的狗喜欢追逐球，看起来非常开心。",
]
metadatas: list = [
    {"page": 1},
    {"page": 2},
    {"page": 3},
    {"page": 4},
    {"page": 5},
    {"page": 6},
    {"page": 7},
    {"page": 8},
    {"page": 9},
    {"page": 10},
]
db = FAISS.from_texts(texts, embedding, metadatas)

# 保存到本地数据库
db.save_local("./vector-store/")

# 后续使用直接使用本地的数据库
new_db = FAISS.load_local("./vector-store/", embedding, allow_dangerous_deserialization=True)
result = new_db.similarity_search("我养了一只猫，叫笨笨")
print(result)
