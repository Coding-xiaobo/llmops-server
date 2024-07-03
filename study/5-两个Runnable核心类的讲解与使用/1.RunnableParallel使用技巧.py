#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/6/30 23:14
@Author :xiaobo
@File   :1.RunnableParallel使用技巧.py
"""
import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 1.编排prompt
joke_prompt = ChatPromptTemplate.from_template("请讲一个关于{subject}的冷笑话，尽可能短一些")
poem_prompt = ChatPromptTemplate.from_template("请写一篇关于{subject}的诗，尽可能短一些")

# 2.创建大语言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

# 3.创建输出解析器
parser = StrOutputParser()

# 4.编排链
joke_chain = joke_prompt | llm | parser
poem_chain = poem_prompt | llm | parser

# 5.并行链 并行执行传入的Runnable链
"""
RunnableParallel支持调用invoke，并且返回字典
Prompt恰好输入的就是字典，所以可以把RunnableParallel格式化的输入放入链中
"""
map_chain = RunnableParallel(joke=joke_chain, poem=poem_chain)
# map_chain = RunnableParallel({
#     "joke": joke_chain,
#     "poem": poem_chain,
# })

res = map_chain.invoke({"subject": "程序员"})
"""
{'joke': '为什么程序员总是冷静？\n因为他们总是在处理 bug！', 'poem': '在代码的世界里徘徊，\n逐行追寻着思维的光芒。\n逻辑交织成诗意的舞蹈，\n程序员，书写着未来的方向。'}
"""
print(res)
