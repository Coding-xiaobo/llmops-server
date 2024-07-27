#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/7/27 16:36
@Author :xiaobo
@File   :vector_database_service.py
"""
import os

import weaviate
from injector import inject
from langchain_weaviate import WeaviateVectorStore
from langchain_openai import OpenAIEmbeddings
from weaviate import WeaviateClient


@inject
class VectorDatabaseService:
    """向量数据库服务"""
    client: WeaviateClient
    vector_store: WeaviateVectorStore

    def __init__(self):
        """构造函数，完成向量数据库服务的客户端+Langchain向量书实例的创建"""
        # 1. 创建/连接weaviate向量数据库
        self.client = weaviate.connect_to_local(
            host=os.getenv("WEAVIATE_HOST"),
            port=int(os.getenv("WEAVIATE_PORT"))
        )
        # 2. 创建langchain向量数据库
        self.vector_store = WeaviateVectorStore(
            client=self.client,
            index_name="Dataset",
            text_key="text",
            embedding=OpenAIEmbeddings(model="text-embedding-3-small")
        )
