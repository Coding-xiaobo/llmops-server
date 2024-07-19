#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/7/19 15:10
@Author :xiaobo
@File   :1-HuggingFace本地其纳入模型.py
"""
from langchain_huggingface import HuggingFaceEmbeddings
import os

os.environ['HF_ENDPOINT'] = 'hf-mirror.com'
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L12-v2",
    cache_folder="./embeddings/"
)

query_vector = embeddings.embed_query("你好，我是小赵，我喜欢打篮球")

print(query_vector)
print(len(query_vector))
