# -*- coding=utf-8 -*-
r"""

"""


def getApiDescription() -> str:
    from os.path import dirname, join
    with open(join(dirname(__file__), 'description.md')) as file:
        return file.read()
