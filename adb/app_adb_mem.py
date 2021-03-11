# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 14:59
# @Author  : xiaoke
# @Email   : 976249817@qq.com
# @File    : app_adb_mem.py

import os
from utils.operate_log_util import logger
from utils.operate_system_search import get_system_use_search

find = get_system_use_search()


@logger('获取内存')
def collect_mem(packagename):
    cpu = 'adb shell top -n 1| %s %s' % (find, packagename)
    # rss实际使用物理内存
    rss_cpu = os.popen(cpu).readlines()[0].split()[6]
    return rss_cpu


if __name__ == '__main__':
    print(collect_mem("com.a1chemic.owner.android"))
