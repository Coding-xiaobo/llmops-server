#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/7/28 17:53
@Author :xiaobo
@File   :自定义加载器使用.py
"""
from typing import Iterator, AsyncIterator

from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document


class CustomDocumentLoader(BaseLoader):
    """
    自定义文档加载器，将文本文件的每一行都解析成Document
    需要实现lazy_load、alazy_load
    """

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    """
    每次调用 lazy_load 函数的迭代器的 next() 方法时，
    它都会读取文件的下一行，
    并创建一个新的 Document 实例，然后返回这个实例。
    这样，Document 实例是按需生成的，而不是一次性全部加载到内存中，这有助于提高内存效率，特别是在处理大文件时
    """

    def lazy_load(self) -> Iterator[Document]:
        # 1.读取对应的文件
        with open(self.file_path, encoding="utf-8") as f:
            line_number = 0
            # 2.提取文件的每一行
            for line in f:
                # 3.将每一行生成一个Document实例并通过yield返回
                yield Document(
                    page_content=line,
                    metadata={"score": self.file_path, "line_number": line_number}
                )
                line_number += 1

    async def alazy_load(self) -> AsyncIterator[Document]:
        # 异步操作文件的库
        import aiofiles
        async with aiofiles.open(self.file_path, encoding="utf-8") as f:
            line_number = 0
            async for line in f:
                yield Document(
                    page_content=line,
                    metadata={"score": self.file_path, "line_number": line_number}
                )
                line_number += 1


loader = CustomDocumentLoader("./喵喵.txt")
documents = loader.load()

print(documents)
print(len(documents))
print(documents[0].metadata)
