import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "你正在执行一项测试，请重复用户传递的内容，除了重复其他均不操作"
    ),
    ("human", "{query}")
])
llm = ChatOpenAI(model="gpt-3.5-turbo")

# 传值给kwargs参数，调用时和原有参数合并起来一起调用
chain = prompt | llm.bind(stop="世界") | StrOutputParser()

content = chain.invoke({"query": "你好，世界！"})

print(content)
