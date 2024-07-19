#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/7/19 16:39
@Author :xiaobo
@File   :2-接入千帆embedding.py
"""
import dotenv
from langchain_community.embeddings.baidu_qianfan_endpoint import QianfanEmbeddingsEndpoint

dotenv.load_dotenv()

embeddings = QianfanEmbeddingsEndpoint(model="bge-large-zh")

query_vector = embeddings.embed_query("我叫赵博祺，我喜欢打篮球游泳")

print(query_vector)
print(len(query_vector))
print(len(query_vector))
