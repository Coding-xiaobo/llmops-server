from langchain_community.document_loaders import UnstructuredMarkdownLoader

# 加载时不分割，如果分割是按照元素类型分割，后续使用文本分割器进行分割
loader = UnstructuredMarkdownLoader("./项目API资料.md")
documents = loader.load()

print(documents)
print(len(documents))
print(documents[0].metadata)
