#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/10/6 11:43
@Author :xiaobo
@File   :2.Blob加载器.py
"""
from langchain_community.document_loaders.blob_loaders import FileSystemBlobLoader

loader = FileSystemBlobLoader(".", show_progress=True)

for blob in loader.yield_blobs():
    # 一个blob是一个文件
    print(blob.as_string())
