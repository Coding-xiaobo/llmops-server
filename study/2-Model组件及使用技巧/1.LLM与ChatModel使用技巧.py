#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/6/30 15:36
@Author :xiaobo
@File   :1.LLM与ChatModel使用技巧.py
"""
from datetime import datetime

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# 导入环境变量 ---> 导入秘钥
dotenv.load_dotenv()

# 1.编排prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请回答用户的问题，现在的时间是{now}"),
    ("human", "{query}"),
]).partial(now=datetime.now())

# 2.创建大语言模型
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")  # 导入模型

# llm.invoke可以接收多种数据类型：BaseMessage, List[str], Tuple[str, str], str, Dict[str, Any]
# 底层会将他们都转换成消息列表，然后再传递给聊天模型
ai_message = llm.invoke(prompt.invoke({"query": "现在是几点，请讲一个程序员的冷笑话"}))

print(ai_message.type)
print(ai_message.content)
"""
{'token_usage': {'completion_tokens': 46, 'prompt_tokens': 69, 'total_tokens': 115}, 'model_name': 'gpt-3.5-turbo-16k-0613', 'system_fingerprint': 'fp_b28b39ffa8', 'finish_reason': 'stop', 'logprobs': None}
"""
print(ai_message.response_metadata)
