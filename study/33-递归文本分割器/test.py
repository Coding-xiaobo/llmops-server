#!/user/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/8/10 14:19
@Author :xiaobo
@File   :test.py
"""


def test(*args, a, b=1):
    print(args, a, b)


s = (1, 2)
test(a=1, b=2, *s)
