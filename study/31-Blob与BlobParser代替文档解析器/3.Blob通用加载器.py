#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/10/6 11:48
@Author :xiaobo
@File   :3.Blob通用加载器.py
"""

from langchain_community.document_loaders.generic import GenericLoader

loader = GenericLoader.from_filesystem(".", glob="*.txt", show_progress=True)

for idx, doc in enumerate(loader.lazy_load()):
    print(f"当前正在加载第{idx}个文件,文件名:{doc.metadata['source']}")
