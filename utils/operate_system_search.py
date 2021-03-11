# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 20:36
# @Author  : xiaoke
# @Email   : 976249817@qq.com
# @File    : operate_system_search.py

import platform
from utils.operate_log_util import logger


@logger("根据不同的系统，使用相应的搜索命令")
def get_system_use_search():
    sys = platform.system()
    if sys == "Windows":
        search_commond = "findstr"
    else:
        search_commond = "grep"
    return search_commond
