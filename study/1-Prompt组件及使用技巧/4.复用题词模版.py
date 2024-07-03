#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/6/30 13:04
@Author :xiaobo
@File   :复用提示模版.py
"""
from langchain_core.prompts import PromptTemplate, PipelinePromptTemplate

full_template = PromptTemplate.from_template("""{instruction}
{example}
{start}

""")

# 描述模板
instruction_prompt = PromptTemplate.from_template("你正在模拟{person}")

# 示例模板
example_prompt = PromptTemplate.from_template("""下面是一个交互例子：

Q: {example_q}
A: {example_a}""")

# 开始模板
start_prompt = PromptTemplate.from_template("""现在，你是一个真实的人，请回答用户的问题:

Q: {input}
A:""")

pipeline_prompts = [
    ("instruction", instruction_prompt),
    ("example", example_prompt),
    ("start", start_prompt)
]

# final_prompt 最完整的模版
# pipeline_prompts 列表，值是一个元组，第一个值是full_template中的变量信息，第二个值是替换的模版
pipeline_prompt = PipelinePromptTemplate(
    final_prompt=full_template,
    pipeline_prompts=pipeline_prompts,
)

"""
input_variables=['example_a', 'input', 'example_q', 'person'] final_prompt=PromptTemplate(input_variables=['example', 'instruction', 'start'], template='{instruction}\n{example}\n{start}\n\n') pipeline_prompts=[('instruction', PromptTemplate(input_variables=['person'], template='你正在模拟{person}')), ('example', PromptTemplate(input_variables=['example_a', 'example_q'], template='下面是一个交互例子：\n\nQ: {example_q}\nA: {example_a}')), ('start', PromptTemplate(input_variables=['input'], template='现在，你是一个真实的人，请回答用户的问题:\n\nQ: {input}\nA:'))]
"""

print(pipeline_prompt)  # 合并成功

"""
你正在模拟雷军
下面是一个交互例子：

Q: 你最喜欢的汽车是什么?
A: 小米su7
现在，你是一个真实的人，请回答用户的问题:

Q: 你最喜欢的手机是什么?
A:
"""
print(pipeline_prompt.invoke({
    "person": "雷军",
    "example_q": "你最喜欢的汽车是什么?",
    "example_a": "小米su7",
    "input": "你最喜欢的手机是什么?"
}).to_string())
