# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 14:46
# @Author  : xiaoke
# @Email   : 976249817@qq.com
# @File    : app_adb_cpu.py
import os
from utils.operate_log_util import logger
from utils.operate_system_search import get_system_use_search

find = get_system_use_search()


@logger('获取cpu信息')
def collect_cpu(packagename):
    cpu = 'adb shell top -n 1| %s %s' % (find, packagename)
    # print(os.popen(cpu).readlines()[0].split())
    re_cpu = os.popen(cpu).readlines()[0].split()[2]
    return re_cpu


if __name__ == '__main__':
    print(collect_cpu("com.a1chemic.owner.android"))
