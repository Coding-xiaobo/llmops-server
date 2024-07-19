#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/7/19 13:58
@Author :xiaobo
@File   :OpenAI嵌入模型.py
"""

import numpy as np
from numpy.linalg import norm
import dotenv
from langchain_openai import OpenAIEmbeddings

dotenv.load_dotenv()


def cosine_similarity(vec1: list, vec2: list) -> float:
    """计算传入两个向量的余弦相似度"""
    # 1. 计算两个向量的点积
    dot_product = np.dot(vec1, vec2)
    # 2. 计算两个向量的长度
    vec1_norm = np.linalg.norm(vec1)
    vec2_norm = np.linalg.norm(vec2)
    # 3. 计算余弦相似度
    return dot_product / (vec1_norm * vec2_norm)


# 1. 创建文本嵌入模型
embedding = OpenAIEmbeddings(model="text-embedding-3-small")

# 2. 嵌入文本
query_vector = embedding.embed_query("我是赵博祺，我喜欢打篮球")

print(query_vector)
print(len(query_vector))

# 3. 嵌入文档列表/字符串列表
document_vector = embedding.embed_documents([
    "我叫赵博祺，我喜欢打篮球",
    "这个喜欢打篮球的人叫赵博祺",
    "求知若渴，虚心若雨"
])
# 4. 计算余弦相似度
print("向量1和向量2的相似度", cosine_similarity(document_vector[0], document_vector[1]))
print("向量2和向量3的相似度", cosine_similarity(document_vector[1], document_vector[2]))
print("向量1和向量3的相似度", cosine_similarity(document_vector[0], document_vector[2]))
